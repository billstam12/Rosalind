import imp
from math import factorial
bio = imp.load_source('bioLibrary', '/home/bill/Documents/ML_Projects/Rosalind/bioLibrary.py')

import math

d = bio.dna("GCGCCTACCACTGTTCATCGCCGCAGTTGATGGGAACGTTAGGCGTGGAGGGGTACCAAGCGGGAAAAATCACCGAGCTGGAGAGCAATACAGGGGG")
arr = [0.092 ,0.139 ,0.237 ,0.272 ,0.332 ,0.378 ,0.469 ,0.538 ,0.587 ,0.628 ,0.739 ,0.759 ,0.843 ,0.880]

def randomString(d, arr):
	table = []
	for p in arr:
		total_p = 0
		dic = {
			'A' : (1 - p)/2,
			'T' : (1 - p)/2,
			'G' : p/2,
			'C' : p/2
		}
		
		d.countBases()
		#total_p = p_g*d.g*p_t*d.t*p_c*d.c*p_a*d.a
		for i, a in enumerate(d.string):
			if(i == 0):
				total_p = dic[a]
			else:
				total_p *= dic[a]
		table.append(math.log10(total_p))
	return table

tb = randomString(d, arr)
print(" ".join(str(x) for x in tb))