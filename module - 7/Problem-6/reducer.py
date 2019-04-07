#!/usr/bin/env python
"""reducer.py"""

from operator import itemgetter
import sys


A = []
B = []
A_rowzero = [0,0,0,0,0]
A_rowone = [0,0,0,0,0]
A_rowtwo = [0,0,0,0,0]
A_rowthree = [0,0,0,0,0]
A_rowfour = [0,0,0,0,0]
B_rowzero = [0,0,0,0,0]
B_rowone = [0,0,0,0,0]
B_rowtwo = [0,0,0,0,0]
B_rowthree = [0,0,0,0,0]
B_rowfour = [0,0,0,0,0]

for line in sys.stdin:
	line = line.strip()
	key,i,j,value = line.split(", ")
	i = int(i)
	j = int(j)
	value = int(value)
	if key == 'a':
		if i == 0:

			A_rowzero[j] = value
		if i == 1:

			A_rowone[j] = value
		if i == 2:

			A_rowtwo[j] = value
		if i == 3:

			A_rowthree[j] = value
		if i == 4:

			A_rowfour[j] = value
	else:
		if i == 0:

			B_rowzero[j] = value

		if i == 1:
			B_rowone[j] = value
		if i == 2:
			B_rowtwo[j] = value
		if i == 3:
			B_rowthree[j] = value
		if i == 4:
			B_rowfour[j] = value
A.append(A_rowzero)
A.append(A_rowone)
A.append(A_rowtwo)
A.append(A_rowthree)
A.append(A_rowfour)
B.append(B_rowzero)
B.append(B_rowone)
B.append(B_rowtwo)
B.append(B_rowthree)
B.append(B_rowfour)

result = [[sum(a * b for a, b in zip(A_row, B_col))
                        for B_col in zip(*B)]
                                for A_row in A]
for row in result:
    for col in row:
	print '%s' % [result.index(row), row.index(col), col]
