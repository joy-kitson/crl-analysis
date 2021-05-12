#!/usr/bin/env python3

import argparse
import OpenSSL
import time
import calendar

def parse_args():
    parser = argparse.ArgumentParser()

    # Optional/named arguments
    parser.add_argument('-i', '--input', default='gds5-16.crl')
    
    return parser.parse_args()

def read_crl(path, is_asn1=True):
    with open(path, 'rb') as f:
        raw_crl = f.read()

    if is_asn1:
        return OpenSSL.crypto.load_crl(OpenSSL.crypto.FILETYPE_ASN1, raw_crl)
    else:
        return OpenSSL.crypto.load_crl(OpenSSL.crypto.FILETYPE_PEM, raw_crl)

def try_decode(byte_string):
    try:
        return byte_string.decode('UTF-8')
    except:
        return None

def main():
    args = parse_args()

    crl = read_crl(args.input)
    issuer = crl.get_issuer().organizationName

    print('issuer,serial,reason,date')
    for r in crl.get_revoked():
        serial = try_decode(r.get_serial())
        reason = try_decode(r.get_reason())
        rev_date = try_decode(r.get_rev_date())
        rev_date = calendar.timegm(time.strptime(rev_date, '%Y%m%d%H%M%SZ'))
        print(f'"{issuer}",{serial},"{reason}",{rev_date}')

if __name__ == '__main__':
    main()
