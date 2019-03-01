from math import factorial

def countSubsets2(n,m):
	count = 0
	for i in range(m, n+1):
		count += factorial(n)/(factorial(i)*factorial(n-i))
	return count % 1000000

print countSubsets2(1867, 1281)