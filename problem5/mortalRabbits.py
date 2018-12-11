def mortal_rabbits(n, k):
	ages = [1] + [0]*(k-1)
	for i in xrange(n-1):
		ages = [sum(ages[1:])] + ages[:-1]
		print ages
	return sum(ages)


print mortal_rabbits(89,20)
