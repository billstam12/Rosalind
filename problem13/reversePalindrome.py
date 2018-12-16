from bioLibrary import *

# return substrings of length k to l
def getAllSubstrings(string, k):
    length = len(string)
    for i in xrange(length):
        for j in xrange(i + k, length+1 ):
            	yield((string[i:j], i)) #yield string and index
            
l = 12
seq = fastaIter("dna.FASTA")
for s in seq:
	for (substring, i) in (getAllSubstrings(s[1],4)):
		if(len(substring) <= l):
			rev = reverse(substring)
			comp = complement(rev)
			if(substring == comp):
				print (i+1), len(substring)