#!/usr/bin/env python
"""reducer.py"""

from operator import itemgetter
import sys

strings = []
for line in sys.stdin:
	line = line.strip()
	line = line.strip("\"")
	length = len(line)
	length = length - 10
	line = line[0: length]
	if line not in strings:
		strings.append(line)
		print "%s" % line
