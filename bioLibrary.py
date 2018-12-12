from itertools import groupby
from collections import Counter

def countBases(dna):
#begin search
    a = dna.count('A')
    c = dna.count('C')
    g = dna.count('G')
    t = dna.count('T')

    return (a,c,g,t)

def dnaToRna(dna):
	dna = list(dna)
	rna = map(lambda s: s.replace('T' , 'U'), dna)
	rna = ''.join(rna)
	return rna


def reverse(dna):
	dna = list(dna)
	reversed = dna[::-1]
	return reversed

def complement(dna):
	dna = list(dna)
	reverse = []
	for i in range(len(dna)):
		if(dna[i]) == 'T':
			reverse.append('A')
		elif(dna[i]) == 'A':
			reverse.append('T')
		elif(dna[i]) == 'C':
			reverse.append('G')
		elif(dna[i]) == 'G':
			reverse.append('C')
	reverse =''.join(reverse)
	return reverse

def fibonacci(n,k):
	if(n == 1):
		return 1
	elif(n ==2):
		return k

	one = fibonacci(n - 1, k)
	two = fibonacci(n - 2, k)

	if(n <=4):
		return (one + two)

	return (one+ (two*k))

def fastaIter(fasta_name):
	"""
	modified from Brent Pedersen
	Correct Way To Parse A Fasta File In Python
	given a fasta file. yield tuples of header, sequence
	"""
	"first open the file outside "
	fh = open(fasta_name)

	# ditch the boolean (x[0]) and just keep the header or sequence since
	# we know they alternate.
	faiter = (x[1] for x in groupby(fh, lambda line: line[0] == ">"))

	for header in faiter:
		# drop the ">"
		headerStr = header.__next__()[1:].strip()

		# join all sequence lines to one.
		seq = "".join(s.strip() for s in faiter.__next__())

		yield (headerStr, seq)

def countGC(seq):
	counts = Counter(seq[1])
	return ((counts['G'] + counts['C'])/(counts['G'] + counts['C'] + counts['A'] + counts['T']))

def hammingDistance(s1,s2):
    assert len(s1) == len(s2) #Must be of equal lengths
    return sum(c1 != c2 for c1, c2 in zip(s1, s2))
