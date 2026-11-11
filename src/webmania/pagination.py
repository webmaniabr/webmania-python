"""Bounded pull iterators with explicit, filter-bound continuation state."""
from __future__ import annotations
from dataclasses import dataclass
import json
from .errors import WebmaniaError
from .transport import positive


@dataclass(frozen=True, repr=False)
class PageContinuation:
    _binding: str
    _page: int
    _offset: int
    _page_size: int

    def __repr__(self): return 'PageContinuation([private filters])'


class PageIterator:
    def __init__(self, fetch, query, max_pages, max_items, continuation, options, identity):
        if not positive(max_pages, True) or max_items is not None and not positive(max_items, True):
            raise WebmaniaError('configuration', 'Pagination limits must be positive integers.')
        invalid = False
        try:
            if query is not None and not isinstance(query, dict): raise ValueError
            params = dict(query or {})
            if any(not isinstance(k, str) for k in params): raise ValueError
            encoded = json.dumps(params, sort_keys=True, ensure_ascii=False, allow_nan=False, separators=(',', ':'))
            encoded.encode('utf-8')
            params = json.loads(encoded)
        except (ValueError, TypeError, UnicodeError, RecursionError): invalid = True
        if invalid: raise WebmaniaError('validation', 'Expected finite Unicode pagination filters.')
        self.page = params.pop('page', 1)
        if not positive(self.page, True) or 'per_page' in params and not positive(params['per_page'], True):
            raise WebmaniaError('validation', 'Page and page size must be positive integers.')
        self.binding = json.dumps([identity, params], sort_keys=True, ensure_ascii=True, separators=(',', ':'))
        self.page_size = params.get('per_page')
        self.offset = 0
        if continuation is not None:
            if not isinstance(continuation, PageContinuation) or continuation._binding != self.binding:
                raise WebmaniaError('pagination', 'Continuation requires unchanged filters and page size.')
            if not positive(continuation._page, True) or not positive(continuation._page_size, True) or type(continuation._offset) is not int or not 0 <= continuation._offset < continuation._page_size:
                raise WebmaniaError('pagination', 'Invalid continuation position.')
            if query is not None and 'page' in query and query['page'] != continuation._page:
                raise WebmaniaError('pagination', 'Continuation controls the next page.')
            self.page, self.offset, self.page_size = continuation._page, continuation._offset, continuation._page_size
        self.fetch, self.params, self.options = fetch, params, options
        self.max_pages, self.max_items = max_pages, max_items
        self.pages = self.yielded = 0
        self.items = None
        self.index = 0
        self.last_page = None
        self.continuation = None
        self.finished = False

    def __iter__(self): return self

    def __next__(self):
        if self.finished: raise StopIteration
        if self.max_items is not None and self.yielded >= self.max_items:
            self.finished = True
            raise StopIteration
        while self.items is None or self.index >= len(self.items):
            if self.items is not None:
                if self.page >= self.last_page:
                    self.finished = True; self.continuation = None; raise StopIteration
                self.page += 1
            if self.pages >= self.max_pages:
                self.finished = True
                raise WebmaniaError('pagination', 'Pagination exceeded max_pages.')
            result = self.fetch(query={**self.params, 'page': self.page}, options=self.options)
            self.pages += 1
            meta = result['meta']
            if meta['current_page'] != self.page or meta['last_page'] < self.page or self.page_size is not None and meta['per_page'] != self.page_size:
                raise WebmaniaError('pagination', 'Pagination metadata is inconsistent with the requested page size or page.')
            self.page_size = meta['per_page']
            self.last_page = meta['last_page']
            self.items = result['data']
            if len(self.items) > self.page_size or self.offset > len(self.items):
                raise WebmaniaError('pagination', 'Pagination item bounds are inconsistent.')
            self.index, self.offset = self.offset, 0
        item = self.items[self.index]
        self.index += 1
        self.yielded += 1
        if self.index < len(self.items):
            self.continuation = PageContinuation(self.binding, self.page, self.index, self.page_size)
        elif self.page < self.last_page:
            self.continuation = PageContinuation(self.binding, self.page + 1, 0, self.page_size)
        else: self.continuation = None
        return item
