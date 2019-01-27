from bioLibrary import *

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

p = []
for s in fastaIter("dataset.txt"):
	p.append(s)

sub = transRatio(p[0][1], p[1][1])
print sub