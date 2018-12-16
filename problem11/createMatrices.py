from bioLibrary import *
import numpy as np

def profileMatrix(file):
	matrix = []
	seq  = fastaIter("dna.FASTA")
	for s in seq:
		matrix.append(list(s[1]))
	
	A = []
	G = []
	C = []
	T = []
	for j in range(len(matrix[0])):
		a = 0
		t = 0
		g = 0
		c = 0
		
		for i in matrix:
			if(i[j]=='A'):
				a += 1
			if(i[j]=='G'):
				g += 1
			if(i[j]=='C'):
				c += 1
			if(i[j]=='T'):
				t += 1
		A.append(a)
		G.append(g)
		C.append(c)
		T.append(t)
	return np.matrix([A,G,C,T])

def concensus(profile):
	conc = []
	for i in profile.T:
		id =  np.argmax(i)
		if(id==0):
			conc.append("A")
		elif(id==1):
			conc.append("G")
		elif(id==2):
			conc.append("C")
		elif(id==3):
			conc.append("T")
	return "".join(conc)

profile = profileMatrix("dna.FASTA")
conc = concensus(profile)
print str(conc)

import pandas as pd 
profile = pd.DataFrame(profile)
profile.to_csv("profile_matrix.csv")
