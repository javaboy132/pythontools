######################
# (c) 2017 Alex Coad
# GPLv3
# A basic program that reads source code files and makes a TODO.filename.txt file, containing line numbers and TODO: messages from the source code files
import sys,getopt

filename=""
helptext="todoreader.py -f <inputfilename>"
try:
    opts,args=getopt.getopt(sys.argv[1:],"hf:",["file="])
except getopt.GetoptError:
    print(helptext)
    sys.exit(2)
for opt,arg in opts:
    if opt=='-h':
        print(helptext)
        sys.exit()
    elif opt in ("-f","--file"):
        filename=arg

fp=open(filename,'r')
op=open("TODO."+filename+".txt",'w')
linenum=0
for line in fp:
    linenum=linenum+1
    if 'TODO:' in line:
        op.write("line: "+str(linenum)+": "+line)

fp.close()
op.close()
