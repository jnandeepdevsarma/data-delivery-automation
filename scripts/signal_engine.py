#!/usr/bin/env python3
import argparse
import json
import numpy as np


def compute_signals(raw):
# raw: JSON from fetch_data (example limited parsing)
# This is a placeholder — replace with your real signal logic
close = np.array([1,2,3,2,3,4])
signals = {
'trend': 'up' if close[-1] > close[0] else 'down',
'last': float(close[-1]),
'mean': float(close.mean()),
'vol': float(np.std(close))
}
return signals


if __name__ == '__main__':
import sys
p = argparse.ArgumentParser()
p.add_argument('--in', dest='infile', required=True)
p.add_argument('--out', required=True)
args = p.parse_args()
raw = json.load(open(args.infile))
signals = compute_signals(raw)
json.dump(signals, open(args.out, 'w'))
print('signals ->', args.out)