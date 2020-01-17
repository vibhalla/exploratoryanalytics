# -*- coding: utf-8 -*-
"""
Created on Sun Jul  7 22:31:33 2019
Final Project Phase 1
Analysis of available Breast Cancer data
@author: vishal_bhalla
"""
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

"""
Data Structure
ID 		Sample code number 	id 			number 
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
def calcStat(cData):
    statDF = pd.DataFrame(columns=("mean","median","sd","variance"), index=cData.columns)
    # Calculate and save the stats to statDF dataframe, for one column of cData at a time
    for colName in cData:
        statDF.loc[colName,"mean"] = round(cData[colName].mean(),2)
        statDF.loc[colName,"median"] = round(cData[colName].median(),2)
        statDF.loc[colName,"sd"] = round(cData[colName].std(),2)
        statDF.loc[colName,"variance"] = round(cData[colName].var(),2)
    return statDF

    
def main():
    print("\n This program analyses the Breast Cancer Data \n")
    # Load the data into a data frame, forward fill the NA values and convert to int 
    brCancerRawData = pd.read_csv("../Data/Breast-Cancer-Wisconsin.csv" , na_values = '?', dtype = 'str')
    brCancerRawData["A7"] = brCancerRawData["A7"].ffill()
    brCancerRawData = brCancerRawData.astype(int)
    #Call calcStat function to calculate the various statistics
    statDF = calcStat(brCancerRawData.loc[:,"A2":"A10"])
    print("\n Below are the Mean, Median , Standard Deviation and Variance of the observations in the data \n")
    print(statDF)


main()


