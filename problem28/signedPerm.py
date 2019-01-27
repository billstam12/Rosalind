from itertools import permutations

def checkDup(p):
	for obj in p:
		if -obj in p:
			return 0
	return 1

def signedPerm(n):
	orders = []
	for i in range(-n, n+1):
		if i != 0:
			orders.append(i)

	count = 0 
	for p in permutations(orders, r = n):
		if (0!=checkDup(p)):
			count+=1
			print " ".join('%2d'%x for x in p)

	print count
n = 4
signedPerm(n)