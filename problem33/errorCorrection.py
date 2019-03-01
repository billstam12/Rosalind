import imp
bio = imp.load_source('bioLibrary', '/home/bill/Documents/ML_Projects/Rosalind/bioLibrary.py')
import numpy as np

def errorCorrection(reads):
	# First remove duplicates
	noOfShows = np.ones(len(reads))
	hammingsMat = []
	hammingsMatRC = []
	for i in range(len(reads)):
		hammings = np.zeros(len(reads))
		hammingsRC = np.zeros(len(reads))
		reads[i].reverseComplement()
		for j in range(len(reads)):
			reads[j].reverseComplement()
			hammings[j] = bio.hammingDistance(reads[i].string, reads[j].string)
			hammingsRC[j] = bio.hammingDistance(reads[i].string, reads[j].reverseComplementString)
			if(i!=j):
				if((reads[i].string == reads[j].string) | (reads[i].reverseComplementString == reads[j].string)):
					noOfShows[i] += 1

		hammingsMat.append(hammings)
		hammingsMatRC.append(hammingsRC)

	# Get indexes of wrongs
	wrongs = []
	for i in range(len(noOfShows)):
		if(noOfShows[i] == 1):
			wrongs.append(i)
	#print noOfShows
	for i in range(len(noOfShows)):
		if noOfShows[i] == 1:
			for h in range(len(hammingsMat)):
				if(h not in wrongs):
					if((hammingsMat[i][h] == 1)): # Check for correct reads only
						print str(reads[i].string) + "->" + str(reads[h].string)
						break;
					if((hammingsMatRC[i][h] == 1)):
						print str(reads[i].string) + "->" + str(reads[h].reverseComplementString)
						break;
	
	
reads = []
for i in bio.fastaIter("dataset.txt"):
	reads.append(bio.dna(i[1]))

errorCorrection(reads)