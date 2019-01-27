from bioLibrary import *

strs = []
for i in fastaIter("dataset.txt"):
	strs.append(i[1])

def merge(s1, s2, str):
	if s2 in s1:
		return s1
	else:
		longest_sub = s2[(s2.rfind(str)+len(str)):]
		return s1 + longest_sub


all_cands = []
for i in range(len(strs)):
	candidate = strs[i]
	for j in range(len(strs)):
		if(i!=j):
			temp_2 = strs[j]
			while(1):
				longest_sub = ""
				if(temp_2 in candidate):
					candidate = merge(candidate, strs[j], temp_2)
					break;
				else:
					temp_2 = temp_2[:-1]
					
			# get the one with the most letters
	all_cands.append(candidate)
print min(all_cands, key=len) # prints "i"
#MAYBE set as candidate_0 the shortest string in the list
#Deterministic way

