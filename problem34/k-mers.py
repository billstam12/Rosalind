import imp
bio = imp.load_source('bioLibrary', '/home/bill/Documents/ML_Projects/Rosalind/bioLibrary.py')
import numpy as np
import re
from itertools import product

n = 4
def kMerComposition(st, k):
	st = st.strip()
	strs = "ACGT"
	subs = product(strs, repeat = k)
	kmers = []
	for s in subs:
		kmers.append("".join(x for x in s))
	
	mat = []
	for km in (kmers):
		mat.append((len(re.findall("(?=" + km + ")" ,st))))
	print " ".join('%2d'%x for x in mat)

for d in bio.fastaIter("dataset.txt"):
	kMerComposition(d[1].strip(), n)