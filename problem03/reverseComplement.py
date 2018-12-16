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

dna = open('rosalind_revc.txt', 'r').read()
reverse = reverse(dna)
print reverse
complement =  complement(reverse)
print complement