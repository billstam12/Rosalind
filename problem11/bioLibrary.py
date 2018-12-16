from itertools import groupby
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
		headerStr = header.next()[1:].strip()

		# join all sequence lines to one.
		seq = "".join(s.strip() for s in faiter.next())

		yield (headerStr, seq)

def countGC(seq):
	counts = Counter(seq[1])
	return ((counts['G'] + counts['C'])/(counts['G'] + counts['C'] + counts['A'] + counts['T']))

def hammingDistance(s1,s2):
    assert len(s1) == len(s2) #Must be of equal lengths
    return sum(c1 != c2 for c1, c2 in zip(s1, s2))


codons = {
"UUU" : "F",
"CUU" : "L",
"AUU" : "I",
"GUU" : "V",
"UUC" : "F",
"CUC" : "L",
"AUC" : "I",
"GUC" : "V",
"UUA" : "L",
"CUA" : "L",
"AUA" : "I",     
"GUA" : "V",
"UUG" : "L",
"CUG" : "L",
"AUG" : "M",
"GUG" : "V",
"UCU" : "S",
"CCU" : "P",
"ACU" : "T",
"GCU" : "A",
"UCC" : "S",
"CCC" : "P",
"ACC" : "T",
"GCC" : "A",
"UCA" : "S",
"CCA" : "P",
"ACA" : "T",
"GCA" : "A",
"UCG" : "S",
"CCG" : "P",
"ACG" : "T",
"GCG" : "A",
"UAU" : "Y",
"CAU" : "H",
"AAU" : "N",
"GAU" : "D",
"UAC" : "Y",
"CAC" : "H",
"AAC" : "N",
"GAC" : "D",
"UAA" : "Stop",
"CAA" : "Q",
"AAA" : "K",
"GAA" : "E",
"UAG" : "Stop",
"CAG" : "Q",
"AAG" : "K",
"GAG" : "E",
"UGU" : "C",
"CGU" : "R",
"AGU" : "S",
"GGU" : "G",
"UGC" : "C",
"CGC" : "R",
"AGC" : "S",
"GGC" : "G",
"UGA" : "Stop",
"CGA" : "R",
"AGA" : "R",
"GGA" : "G",
"UGG" : "W",
"CGG" : "R",
"AGG" : "R",
"GGG" : "G"
}

def dnaToAA(dna):
	aminoacid = []
	for i in range(0, len(dna), 3):
		dna3 = (dna[i:i+3])
		amino = codons[dna3]
		if(amino == "Stop"):
			return "".join(aminoacid)
		else:
			aminoacid.append(amino)
	return "".join(aminoacid)