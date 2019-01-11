aa_nums = {
	"F" : 2,
	"L" : 6,	
	"S" : 6,
	"Y" : 2,
	"Stop" : 3,
	"C" : 2,
	"W" : 1,
	"P" : 4,
	"H" : 2,
	"Q" : 2,
	"R" : 6,
	"I" : 3,
	"M" : 1,
	"T" : 4,
	"N" : 2,
	"K" : 2,
	"V" : 4,
	"A" : 4,
	"D" : 2,
	"E" : 2,
	"G" : 4
}


def noOfRNAStrings(str):
	prob = 1
	for i in str:
		prob *= (aa_nums[i])
		prob = prob%1000000
	prob *= 3
	prob = prob % 1000000
	return prob
mrna = open('dataset.tx', 'r').read().strip()
print noOfRNAStrings(mrna)

