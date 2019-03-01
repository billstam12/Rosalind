import imp
from math import factorial
bio = imp.load_source('bioLibrary', '/home/bill/Documents/ML_Projects/Rosalind/bioLibrary.py')

def distanceMatrix(seqs):
	l = len(sequences[0]) #get length
	distMat = []
	for i in range(len(sequences)):
		distances = []
		for j in range(len(sequences)):
			distances.append(float(bio.hammingDistance(sequences[i],sequences[j]))/l)
		distMat.append(distances)

	return distMat

sequences = []
for d in bio.fastaIter("dataset.txt"):
	sequences.append(d[1])

distMat = (distanceMatrix(sequences))
for d in distMat:
	print( " ".join(str(x) for x in d))
