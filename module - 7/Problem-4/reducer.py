#!/usr/bin/env python
"""reducer.py"""

from operator import itemgetter
import sys

relations = []
for line in sys.stdin:
	line = line.strip()
	data = line.split('\t', 1)
	normaldata = [data[0], data[1]]
	if normaldata not in relations:
		relations.append(normaldata)
	else:
		relations.remove(normaldata)
	reversedata = [data[1], data[0]]
	if reversedata not in relations:
		relations.append(reversedata)
	else:
		relations.remove(reversedata)
for relation in relations:
	print '%s' % relation
