#!/usr/bin/env python
"""mapper.py"""

import sys

for line in sys.stdin:
	line = line.strip()
	line = line.strip("[")
	line = line.strip("]")
	data = line.split(", ")
	print '%s' % data[1]
