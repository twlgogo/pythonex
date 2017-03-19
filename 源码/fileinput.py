import fileinput 

def process(string):
	print("Processing: ",string)

f = open(r"123.txt")	
for line in f:
	process(line)
	

f.close()	