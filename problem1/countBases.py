def countBases(dna):
#begin search
    a = dna.count('A')
    c = dna.count('C')
    g = dna.count('G')
    t = dna.count('T')

    return (a,c,g,t)

# open file
dna = open('rosalind_dna.txt', 'r').read()
a, c ,g, t = countBases(dna)
print a, c, g, t