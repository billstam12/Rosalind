
def minerv(file, n):
	with open(file) as f:
		content = f.readlines()
	print (n - (len(content)-1) - 1)

def createList(file):
	with open(file) as f:
		content = f.readlines()
	treeNodes = int((content[0].split())[0])
	adjList = { x : [] for x in range(1, (treeNodes)+1)}

	for i in range(1, len(content)):
		for s1 in content[i].split():
			for s2 in content[i].split():
				if s2!=s1:
					adjList[int(s1)].append(s2)
	return (adjList, treeNodes)

adjList, n = createList("dataset.txt")
minerv("dataset.txt",n)


