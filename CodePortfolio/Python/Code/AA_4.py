# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 07:23:10 2019
Program to find longest common subsequence(LCS)
@author: vishal_bhalla
"""

from time import time
import sys
sys.setrecursionlimit(5000)

def getLCS(X,Y):
    strtTime = time()
    m = len(X)
    n = len(Y)
    c = [[0 for x in range(n+1)] for x in range(m+1)]
    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0:
                c[i][j] = 0
            elif X[i-1] == Y[j-1]: 
                c[i][j] = c[i-1][j-1] + 1
            else: 
                c[i][j] = max(c[i-1][j], c[i][j-1])
    idx = c[m][n]
    printlcs = [""] * (idx+1)
    a = m 
    b = n 
    while a > 0 and b > 0:
        # If current val in X[] and Y[] are same, then it is part of LCS 
        if X[a-1] == Y[b-1]: 
            printlcs[idx-1] = X[a-1] 
            a-=1
            b-=1
            idx-=1
        elif c[a-1][b] > c[a][b-1]: 
            a-=1
        else: 
            b-=1
    
    endTime = time()
    return endTime - strtTime,printlcs
    

def main():
    #print(u'\u2196')
    print("This program is to find the Longest Common Substring(LCS)")
    #X = ('A','B','C','B','D','A','B')
    #Y = ('B','D','C','A','B','A')
    X = ('1','0','0','1','0','1','0','1')
    Y = ('0','1','0','1','1','0','1','1','0')
    timing,lcs = getLCS(X,Y)
    print ("LCS between ", X , " and " , Y,  " is:\n " + "".join(lcs))
    print("Time Taken: ",timing) 
            
            
main()
