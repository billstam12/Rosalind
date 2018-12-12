from itertools import groupby
from collections import Counter

def fastaIter(fasta_name):
	"""
	modified from Brent Pedersen
	Correct Way To Parse A Fasta File In Python
	given a fasta file. yield tuples of header, sequence
	"""
	"first open the file outside "
	fh = open(fasta_name)

	# ditch the boolean (x[0]) and just keep the header or sequence since
	# we know they alternate.
	faiter = (x[1] for x in groupby(fh, lambda line: line[0] == ">"))

	for header in faiter:
		# drop the ">"
		headerStr = header.__next__()[1:].strip()

		# join all sequence lines to one.
		seq = "".join(s.strip() for s in faiter.__next__())

		yield (headerStr, seq)


def countGC(seq):
	counts = Counter(seq[1])
	return ((counts['G'] + counts['C'])/(counts['G'] + counts['C'] + counts['A'] + counts['T']))

seq = fastaIter("sequence.FASTA")
max = 0
max_id = "1"
for s in seq:
	gc_per = countGC(s)
	print (gc_per*100)
	if(gc_per > max):
		max = gc_per
		max_id = s[0]
print(max_id)