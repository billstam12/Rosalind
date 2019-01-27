
from bioLibrary import *
cache = {'':1, 'A':0, 'C':0, 'G':0, 'U':0, 'AA':0, 'AC':0, 'AG':0, 'AU':1, 'CA':0, 'CC':0,
		'CG':1, 'CU':0, 'GA':0, 'GC':1, 'GG':0, 'GU':0, 'UA':1, 'UC':0, 'UG':0, 'UU':0}

def countRNA2Structures(seq):
	# if sequence not in dictionary
	if seq not in cache:
		# iterate over range by 2's as we don't want odd lengths
		tmp = []
		for k in range(1, len(seq), 2):
			''' Multiply first half of the string * the first nt and ending nt of first half
			* second half
			This multiplication is to combine the number of noncrossing
			perfect matches from the subproblems.
			The actual value/counts comes from the dynamically generated dictionary.
			'''
			tmp.append(countRNA2Structures(seq[1:k]) * cache[seq[0]+seq[k]] * countRNA2Structures(seq[k+1:]))
		# assign current sequence into dictionary for later use
		cache[seq] = sum(tmp)
		print cache
	return cache[seq]


for i in fastaIter("dataset.txt"):
	print countRNA2Structures(i[1]) % 10**6
