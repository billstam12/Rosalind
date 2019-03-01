import imp
from math import factorial
bio = imp.load_source('bioLibrary', '/home/bill/Documents/ML_Projects/Rosalind/bioLibrary.py')

def failureArray(s):
	fa = [0] * len(s)
	fa[0] = 0
	for i in range(1,len(s)):
		j =  fa[i - 1]
		while(s[i]!=s[j] and j > 0):
			j = fa[j - 1]
		if s[i] == s[j]:
			j+=1
		fa[i] = j
		
	return fa

for d in bio.fastaIter("dataset.txt"):
	fa = failureArray(d[1])
	print " ".join(str(x) for x in fa)