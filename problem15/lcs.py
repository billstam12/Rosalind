def longest_common_substring(s1, s2):
	m = [[0] * (1 + len(s2)) for i in xrange(1 + len(s1))]
	longest, x_longest = 0, 0
	for x in xrange(1, 1 + len(s1)):
		 for y in xrange(1, 1 + len(s2)):
			  if s1[x - 1] == s2[y - 1]:
					m[x][y] = m[x - 1][y - 1] + 1
					if m[x][y] > longest:
						longest = m[x][y]
						x_longest = x
			  else:
				  m[x][y] = 0
	return s1[x_longest - longest: x_longest]

from bioLibrary import *
seq =  fastaIter("dna.FASTA")
seqs = []
for s in seq:
	seqs.append(s)
import numpy as numpy
seqs = np.array(seqs)

for i in range((seqs.shape)[0]):
	for j in range(i+1,(seqs.shape)[0]):
		print longest_common_substring(seqs[i][1],seqs[j][1])