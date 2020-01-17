# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 23:31:37 2019
Applied Algorithms - Written Assignment #2 - Recursion
@author: vishal_bhalla
"""

from time import time
import matplotlib.pyplot  as plt
import sys
sys.setrecursionlimit(5000)

def recurCalc(data):
    dlen = len(data)
    maxSum = 0
    strtTime = time()
    li,hi,maxSum = getSub(data,0,dlen-1)
    endTime = time()
    print(" Max SubArray: A[",li,"..",hi,"]\n","Max Sum:",maxSum)
    return endTime - strtTime
    
def getSub(A,low,high):
    if low == high:
        return low, high, A[low]
    else:
        mid = ((high + low)//2)
        ll,lh,ls = getSub(A,low,mid)
        rl,rh,rs = getSub(A,mid + 1,high)
        cl,ch,cs = getCrossSub(A,low,mid,high)
        if(ls >= rs and ls >= cs):
            return ll,lh,ls
        elif(rs >= ls and rs >= cs):
            return rl,rh,rs
        else:
            return cl,ch,cs
        
    
def getCrossSub(A,low,mid,high):
    leftSum = rightSum = float('-inf')
    leftInd = low
    rightInd = high
    subSum = 0
    for i in range(mid,low,-1):
        subSum = subSum + A[i]
        if subSum > leftSum:
            leftSum=subSum
            leftInd = i
    subSum = 0
    for j in range(mid+1,high,1):
        subSum = subSum + A[j]
        if subSum > rightSum:
            rightSum=subSum
            rightInd = j
    return leftInd,rightInd,leftSum + rightSum
    
def main():
    print("This program is a demo for recursive method of computing the largest subarray")
    runStat = []
    # Read the file in steps of 5000
    for j in range(5000,100001,5000):
        inpFile = open("../Data/input-programming-2.txt", "r")
        data = []
        for i in range(j):
            data.append(int(inpFile.readline().strip()))
        # Call the recurCalc function of array 3 times for each data size
        calcTime = 0
        for itratn in range(3):
            calcTime = calcTime + recurCalc(data)
        runStat.append([j,round(calcTime/3,5)])
        inpFile.close()
    #runStat = np.array(runStat)
    print(runStat)
    plt.xlim([5000,100000])
    plt.ylim([0,.4])
    plt.scatter(*zip(*runStat))
    plt.show()
 
            
            
main()
