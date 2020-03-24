"""
You have three $20 dollar bills, five $10 dollar bills, two $5 dollar bills, and five $1 dollar bills.
How many ways can you make change for a $100 dollar bill?
"""

import itertools as iter

def findCombinations(total, currency):
	bills = []
	for x in currency:
		for y in range(x[1]):
			bills.append(x[0])

	#finding the answer
	answer = []
	length = len(bills)
	for pair in range(length+1):
		for combinations in iter.combinations(bills, pair):
			if sum(combinations) == total:
				answer.append(combinations)
	return len(set(answer))

bills = [[20, 3], [10, 5], [5, 2], [1, 5]]
input = [100, bills]
print(findCombinations(input[0], input[1]))