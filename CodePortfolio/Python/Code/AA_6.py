# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 06:01:26 2019
This program checks if the input graph is bipartite or not
@author: vishal_bhalla
"""
import sys
import ast
sys.setrecursionlimit(5000)


def createAdjList(n,edges):
    adjList = {}
    for e in edges:
        adjList.setdefault(e[0],[]).append(e[1])
        adjList.setdefault(e[1],[]).append(e[0])
    return adjList
    


def chkBipartite(adjList, vrtx):
    clr = {vrtx: 0}
    visited = [vrtx]
    stckNode = []
    stckNode.append(vrtx)
    s1 = set()
    s2 = set()
    while stckNode:
        vrtx = stckNode[-1]
        new_clr = 1 - clr[vrtx]
        if vrtx not in visited:
            visited.append(vrtx)
        stckNode_pop = True
        for next in adjList[vrtx]:
            if next not in visited:
                stckNode.append(next)
                clr[next] = new_clr
                stckNode_pop = False
            else:
                if clr[next] != new_clr:
                    return False, None, None
        if stckNode_pop:
            stckNode.pop()
    print("\nVisited Nodes: " , visited)
    for key, val in clr.items():
        if val == 0:
            s1.add(key)
        else:
            s2.add(key)
    return True,s1,s2

def main():
    print("\nThis program is to check if the input graph is bipartite\n")
    edges = []
    # Read the file
    with open("../Data/bipartite.txt" , 'r') as f:
        n = int(f.readline())
        for line in f:
            edges.append(line.rstrip())
    edge = [ast.literal_eval(edVal.strip()) for edVal in edges]
    adjList = createAdjList(n,edge)
    print("Adjacency List: ",adjList)
    check,s1,s2 = chkBipartite(adjList,1)
    if check:
        print("\nThis graph is Bipartite")
        print("\nSet 1:", s1, "\nSet 2:", s2)
    else:
        print("\nThe graph is not Bipartite")
    
           
            
main()


