#!/usr/bin/env python3
import argparse
import json
import pandas as pd
import requests


def fetch():
# replace with your chosen data source
# example: fetch ES / NIFTY / custom API
url = "https://query1.finance.yahoo.com/v7/finance/chart/%5ENSEI?range=5d&interval=60m"
r = requests.get(url, timeout=20)
return r.json()


if __name__ == '__main__':
p = argparse.ArgumentParser()
p.add_argument('--out', required=True)
args = p.parse_args()
data = fetch()
with open(args.out, 'w') as f:
json.dump(data, f)
print('fetched ->', args.out)