import numpy as np


def createSuperstrings(data, no):
	superstrings = []
	for i in range(len(data)):
		for j in range(len(data)):
			string = data[i]
			for z in range(int(no)-1):
				string = string+(data[j])
			superstrings.append(string)
	return superstrings

# Create list of words
f = open("dataset.txt", "r")
data = f.readline().split()
no = f.readline()
# Now pass the list and the number to the superstring creator

superstrings  = createSuperstrings(data,no)

sorted_sups =  np.sort(superstrings)
print '\n'.join(map(str, sorted_sups))

