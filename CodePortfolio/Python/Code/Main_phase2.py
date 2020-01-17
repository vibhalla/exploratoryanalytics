
"""
Created on Thu Jul 18 06:58:14 2019
Final Project Phase 2
Analysis of available Breast Cancer data
@author: vishal_bhalla
"""

import pandas as pd
import numpy as np
import random
from random import choice, randint

"""
Data Structure
Scn 		Sample code number 	id 			number 
A2 		Clump Thickness 				   1 - 10 
A3 		Uniformity of Cell Size 		1 - 10 
A4 		Uniformity of Cell Shape 		1 - 10 
A5 		Marginal Adhesion 				1 - 10 
A6 		Single Epithelial Cell Size  1 - 10 
A7 		Bare Nuclei 					   1 - 10 
A8 		Bland Chromatin 				   1 - 10 
A9 		Normal Nucleoli 				   1 - 10 
A10 	Mitoses 						   1 - 10 
Class 	2 for benign, 4 for malignant 	2 or 4 
"""

def getCentroid(cData,init):
    cent = []
    if(init):
        c1 = cData.loc[random.choice([randint(1,len(cData) -1)]),"A2":"A10"].tolist()
        c2 = cData.loc[random.choice([randint(1,len(cData) -1)]),"A2":"A10"].tolist()
        cent.append(c1)
        cent.append(c2)
    else:
        #print(cData.head())
        c1 = cData.loc[(cData['P_Class']==2),"A2":"A10"].mean().tolist()
        c2 = cData.loc[(cData['P_Class']==4),"A2":"A10"].mean().tolist()
        cent.append(c1)
        cent.append(c2)
    return cent
    
def predClass(data_point,centroid):
    dist0 = np.sqrt(np.sum((data_point - centroid[0])**2))
    dist1 = np.sqrt(np.sum((data_point - centroid[1])**2))
    #print("\tdist0:",dist0,"\tdist1",dist1)
    if dist0 > dist1:
        P_Class = 2
    else:
        P_Class = 4
    return P_Class
       
        
def runCondition(numIter,oldCent,newCent):
    if numIter > 50:
        return True
    return oldCent == newCent
    
       
def getClusterInfo(data):
    cData = data.copy()
    numIter = 1
    oldCent = None
    cData['P_Class'] = 0
    newCent = getCentroid(cData,init=True)
    while not runCondition(numIter,oldCent,newCent):
        oldCent = newCent
        numIter = numIter + 1
        for index, row in cData.iterrows():
            data_point = row[row["A2":"A10"]]
            cData.loc[index,"P_Class"] = predClass(data_point,newCent)
        newCent = getCentroid(cData,init=False)
        
    print("Final Mean:\n")
    print(newCent[0])
    print(newCent[1])
    print("\nCluster Assignments:\n", cData[['Scn','CLASS','P_Class']].head(20))
    #cData.to_csv("../Data/breast_cancer_clusters")

    
def main():
    print("\n This program analyses the Breast Cancer Data \n")
    # Load the data into a data frame, forward fill the NA values and convert to int 
    brCancerRawData = pd.read_csv("../Data/Breast-Cancer-Wisconsin.csv" , na_values = '?', dtype = 'str')
    brCancerRawData["A7"] = brCancerRawData["A7"].ffill()
    brCancerRawData = brCancerRawData.astype(int)

    
    getClusterInfo(brCancerRawData)
   
    
main()


