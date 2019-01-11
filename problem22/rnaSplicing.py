from bioLibrary import *

def splice(string, substrings):
	for s in substrings:
		string = string.replace(s, '')
	return string

substrings = []
for i,d in enumerate(fastaIter("dna.txt")):
	if i == 0:
		string = d[1]
	else:
		substrings.append(d[1])

string =  splice(string, substrings)
rna = dnaToRna(string)
print dnaToAA(rna)