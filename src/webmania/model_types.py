"""Retain defining-module context on generated runtime type aliases."""
from __future__ import annotations
from typing import ForwardRef, Union, get_args, get_origin


def bind_types(namespace, module, names):
    # TypedDict records its module automatically. Plain aliases containing a
    # string ForwardRef do not; consumers evaluate method hints in another
    # module. Attach that context without changing their static definitions.
    for _ in range(len(names)):
        changed = False
        for name in names:
            value = namespace[name]
            if isinstance(value, str) and value != name and value in namespace and namespace[value] != value:
                namespace[name] = namespace[value]; changed = True
        if not changed: break

    def bind(value, active=frozenset()):
        if isinstance(value, (str, ForwardRef)):
            argument = value if isinstance(value, str) else value.__forward_arg__
            if argument.isidentifier() and argument in namespace and argument not in active:
                return bind(namespace[argument], active | {argument})
            return ForwardRef(argument, module=module)
        origin = get_origin(value)
        args = get_args(value)
        if origin is Union:
            return Union[tuple(bind(arg, active) for arg in args)]
        if origin is list:
            return list[bind(args[0], active)]
        return value

    for name in names:
        namespace[name] = bind(namespace[name])
