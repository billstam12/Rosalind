from itertools import groupby
from itertools import groupby
from collections import Counter
import numpy as np
import math

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

def profileMatrix(file):
	matrix = []
	seq  = fastaIter("dna.FASTA")
	for s in seq:
		matrix.append(list(s[1]))
	
	A = []
	G = []
	C = []
	T = []
	for j in range(len(matrix[0])):
		a = 0
		t = 0
		g = 0
		c = 0
		
		for i in matrix:
			if(i[j]=='A'):
				a += 1
			if(i[j]=='G'):
				g += 1
			if(i[j]=='C'):
				c += 1
			if(i[j]=='T'):
				t += 1
		A.append(a)
		G.append(g)
		C.append(c)
		T.append(t)
	return np.matrix([A,G,C,T])

def concensus(profile):
	conc = []
	for i in profile.T:
		id =  np.argmax(i)
		if(id==0):
			conc.append("A")
		elif(id==1):
			conc.append("G")
		elif(id==2):
			conc.append("C")
		elif(id==3):
			conc.append("T")
	return "".join(conc)

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
	return overlap #RETURN LIST of tuples]

def longestCommonSubstring(s1, s2):
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

def independentAlleles(k, n):
	i = 0
	# Probability of an organism born to two
	# Aa Bb parents, being Aa Bb is 1/2*1/2 = 1/4
	population_total = 0.0
	prob = 0.0
	population_total = 2**k
	for i in range(n, population_total+1):
		success = (0.25)**i
		failure = (0.75)**(population_total - i)
		prob += (failure*success)*math.factorial(population_total)/(math.factorial(i)*math.factorial(population_total-i))
		i+=1

	return prob

aa_nums = {
	"F" : 2,
	"L" : 6,	
	"S" : 6,
	"Y" : 2,
	"Stop" : 3,
	"C" : 2,
	"W" : 1,
	"P" : 4,
	"H" : 2,
	"Q" : 2,
	"R" : 6,
	"I" : 3,
	"M" : 1,
	"T" : 4,
	"N" : 2,
	"K" : 2,
	"V" : 4,
	"A" : 4,
	"D" : 2,
	"E" : 2,
	"G" : 4
}


def noOfRNAStrings(str):
	prob = 1
	for i in str:
		prob *= (aa_nums[i])
		prob = prob%1000000
	prob *= 3
	prob = prob % 1000000
	return prob


def getStartPos(dna):
	startIndexes = []
	for i in range(0, len(dna), 1):
		dna3 = (dna[i:i+3])
		if(len(dna3) == 3):
			amino = codons[dna3]
			if(amino == "M"):
				startIndexes.append(i)
	return startIndexes

def dnaToAAUpdated(dna):
	aas = []
	startIndexes = getStartPos(dna)
	for s in range(len(startIndexes)):
		aas.append(dnaToAA(dna[startIndexes[s]:]))
	return aas

weights =  {
	"A" :  71.03711,
	"C" : 103.00919,
	"D" :115.02694,
	"E" :  129.04259,
	"F" :   147.06841,
	"G" :  57.02146,
	"H" :  137.05891,
	"I" :  113.08406,
	"K" :  128.09496,
	"L" :  113.08406,
	"M" :  131.04049,
	"N" :  114.04293,
	"P" :  97.05276,
	"Q" :  128.05858,
	"R" :  156.10111,
	"S" :  87.03203,
	"T" :  101.04768,
	'V' :  99.06841,
	'W' :  186.07931,
	"Y" :  163.06333 
}

def totalWeight(protein):
	weight = 0
	for i in protein:
		weight += weights[i]
	return weight


