import sys
filename = sys.argv[1]
filename1 = sys.argv[2]
infile=open(filename)
outfile=open(filename1,'w')
for line in infile:
	line=line.strip("\n")
	outfile.write(str(len(line))+"\n")
infile.close()
outfile.close()
