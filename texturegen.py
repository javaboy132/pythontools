###################
# (c) 2017 Alex Coad
# GPLv3
# A basic black and white python texture generator
import numpy as np
import sys,getopt
import random
import matplotlib.pyplot as plt
from scipy import signal
from scipy import misc

n=100
b=0
show=True
outfile='out.png'
x=np.random.normal(0,1,n)
y=np.random.normal(0,1,n)
helptext='texturegen.py -o <outputfilename> -n <numiterations> -m <generationmode> -b <blur level>'

try:
    opts,args=getopt.getopt(sys.argv[1:],"hn:m:b:o:",["num=","mode=","blur=","out=","noshow"])
except getopt.GetoptError:
    print(helptext)
    sys.exit(2)
for opt,arg in opts:
    if opt=='-h':
        print(helptext)
        sys.exit()
    elif opt in ("-n","--num"):
        n=arg
    elif opt in ("-o","--out"):
        outfile=arg
    elif opt in ("--noshow"):
        show=False
    elif opt in ("-m","--mode"):
        if arg=='plaid':
            x=np.random.normal(0,1,n)
            y=np.random.normal(0,1,n)
        elif arg=='thing1':
            x=np.random.normal(0.8,2,n)
            y=np.random.normal(0.7,2,n)
        elif arg=='rand1':
            x=np.random.normal(np.random.rand(),np.random.rand(),n)
            y=np.random.normal(np.random.rand(),np.random.rand(),n)
        elif arg=='rand2':
            x=np.random.normal(np.random.rand(),np.random.rand(),n)
            y=np.random.normal(np.random.rand(),np.random.rand(),n)
            np.random.shuffle(x)
            np.random.shuffle(y)
        elif arg=='rand3':
            x=np.random.normal(random.random(),random.random(),n)
            y=np.random.normal(random.random(),random.random(),n)
        else:
            x=np.linspace(0,4,n)
            y=np.linspace(0,3,n)
    elif opt in ("-b","--blur"):
        b=arg

def f(x,y):
    return (1-x/2+x**5+y**3)*np.exp(-x**2-y**2)

#x=np.linspace(-2,3,4*n)
#y=np.linspace(-3,3,3*n)
k = np.array([[1,1,1],[1,1,0],[1,0,0]])
#x=ndimage.convolve(x,k,mode='constant',cval=0.0)
#y=ndimage.convolve(y,k,mode='constant',cval=0.0)
X,Y=np.meshgrid(x,y)
Z=f(X,Y)
for i in range(int(b)):
    Z=signal.convolve2d(Z,k,mode='full',boundary='wrap')

if show:
    plt.imshow(Z)
    plt.show()

misc.imsave(outfile,Z)
