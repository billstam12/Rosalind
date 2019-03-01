import imp
from math import factorial
bio = imp.load_source('bioLibrary', '/home/bill/Documents/ML_Projects/Rosalind/bioLibrary.py')


def matchingRandoms(dna, p, n):
	dic = {
		'A' : (1 - p)/2,
		'T' : (1 - p)/2,
		'G' : p/2,
		'C' : p/2
	}
		
	d.countBases()
	total_p = 0
	for i, a in enumerate(d.string):
		if(i == 0):
			total_p = dic[a]
		else:
			total_p *= dic[a]

	return 1 - (1-total_p)**n


 

d = bio.dna("GTACCCCT")
gc = 0.445696
n = 87320

print matchingRandoms(d, gc, n)