from bioLibrary import *
import math

def perfectMatch(rna):
	u = 0
	g = 0
	for i in range(len(rna)):
		if rna[i] == "U":
			u += 1
		elif rna[i] == "G":
			g += 1
	return math.factorial(u)*math.factorial(g)
	
for i in fastaIter("dataset.txt"):
	print perfectMatch(i[1])