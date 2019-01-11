def findSubstring(s1,s2):
	pos = [] 
	for i in range(len(s1)):
		if(s1[i:i+len(s2)]==s2):
			pos.append(i+1)
	return pos

with open('dataset','r') as f:
    dna = f.readlines()
    for i in range(1,len(dna),2):
    	s1 = dna[i].strip()
    	s2 = dna[i+1].strip()
    	pos = findSubstring(s1,s2)
    	print(' '.join(str(x) for x in pos))

