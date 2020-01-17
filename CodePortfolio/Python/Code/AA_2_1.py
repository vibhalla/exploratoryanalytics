# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 06:34:59 2019
Applied Algorithms - Written Assignment #2
@author: vishal_bhalla
"""

import numpy as np
from time import time
import matplotlib.pyplot  as plt


def brutCalc(A):
    #This function will sort the data in the array passed as the argument.
    dlen = len(A)
    startPos = endPos = 0
    maxSum = 0
    strtTime = time()
    for i in range(0,dlen,1):
        subSum = 0
        for j in range(i,dlen,1):
            subSum = subSum + A[j]
            if subSum > maxSum:
                maxSum=subSum
                startPos = i
                endPos = j
    endTime = time()
    print(" Max SubArray: A[",startPos,"..",endPos,"]\n","Max Sum:",maxSum)
    return endTime - strtTime
    
def main():
    print("This program is a demo for brute force method of computing the largest subarray")
    runStat = []
    # Read the file in steps of 5000
    for j in range(5000,100001,5000):
        inpFile = open("../Data/input-programming-2.txt", "r")
        data = []
        for i in range(j):
            data.append(int(inpFile.readline().strip()))
        # Call the brutCalc function of array 3 times for each data size
        calcTime = 0
        for itratn in range(3):
            calcTime = calcTime + brutCalc(data)
        runStat.append([j,round(calcTime/3,5)])
        inpFile.close()
    #runStat = np.array(runStat)
    print(runStat)
    plt.xlim([5000,100000])
    plt.ylim([0,750])
    plt.scatter(*zip(*runStat))
    plt.show()
 
            
            
main()
