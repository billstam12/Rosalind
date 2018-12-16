from bioLibrary import *
import numpy as np

def overlapGraph(file, o):
	suffixes = []
	prefixes = []
	seq_names = []
	seq  = fastaIter("dna.FASTA")
	for s in seq:
		prefixes.append(s[1][:o])
		suffixes.append(s[1][-o:])
		seq_names.append(s[0])
	overlap = []
	for i in range(len(prefixes)):
		for j in range(len(suffixes)):
			if ((prefixes[i] == suffixes[j]) & (i!=j)):
				overlap.append((seq_names[j],seq_names[i]))
	return overlap #RETURN LIST of tuples

overlap = overlapGraph("dna.FASTA", 3)
for o in overlap:
	print o[0],o[1]