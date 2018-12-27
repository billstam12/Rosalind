import math
def independentAlleles(k, n):
	i = 0
	# Probability of an organism born to two
	# Aa Bb parents, being Aa Bb is 1/2*1/2 = 1/4
	population_total = 0.0
	prob = 0.0
	population_total = 2**k
	for i in range(n, population_total+1):
		success = (0.25)**i
		failure = (0.75)**(population_total - i)
		prob += (failure*success)*math.factorial(population_total)/(math.factorial(i)*math.factorial(population_total-i))
		i+=1

	return prob
independentAlleles(6,16)