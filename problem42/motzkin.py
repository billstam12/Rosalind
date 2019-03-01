import imp
from math import factorial
bio = imp.load_source('bioLibrary', '/home/bill/Documents/ML_Projects/Rosalind/bioLibrary.py')

cache = {}
match = lambda s, t: set([s, t]) == set(['A', 'U']) or set([s, t]) == set(['C', 'G'])

def motzkinNumbers(s):
	if s in cache:
		return cache[s]
	else:
		output = 1L
		if len(s) == 2 and match(s[0], s[1]):
			output = 2L
		elif len(s) > 2:
			output = motzkinNumbers(s[1:]) + sum([match(s[0], s[k]) * motzkinNumbers(s[1: k])
					* motzkinNumbers(s[k + 1:]) for k in range(1, len(s))])
			output %= 10e6
		cache[s] = output
		
		return int(output)



for i in bio.fastaIter("dataset.txt"):
	print motzkinNumbers(i[1]) % 10**6
