def problem3_1(txtfilename):
    s=-1
    f=open(txtfilename)
    for line in f:
        print(line,end="")
        s=s+len(line)
    print("\nThere are", s,"letters in the file.")
    f.close()
