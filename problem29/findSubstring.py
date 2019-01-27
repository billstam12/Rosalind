from bioLibrary import *

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
p = []
for s in fastaIter("dataset.txt"):
	p.append(s)

sub = oneSubstring(p[0][1], p[1][1])
print " ".join('%2d'%x for x in sub)