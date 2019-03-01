import imp
bio = imp.load_source('bioLibrary', '/home/bill/Documents/ML_Projects/Rosalind/bioLibrary.py')
import numpy as np
import re
from itertools import product, chain

def order_strings(dictionary, strs):
	print dictionary
	permutations = list(chain(strs))
	srt_perms = sorted(permutations, key = lambda word: [dictionary.index(c) for c in word])
	return srt_perms

def order_lex(dictionary, n):
	strs = []
	dictionary = "".join(str(x) for x in dictionary)
	for i in range(1,n+1):
		for p in product(dictionary, repeat = i):
			strs.append("".join(x for x in p))
	return order_strings(dictionary, strs)
	


f = open("dataset.txt", "r")
dictionary =  (f.readline().strip().split())
n =  int(f.readline())


for p in order_lex(dictionary, n):
	print p