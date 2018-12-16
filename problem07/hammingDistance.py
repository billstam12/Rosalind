def hammingDistance(s1,s2):
    assert len(s1) == len(s2) #Must be of equal lengths
    return sum(c1 != c2 for c1, c2 in zip(s1, s2))


with open('rosalind_dna.txt','r') as f:
    dna = f.readlines()
    dna = [x.strip() for x in dna]

print(hammingDistance(dna[0],dna[1]))
