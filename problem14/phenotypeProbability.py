def phenoProb(i1,i2,i3,i4,i5,i6):
	return (((i1 + i2 + i3 + 0.75*i4 + 0.5*i5 )/5)*10)
#AA-AA 1
#AA-Aa 1
#AA-aa 1
#Aa-Aa 0.75
#Aa-aa 0.5
#aa-aa 0

print phenoProb(18811, 17589, 18888, 19868, 16089, 16757)