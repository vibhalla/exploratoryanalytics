"""
Created on Thu May 23 22:19:21 2019
Assignment 3 - Question 3_2
This program counts the numbers divisible by 7
@author: vishal_bhalla
"""

def main():
    count = 0
    print("This program prints the count of numbers divisible by 7.")
    num = eval( input("Enter a positive integer: " ))
    for i in range(1,num+1,1):
        if i%7 == 0:
            count = count + 1
    if count != 1:
        print("There are ",count, " numbers between 1 and",num, " divisible by 7")
    else:
        print("There is ",count, " number between 1 and",num, " divisible by 7")
    
main()
    