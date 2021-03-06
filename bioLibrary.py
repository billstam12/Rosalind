# DEPENDENCIES
# Itertools for iterationg over string,
# Collections Counter to count instances on strings
# Numpy and math for obvious reasons

# Written in python 2.7
# Vasilis Stamatopoulos

from itertools import groupby, product, chain
from collections import Counter
import numpy as np
import math
import Queue

# Needed Dictionaries

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


aminoacids = {
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

class nucleicAcid:
	def __init__(self, string):
		self.string = string
		self.a = 0
		self.c = 0 
		self.g = 0
		self.t = 0
		self.u = 0
		
		self.gcContent = 0
		self.complementString = ""
		self.reverseString = ""
		self.reverseComplementString = ""
		self.lcss = ""
		self.scss = ""
		self.maximumMatchings = 0

	def countGC(seq):
		counts = Counter(seq[1])
		self.gcContent =  ((counts['G'] + counts['C'])/(counts['G'] + counts['C'] + counts['A'] + counts['T'] + counts['U']))

	def reverse(self):
		dna = list(self.string)
		self.reverseString = dna[::-1]
		return self.reverseString

	def complement(self):
		dna = list(self.string)
		self.complementString = []
		for i in range(len(dna)):
			if(dna[i]) == 'T':
				self.complementString.append('A')
			elif(dna[i]) == 'A':
				self.complementString.append('T')
			elif(dna[i]) == 'C':
				self.complementString.append('G')
			elif(dna[i]) == 'G':
				self.complementString.append('C')
		self.complementString =''.join(self.complementString)
		return self.complementString

	def reverseComplement(self):
		self.reverseComplementString = []
		self.reverse()
		for i in range(len(self.reverseString)):
			if(self.reverseString[i]) == 'T':
				self.reverseComplementString.append('A')
			elif(self.reverseString[i]) == 'A':
				self.reverseComplementString.append('T')
			elif(self.reverseString[i]) == 'C':
				self.reverseComplementString.append('G')
			elif(self.reverseString[i]) == 'G':
				self.reverseComplementString.append('C')
		self.reverseComplementString =''.join(self.reverseComplementString)
		return self.reverseComplementString

	# Get Longest Increasing subsequence lcss
	# Using dynamic Programming
	def increasing(self, seq):
	    P = [None] * len(seq)
	    M = [None] * len(seq)

	    L = 1
	    M[0] = 0
	    for i in range(1, len(seq)):
	        lo = 0
	        hi = L
	        if seq[M[hi - 1]] < seq[i]:
	            j = hi
	        else:
	            while hi - lo > 1:
	                mid = (hi + lo) // 2
	                print M
	                if seq[M[mid - 1]] < seq[i]:
	                    lo = mid
	                else:
	                    hi = mid

	            j = lo
	        P[i] = M[j - 1]
	        if j == L or seq[i] < seq[M[j]]:
	            M[j] = i
	            L = max(L, j + 1)

	    result = []
	    pos = M[L - 1]
	    for k in range(L):
	        result.append(seq[pos])
	        pos = P[pos]

	    self.lcss = (result[::-1])
	    return self.lcss

	def decreasing(self, seq):
	    P = [None] * len(seq)
	    M = [None] * len(seq)

	    L = 1
	    M[0] = 0
	    for i in range(1, len(seq)):
	        lo = 0
	        hi = L
	        if seq[M[hi - 1]] > seq[i]:
	            j = hi
	        else:
	            while hi - lo > 1:
	                mid = (hi + lo) // 2
	                if seq[M[mid - 1]] > seq[i]:
	                    lo = mid
	                else:
	                    hi = mid

	            j = lo
	        P[i] = M[j - 1]
	        if j == L or seq[i] > seq[M[j]]:
	            M[j] = i
	            L = max(L, j + 1)
	    result = []
	    pos = M[L - 1]
	    for k in range(L):
	        result.append(seq[pos])
	        pos = P[pos]

	    self.scss = (result[::-1])
	    return self.scss

	def failureArray(seq):
		fa = [0] * len(seq)
		fa[0] = 0
		for i in range(1,len(seq)):
			j =  fa[i - 1]
			while(seq[i]!=seq[j] and j > 0):
				j = fa[j - 1]
			if seq[i] == seq[j]:
				j+=1
			fa[i] = j
			
		return fa  

class dna(nucleicAcid):

	def __init__(self, string):
		nucleicAcid.__init__(self, string)
		self.startIndexes = []
		self.aas = []

	def countBases(self):
	#begin search
		self.a = self.string.count('A')
		self.c = self.string.count('C')
		self.g = self.string.count('G')
		self.t = self.string.count('T')
		return self.a, self.c, self.g, self.t

	def dnaToRna(self):
		self.string = list(self.string)
		rna = map(lambda s: s.replace('T' , 'U'), self.string)
		rna = ''.join(rna)
		return rna

	def dnaToAA(self):
		aminoacid = []
		for i in range(0, len(self.string), 3):
			dna3 = (self.dna[i:i+3])
			amino = codons[dna3]
			if(amino == "Stop"):
				return "".join(aminoacid)
			else:
				aminoacid.append(amino)
		return "".join(aminoacid)

	def getStartPos(self):
		for i in range(0, len(self.string), 1):
			dna3 = (self.string[i:i+3])
			if(len(dna3) == 3):
				amino = codons[dna3]
				if(amino == "M"):
					self.startIndexes.append(i)

	def dnaToAAUpdated(self):
		startIndexes = getStartPos(self.string)
		for s in range(len(startIndexes)):
			self.aas.append(self.dnaToAA(self.string[startIndexes[s]:]))
	
	def kMerComposition(self, k):
		st = st.strip()
		strs = "ACGT"
		subs = product(strs, repeat = k)
		kmers = []
		for s in subs:
			kmers.append("".join(x for x in s))
		
		mat = []
		for km in (kmers):
			mat.append((len(re.findall("(?=" + km + ")" ,self.string))))

		return " ".join('%2d'%x for x in mat)

	def maximumMatchings(self):
		A, C, G, T = self.countBases()
		AT = factorial(max(A, T)) / factorial(max(A, T) - min(A, T))
		GC = factorial(max(G, C)) / factorial(max(G, C) - min(G, C))
		self.maximumMatchings = (AT*GC)
		return (AT)*(GC)

class rna(nucleicAcid):

	def __init__(self, string):
		nucleicAcid.__init__(self, string)
		self.perfectMatches = 0
		self.ncPerfectMatches = 0
		self.cachePerfectMatches = {'':1, 'A':0, 'C':0, 'G':0, 'U':0, 'AA':0, 'AC':0, 'AG':0, 'AU':1, 'CA':0, 'CC':0,
		'CG':1, 'CU':0, 'GA':0, 'GC':1, 'GG':0, 'GU':0, 'UA':1, 'UC':0, 'UG':0, 'UU':0}
	
	# Find number of perfect matches of the rna graph
	def perfectMatch(self, rna):
		self.u = 0
		self.g = 0
		for i in range(len(rna)):
			if rna[i] == "U":
				self.u += 1
			elif rna[i] == "G":
				self.g += 1
		self.perfectMatches = math.factorial(self.u)*math.factorial(self.g)

	# Find and cound the non-crossing perfect matches of the string
	def countRNA2Structures(self, seq):
		# if sequence not in dictionary
		if seq not in self.cache:
			# iterate over range by 2's as we don't want odd lengths
			tmp = []
			for k in range(1, len(seq), 2):
				''' Multiply first half of the string * the first nt and ending nt of first half
				* second half
				This multiplication is to combine the number of noncrossing
				perfect matches from the subproblems.
				The actual value/counts comes from the dynamically generated dictionary.
				'''
				tmp.append(countRNA2Structures(seq[1:k]) * self.cache[seq[0]+seq[k]] * countRNA2Structures(seq[k+1:]))
			# assign current sequence into dictionary for later use
			self.cache[seq] = sum(tmp)
		self.cache[seq]

	def kMerComposition(self, k):
		st = st.strip()
		strs = "ACGU"
		subs = product(strs, repeat = k)
		kmers = []
		for s in subs:
			kmers.append("".join(x for x in s))
		
		mat = []
		for km in (kmers):
			mat.append((len(re.findall("(?=" + km + ")" ,self.string))))
		return " ".join('%2d'%x for x in mat)

	def countBases(self):
	#begin search
		self.a = self.string.count('A')
		self.c = self.string.count('C')
		self.g = self.string.count('G')
		self.u = self.string.count('U')
		return self.a, self.c, self.g, self.u

	def maximumMatchings(r):
		A, C, G, U = r.countBases()
		AU = factorial(max(A, U)) / factorial(max(A, U) - min(A, U))
		GC = factorial(max(G, C)) / factorial(max(G, C) - min(G, C))
		self.maximumMatchings = (AU)*(GC)
		return (AU)*(GC)


class aminoAcid:
	
	def __init__(self, string):
		self.string = string
		self.rnaStrings = 0
		self.weight = 0

	def noOfRNAStrings(str):
		prob = 1
		for i in str:
			prob *= (aminoacids[i])
			prob = prob%1000000
		prob *= 3
		prob = prob % 1000000
		self.rnaStrings = prob

	def totalWeight(protein):
		for i in protein:
			self.weight += weights[i]
		
# Used to iterate over .FASTA files
def fastaIter(fasta_name):

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

def reverse(dna):
	dna = list(dna)
	return dna[::-1]

def complement(dna):
	dna = list(dna)
	complementString = []
	for i in range(len(dna)):
		if(dna[i]) == 'T':
			self.complementString.append('A')
		elif(dna[i]) == 'A':
			self.complementString.append('T')
		elif(dna[i]) == 'C':
			self.complementString.append('G')
		elif(dna[i]) == 'G':
			self.complementString.append('C')
	self.complementString =''.join(self.complementString)

def reverseComplement(self):
	self.reverseComplementString = []
	self.reverse()
	for i in range(len(self.reverseString)):
		if(self.reverseString[i]) == 'T':
			self.reverseComplementString.append('A')
		elif(self.reverseString[i]) == 'A':
			self.reverseComplementString.append('T')
		elif(self.reverseString[i]) == 'C':
			self.reverseComplementString.append('G')
		elif(self.reverseString[i]) == 'G':
			self.reverseComplementString.append('C')
	self.reverseComplementString =''.join(self.reverseComplementString)

## Probability Defining Functions ##

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

## COMPARING FUNCTIONS ##
# 1. Find Hamming Distance between 2 strings
# 2. Find the longest Common Substring of two strings
# 3. Find one substring of two strings s, t
# 4. Get ratio of transitions to transmutations
# 5. Find LCS
# 6. Find edit Distance between 2 strings

def hammingDistance(s1,s2):
    assert len(s1) == len(s2) #Must be of equal lengths
    return sum(c1 != c2 for c1, c2 in zip(s1, s2))

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

def oneSubstring(s, t):
	j = 0
	sub = []
	for i in range(len(t)):
		while(j < len(s)):
			if t[i] == s[j]:
				sub.append(j+1)
				j += 1
				break;
			j += 1
	return sub


def transRatio(s, t):
	transitions = 0
	transmutations = 0
	for i in range(len(s)):
		if(s[i]!=t[i]):
			if((s[i] in ["A", "G"] ) & (t[i] in ["A", "G"])):
				transitions += 1
			elif((s[i] in ["C", "T"] ) & (t[i] in ["C", "T"])):
				transitions += 1
			elif((s[i] in ["C", "T"] ) & (t[i] in ["A", "G"])):
				transmutations += 1
			elif((s[i] in ["A", "G"] ) & (t[i] in ["C", "T"])):
				transmutations += 1

	return float(transitions)/float(transmutations)

# Longest Common Subsequence
def lcs(s1, s2):
	l1 = len(s1)
	l2 = len(s2)
	matrix = [["" for x in range(l2)] for x in range(l1)]
	for i in range(l1):
		for j in range(l2):
			if s1[i] == s2[j]:
				if i == 0 or j == 0:
					matrix[i][j] = s1[i]
				else:
					matrix[i][j] = matrix[i-1][j-1] + s1[i]
			else:
				matrix[i][j] = max(matrix[i-1][j], matrix[i][j-1], key=len)
	cs = matrix[-1][-1]
	return cs

# Reverse String with the lowest number of permutations
def swap(lst, i, j):
    sublst = lst[i:j+1]
    sublst.reverse()
    lst = lst[:i] + sublst + lst[j+1:]
    return lst

def reversalDistance(s, t):
	queue = Queue.Queue()
	visited = set()

	queue.put((s,0))
	while not queue.empty():
		x,d = queue.get()
		visited.add(tuple(x))
		if x == t:
			return d
		for i in xrange(len(x)):
			for j in xrange(i+1, len(x)):
				tmp = swap(x[:], i, j)
				if tuple(tmp) not in visited:
					queue.put((tmp, d+1))


def editDistance(s, t, m, n): #m = len(s), n = len(t)
	
	if(m == 0):
		return n;

	if(n == 0):
		return m;

	if(s[m-1] == t[n-1]):
		return editDistance(s, t, m-1, n-1)

	return 1 + min( editDistance(s,t, m-1, n),
					editDistance(s,t, m, n-1),
					editDistance(s,t , m-1, n-1))


## GRAPH FUNCTIONS ##
# In this section are contained all the graph/traversal functions
# Create profile matrix of dna list
def profileMatrix(file):
	matrix = []
	seq  = fastaIter(file)
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

# Create concensus from the Matrix
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

# Create An overlap graph
def overlapGraph(file, o):
	suffixes = []
	prefixes = []
	seq_names = []
	seq  = fastaIter(file)
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

# Create all possible superstrings
def createSuperstrings(data, no):
	superstrings = []
	for i in range(len(data)):
		for j in range(len(data)):
			string = data[i]
			for z in range(int(no)-1):
				string = string+(data[j])
			superstrings.append(string)
	return superstrings

# Get the shortest Superstring of all possible ones
def shortestSuperstring(file):
	reads = []
	for i in fastaIter(file):
		reads.append(i[1])
	overlaps = []
	overlapping = []
	#find overlaps
	for i in range(len(reads)):
		curr_read = reads[i]
		for j in range(len(curr_read) // 2, len(curr_read)):
			curr_suffix = curr_read[-(j + 1):]
			for k in range(len(reads)):
				curr_comp = reads[k]
				for l in range(len(curr_comp) // 2, len(curr_comp)):
					curr_prefix = curr_comp[:l]
					if curr_suffix == curr_prefix:
						overlaps.append(k)
						overlapping.append([len(curr_suffix), i, k])

	s = set(overlaps)
	print overlapping
	first_read = ''
	count = len(overlapping)
	for m in range(len(overlapping)):
		suf_index = overlapping[m][1]
		if suf_index not in s:		   #find first read and initialise new str
			first_read = suf_index
			new_str = reads[overlapping[m][1]] + reads[overlapping[m][2]][
				overlapping[m][0]:]
			count -= 1
			pref_index = overlapping[m][2]
			while count > 0:					   #when the first read is found, add 
				for n in range(len(overlapping)):  #the remaining in the correct order
					if pref_index == overlapping[n][1]:
						new_str += reads[overlapping[n][2]][overlapping[n][0]:]
						pref_index = overlapping[n][2]
						count -= 1
	return(new_str)

def errorCorrection(reads):
	# First remove duplicates
	noOfShows = np.ones(len(reads))
	hammingsMat = []
	hammingsMatRC = []
	for i in range(len(reads)):
		hammings = np.zeros(len(reads))
		hammingsRC = np.zeros(len(reads))
		reads[i].reverseComplement()
		for j in range(len(reads)):
			reads[j].reverseComplement()
			hammings[j] = bio.hammingDistance(reads[i].string, reads[j].string)
			hammingsRC[j] = bio.hammingDistance(reads[i].string, reads[j].reverseComplementString)
			if(i!=j):
				if((reads[i].string == reads[j].string) | (reads[i].reverseComplementString == reads[j].string)):
					noOfShows[i] += 1

		hammingsMat.append(hammings)
		hammingsMatRC.append(hammingsRC)

	# Get indexes of wrongs
	wrongs = []
	for i in range(len(noOfShows)):
		if(noOfShows[i] == 1):
			wrongs.append(i)
	#print noOfShows
	for i in range(len(noOfShows)):
		if noOfShows[i] == 1:
			for h in range(len(hammingsMat)):
				if(h not in wrongs):
					if((hammingsMat[i][h] == 1)): # Check for correct reads only
						print str(reads[i].string) + "->" + str(reads[h].string)
						break;
					if((hammingsMatRC[i][h] == 1)):
						print str(reads[i].string) + "->" + str(reads[h].reverseComplementString)
						break;
						
# Get number of signed Permutations of a n length string
def checkDup(p):
	for obj in p:
		if -obj in p:
			return 0
	return 1

def signedPerm(n):
	orders = []
	for i in range(-n, n+1):
		if i != 0:
			orders.append(i)

	count = 0 
	for p in permutations(orders, r = n):
		if (0!=checkDup(p)):
			count+=1
			print " ".join('%2d'%x for x in p)

	print count

# Count number of minimum edges need to produce a tree

def minerv(file, n):
	with open(file) as f:
		content = f.readlines()
	print (n - (len(content)-1) - 1)

# Create an adjacency list from a file in the form of a dictionary

def createList(file):
	with open(file) as f:
		content = f.readlines()
	treeNodes = int((content[0].split())[0])
	adjList = { x : [] for x in range(1, (treeNodes)+1)}

	for i in range(1, len(content)):
		for s1 in content[i].split():
			for s2 in content[i].split():
				if s2!=s1:
					adjList[int(s1)].append(s2)
	return (adjList, treeNodes)

# Get all Strings from a Dictionary lexicographicaly
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

# Count number of subsets of n length set
def countSubsets(n):
	count = 1
	for i in range(1, n+1):
		count += factorial(n)/(factorial(i)*factorial(n-i))
	return count % 1000000

# Probability of creating random string from given gc content
def randomString(d, arr):
	table = []
	for p in arr:
		total_p = 0
		dic = {
			'A' : (1 - p)/2,
			'T' : (1 - p)/2,
			'G' : p/2,
			'C' : p/2
		}
		
		d.countBases()
		#total_p = p_g*d.g*p_t*d.t*p_c*d.c*p_a*d.a
		for i, a in enumerate(d.string):
			if(i == 0):
				total_p = dic[a]
			else:
				total_p *= dic[a]
		table.append(math.log10(total_p))
	return table