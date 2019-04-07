#!/usr/bin/env python

import sys
import json

def mapper(record):
	key = record[0]
	value = record[1].strip()
	words = value.split()
	seen = {}
	for w in words:
		intermediate = {}
		if (not seen.get(w,False)):
			seen[w]	= True
			intermediate.setdefault(w, [])
			intermediate[w].append(key)
			print w, intermediate[w]

for line in sys.stdin:
			record = json.loads(line)
			mapper(record)
