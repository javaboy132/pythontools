###################
# (c)2017 Alex Coad
# GPLv3
#
# This is a little command line tool that computes pi using the wallis equation

import sys,getopt

def main(argv):
    numiterations=3
    helptext='pi.py -n <iterations>'
    try:
        opts, args=getopt.getopt(argv,"hn:",["numiterations="])
    except getopt.GetoptError:
        print(helptext)
        sys.exit(2)
    for opt, arg in opts:
        if opt=='-h':
            print(helptext)
            sys.exit()
        elif opt in ("-n","--numiterations"):
            numiterations=arg

    pi=2
    for i in range(arg):
        pi=pi*((4*(i+1)**2)/(4*(i+1)**2-1))

    print(pi)

if __name__=="__main__":
    main(sys.argv[1:])
