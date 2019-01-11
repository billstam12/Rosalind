# Given positive integer k <= 7
# Find the number of possible permutations
# Find and print those permutations of length k
import math
import itertools

def noOfPerm(k):
	return math.factorial(k)

def possiblePerm(k, n):
	arr_start = []
	for i in range(k):
		arr_start.append(i+1)
	
	arrs = []
	for i in itertools.permutations(arr_start):
		arrs.append(i)
	return arrs

k = 6
n = noOfPerm(k)
print n
arrs = possiblePerm(k, n)

for a in arrs:
	print " ".join(str(e) for e in a)