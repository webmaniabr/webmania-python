#!/usr/bin/env python3
"""Executable first-use example for a controlled loopback fixture, no real API."""
import argparse
from urllib.parse import urlsplit
from webmania import CompanyCredentials, NfeClient


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--base-url',required=True);a=p.parse_args()
    if urlsplit(a.base_url).hostname not in ['127.0.0.1','localhost','::1']:raise SystemExit('Controlled quickstart requires loopback.')
    creds=CompanyCredentials('synthetic-key','synthetic-secret','synthetic-access','synthetic-access-secret')
    with NfeClient(creds,base_url=a.base_url) as client:
        certificate=client.get_certificate_validity()
        sefaz=client.get_sefaz_status()
        # Explicit checks: they must also run under python -O.
        if certificate.get('expiration')!=30:raise SystemExit('Unexpected certificate validity response.')
        if sefaz.get('status')!='online':raise SystemExit('Unexpected SEFAZ status response.')
    print('controlled quickstart passed')


if __name__=='__main__':main()
