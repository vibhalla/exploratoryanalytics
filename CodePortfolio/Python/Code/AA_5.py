# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 08:09:39 2019
Program to design Huffman Code for a given text. Sample text is the book 
Study In Scarlet By Sir Arthur Conan Doyle
Ref: https://rosettacode.org/wiki/Huffman_coding#Python
@author: vishal_bhalla
"""

import collections
from heapq import heappush, heappop, heapify

def createDict(data):
    #This function will create a frequency dictionary of characters.
    charFreq = {}
    count = 0
    for ch in data:
        count += 1
        if not ch in charFreq:
            charFreq[ch] = 0
        charFreq[ch] += 1
    return charFreq, count

def getCode(freq):
    # Create Heap, Heapify, Merge lowest 2 frequencies, add code bit and 
    # push it back to the heap
    tempHeap = [[cnt, [ch, ""]] for ch, cnt in freq.items()]
    heapify(tempHeap)
    while len(tempHeap) > 1:
        min1 = heappop(tempHeap)
        min2 = heappop(tempHeap)
        for leafWt in min1[1:]:
            leafWt[1] = '0' + leafWt[1]
        for leafWt in min2[1:]:
            leafWt[1] = '1' + leafWt[1]
        heappush(tempHeap,[min1[0] + min2[0]] + min1[1:] + min2[1:])
    return tempHeap


    
def main():
    print("\n This program is a demo for designing Huffman Code\n")
    # Read the file 
    inpFile = open("../Data/StudyInScarlet.txt", "r")
    data = (inpFile.read().strip())
    inpFile.close()
    #data = "This program is a demo for designing Huffman Code"
    frequency, charCount = createDict(data)
    print("Total Characters:",charCount,"\n")
    print("Number of Characters:", len(frequency), "\n")
    bits = charCount*6
    code = getCode(frequency)
    code = sorted(heappop(code)[1:], key=lambda x: (len(x[-1]), x))
    totalBits = 0
    print("\n Frequency and Code\n")
    for ch in code:
        print(ch[0],"--", frequency[ch[0]]," -- ", ch[1])
        totalBits += frequency[ch[0]]*len(ch[1])
    print("\nTotal Space needed without Huffman Code: ", bits)
    print("Total Space needed with Huffman Code: ", totalBits)
    print("Compression %: " , round((((bits - totalBits)/bits)*100),2))
    
    
main()
