def dnaToRna(dna):
	dna = list(dna)
	rna = map(lambda s: s.replace('T' , 'U'), dna)
	rna = ''.join(rna)
	return rna



# open file
dna = open('dna.txt', 'r').read()
rna =  dnaToRna(dna)
print rna