from math import factorial

def countSubsets(n):
	count = 1
	for i in range(1, n+1):
		print i,n
		count += factorial(n)/(factorial(i)*factorial(n-i))
	return count % 1000000

print countSubsets(864)