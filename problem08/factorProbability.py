def factorProbability(k, m, n):
	total = k + m + n
	total2 = total - 1

	prob = k/total + m/total * ( (k/total2) + (0.75*((m-1)/total2)) + (0.5*(n/total2)) ) + n/total * ( (k/total2) + (0.5*(m/total2)) )

	return prob
	
k = 23
m = 25
n = 21
prob = factorProbability(k,m,n)
print (prob)
