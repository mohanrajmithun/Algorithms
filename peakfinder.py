problemMatrix = [
	[ 4,  5,  6,  7,  8,  7,  6,  5,  4,  3,  2],
	[ 5,  6,  7,  8,  9,  8,  7,  6,  5,  4,  3],
	[ 6,  7,  8,  9, 10,  9,  8,  7,  6,  5,  4],
	[ 7,  8,  9, 10, 11, 10,  9,  8,  7,  6,  5],
	[ 8,  9, 10, 6, 10, 10, 9,  9,  8,  7,  6],
	[ 7,  8,  14, 13, 12, 10,  12,  8,  7,  6,  5],
	[ 6,  7,  15,  9, 10,  9,  8,  7,  6,  5,  4],
	[ 5,  6,  7,  8,  9,  8,  7,  6,  5,  4,  3],
	[ 4,  5,  6,  7,  8,  7,  6,  5,  4,  3,  2],
	[ 3,  4,  5,  6,  7,  6,  5,  4,  3,  2,  1],
	[ 2,  3,  4,  5,  6,  5,  4,  3,  2,  1,  0]
]

import numpy as np

problemMatrix = np.array(problemMatrix)
# print(np.shape(problemMatrix))

midrow,midcol= np.shape(problemMatrix)
midcol=midcol//2

def peakfinder(problemMatrix):
    i=0
    midrow, midcol = np.shape(problemMatrix)
    if midcol <=2 :
        print("two col mat")
        midcol= 0
        col = problemMatrix[:, midcol]
        maxv = np.argmax(col)
        if problemMatrix[maxv,midcol+1]> problemMatrix[maxv,midcol]:
            col = problemMatrix[:, midcol+1]
            maxv = np.argmax(col)
            print(maxv)
            return problemMatrix[maxv,midcol+1],maxv,midcol+1
        return problemMatrix[maxv,midcol],maxv,midcol

    midcol = midcol // 2

    col=problemMatrix[:,midcol]
    maxv=np.argmax(col)
    if problemMatrix[maxv,midcol-1]>col[maxv]:
        print("left side")
        #print("truleft",problemMatrix[maxv,midcol-1],col[maxv])
        betneighrow,betneighcol=maxv,(midcol)
        subprobmatr=problemMatrix[:,0:betneighcol+1]
        #print(subprobmatr)
    if problemMatrix[maxv,midcol+1]>col[maxv]:
        print("right side")
        #print("truright",problemMatrix[maxv,midcol+1],col[maxv])
        betneighrow, betneighcol = maxv, (midcol+1)
        subprobmatr = problemMatrix[:,betneighcol:]
        #print(subprobmatr)
    if problemMatrix[maxv,midcol-1]<=col[maxv] and problemMatrix[maxv,midcol+1]<=col[maxv]:
        print("peak col",midcol,maxv)
        #print("peak",problemMatrix[maxv,midcol-1]>col[maxv],maxv,midcol,"location")
        if i==0:
            print("peak",problemMatrix[maxv,midcol],"row",maxv,"colom",midcol)
        return problemMatrix[maxv,midcol-1],maxv,midcol

    peakvalue,peakrow,peakcol= peakfinder(subprobmatr)
    print(peakvalue,"row",peakrow,"col",peakcol)








peakfinder(problemMatrix)