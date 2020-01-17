# -*- coding: utf-8 -*-
"""
Created on Sun Oct  6 08:02:16 2019

@author: vishal_bhalla
"""


from time import time
import random
import matplotlib.pyplot  as plt
import sys
sys.setrecursionlimit(5000)

def getElement(data,i):
    #print("Unsorted : \n", data)   
    strtTime = time()
    iVal = findVal(data,i)
    endTime = time()
    return endTime - strtTime

def getChunk(A):
    for i in range(0, len(A), 5):  
        yield A[i:i + 5]
        
def getMedian(A):
    x = len(A)
    for y in range(1,x,1):
        key = A[y]
        z = y - 1
        while z >= 0 and A[z] > key:
            A[z + 1] = A[z]
            z = z - 1
        A[z + 1] = key
    return A[(x//2)]

def select(lst,p,r,i):
    if p == r:
        return lst[p]
    q = partition(lst,p,r)
    k = q - p + 1
    if k == i:
        return lst[q]
    elif i < k:
        return select(lst,p,q - 1, i)
    else:
        return select(lst,q + 1, r, i - k)
    
def partition(A,p,r):
    x = A[r]
    i = p - 1
    for j in range(p,r-1,1):
        if A[j] <= x:
            i = i + 1
            z = A[i]
            A[i] = A[j]
            A[j] = z
    A[r] = A[i + 1]
    A[i + 1] = x
    return i + 1


def modPart(A,mm,i):
    x = mm
    p = 0
    r = len(A)
    i = p - 1
    for j in range(p,r-1,1):
        if A[j] <= x:
            i = i + 1
            z = A[i]
            A[i] = A[j]
            A[j] = z
    A[r -1] = A[i + 1]
    A[i + 1] = x
    return i + 1

def findVal(A,i):
    listMedian = []
    if len(A) < 2:
        return A
    else:
        # break the list into chunks of 5
        medList = list(getChunk(A))
        #print(len(medList),"\n",medList[0],"\n",medList[1])
        # Get the number of sublists created and iterate to get the medians for each chunk
        j = len(medList)
        for k in range(j):
            listMedian.append(getMedian(medList[k]))
    mstrMedian = select(listMedian,0,j-1,j//2)
    indX = modPart(A,mstrMedian,i)
    return A[indX]
    

def main():
    print("This program is to find the ith value")
    runStat = []
    # Read the file in steps of 5000
    for j in range(5000,100001,5000):
        inpFile = open("../Data/input-programming-3.txt", "r")
        data = []
        for i in range(j):
            data.append(int(inpFile.readline().strip()))
        # Call the recurCalc function of array 3 times for each data size
        calcTime = 0
        n = len(data)
        for itratn in range(3):
            # Get the i value at random
            i = random.randint(0,n-1)
            calcTime = calcTime + getElement(data,i)
        runStat.append([j,round(calcTime/3,5)])
        inpFile.close()
    #runStat = np.array(runStat)
    print(runStat)
    plt.xlim([5000,100000])
    plt.ylim([0,.1])
    plt.scatter(*zip(*runStat))
    plt.show()
 
            
            
main()
