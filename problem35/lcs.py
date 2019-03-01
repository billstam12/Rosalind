import imp
bio = imp.load_source('bioLibrary', '/home/bill/Documents/ML_Projects/Rosalind/bioLibrary.py')

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

strs = []
for d in bio.fastaIter("dataset.txt"):
	strs.append(d[1])

print lcs(strs[0],strs[1])