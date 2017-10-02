counter = 0

with open('Crime.csv') as myfile:
   for line in myfile:
       finded = line.find('ASSAULT')
       if finded != -1 and finded != 0:
	 counter += 1
print counter
