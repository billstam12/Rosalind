import imp
from math import factorial
bio = imp.load_source('bioLibrary', '/home/bill/Documents/ML_Projects/Rosalind/bioLibrary.py')


def maximumMatchings(r):
	A, C, G, U = r.countBases()
	AU = factorial(max(A, U)) / factorial(max(A, U) - min(A, U))
	GC = factorial(max(G, C)) / factorial(max(G, C) - min(G, C))
	return (AU)*(GC)

for r in bio.fastaIter("dataset.txt"):
	print maximumMatchings(bio.rna(r[1].strip()))