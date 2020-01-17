# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 23:03:56 2019
This program is to observe the performance of bubble sort with change in inpu data size.
@author: vishal_bhalla
"""
import numpy as np
from time import time
import matplotlib.pyplot  as plt


def bblSort(unsrt):
    #This function will sort the data in the array passed as the argument.
    dlen = len(unsrt)
    strtTime = time()
    for x in range(dlen - 1):
        for y in range(dlen - 1,x,-1):
            if unsrt[y] < unsrt[y - 1]:
                a = unsrt[y]
                unsrt[y] = unsrt[y - 1]
                unsrt[y - 1] = a
    endTime = time()
    return endTime - strtTime
    
def main():
    
    runStat = []
    # Read the file in steps of 500
    for j in range(500,10001,500):
        inpFile = open("../Data/input-programming-1.txt", "r")
        data = []
        for i in range(j):
            data.append(int(inpFile.readline().strip()))
        # Call the sort function of array 3 times for each data size
        sortTime = 0
        for itratn in range(3):
            sortTime = sortTime + bblSort(data)
        runStat.append([j,round(sortTime/3,5)])
        inpFile.close()
    #runStat = np.array(runStat)
    print(runStat)
    plt.xlim([500,10000])
    plt.ylim([0,15])
    plt.scatter(*zip(*runStat))
    plt.show()
 
            
            
main()
