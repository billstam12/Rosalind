from bioLibrary import *
import urllib
from bs4 import BeautifulSoup
import re

def proteinMotif(ids, motif):
	urls = ["https://www.uniprot.org/uniprot/" + i + ".fasta" for i in ids]
	objects = []
	for url in urls:
		html = urllib.urlopen(url).read()
		soup = BeautifulSoup(html)

		# kill all script and style elements
		for script in soup(["script", "style"]):
		    script.extract()    # rip it out

		# get text
		text = soup.get_text()
		text = text.split("\n",1)
		text1 = text[1].replace('\r', '').replace('\n', '')

		positions = []
		for m in re.finditer(motif, text1):              
			positions.append(m.start() + 1)     

		id =  (text[0].split('|',2)[1]).strip()
		objects.append((id,positions))
	return objects

def parseMotif(motif): 
	#Convert motif to regex
	motif = motif.replace('{','[^')
	motif = motif.replace('}',']')
	motif = "(?=(" + (motif) + "))"
	motifs =  re.compile(motif)
	return motifs

fh = open("dataset.txt")
motif = "N{P}[ST]{P}"
motif = parseMotif(motif)
ids = fh.readlines()
ids = [x.strip() for x in ids]
objects = proteinMotif(ids, motif)

for o in objects:
	if (len(o[1])!=0):
		print o[0]
		print(' '.join(str(x) for x in o[1]))

