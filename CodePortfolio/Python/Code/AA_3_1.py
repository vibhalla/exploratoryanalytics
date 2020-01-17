# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 21:48:14 2019
This program demoes Merge Sort
@author: vishal_bhalla
"""


from time import time
import matplotlib.pyplot  as plt
import sys
sys.setrecursionlimit(5000)

def getSorted(data):
    #print("Unsorted : \n", data)
    strtTime = time()
    mergeSort(data)
    endTime = time()
   # print("Sorted : \n", sortedData)
    return endTime - strtTime
    
def mergeSort(A):
    if len(A) < 2:
        return A
    else:
        mid = ((len(A))//2)
        left = mergeSort(A[:mid])
        right = mergeSort(A[mid:])
        sortedArray = merge(left,right)
        return sortedArray
    
def merge(left,right):
    i = 0
    j = 0
    sortedArray = []
    ll = len(left)
    rl = len(right)
    while i < ll and j < rl:
        if left[i] > right[j]:
            sortedArray.append(right[j])
            j += 1
        else:
            sortedArray.append(left[i])
            i += 1
    while i < ll:
            sortedArray.append(left[i])
            i += 1
    while j < rl:
            sortedArray.append(right[j])
            j += 1
    return sortedArray

def main():
    print("This program is to implement Merge Sort algorithm")
    runStat = []
    # Read the file in steps of 5000
    for j in range(5000,100001,5000):
        inpFile = open("../Data/input-programming-3.txt", "r")
        data = []
        for i in range(j):
            data.append(int(inpFile.readline().strip()))
        # Call the recurCalc function of array 3 times for each data size
        calcTime = 0
        for itratn in range(3):
            calcTime = calcTime + getSorted(data)
        runStat.append([j,round(calcTime/3,5)])
        inpFile.close()
    #runStat = np.array(runStat)
    print(runStat)
    plt.xlim([5000,100000])
    plt.ylim([0,1])
    plt.scatter(*zip(*runStat))
    plt.show()
 
            
            
main()
