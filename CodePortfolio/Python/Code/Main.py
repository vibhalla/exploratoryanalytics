"""
Created on Sat Jul 20 20:31:58 2019
Final Project Phase 3
Analysis of available Breast Cancer data
@author: vishal_bhalla
"""

import pandas as pd
import numpy as np

    
def getPredictionError(pred):
    # Function to calculate Error values
    # Calculate the total values, rows with predicted rows =2 , 4
    ttlRows = pred["CLASS"].count()
    ttl2Rows = (pred.P_Class.values == 2).sum()
    ttl4Rows = (pred.P_Class.values == 4).sum()
    
    # Create a DF with incorrect predictions
    predFalse = pred[pred["CLASS"] != pred["P_Class"]]
    falseRows = predFalse["CLASS"].count()
    false2Rows = (predFalse.P_Class.values == 2).sum()
    false4Rows = (predFalse.P_Class.values == 4).sum()
    
    print("\n --- Error Rates in Clustering --- \n")
    print("\nTotal Rows: ",ttlRows,"\nTotal Rows predicted 2: ", ttl2Rows,
          "\nTotal Rows predicted 4: ",ttl4Rows)
    print("\nIncorrectly Predicted Rows: ",falseRows,"\nIncorrectly predicted as 2: " 
          , false2Rows, "\nIncorrectly predicted as 4: ",false4Rows)
    print("\nerror B = " , false4Rows , "/" , ttl2Rows , "= ",
          (np.around(false4Rows/ttl2Rows,decimals=4)))
    print("error M = " , false2Rows , "/" , ttl4Rows , "= ",
          (np.around(false2Rows/ttl4Rows,decimals=4)))
    print("Total error rate = " , falseRows , "/" , ttlRows , "= ",
          (np.around(falseRows/ttlRows,decimals=4)))
    
def main():
    print("\n This program analyses the Breast Cancer Data \n")
    # Load the data into a data frame, forward fill the NA values and convert to int 

    brCancerPredictions = pd.read_csv("../Data/breast_cancer_clusters")
    getPredictionError(brCancerPredictions)
    
main()


