#Question 1
myList=[2,3,4,5]
myListFinal=[]
k=1
for i in myList:
    for j in range(k,len(myList)):
        myListFinal.append(i+myList[j])
    k=k+1
print("Starting List",myList)
print("Summed List",myListFinal) 

#*****************************

myList=[2,3,4,5]
myListFinal=[]
myListFinal.append([i+myList[e] for i in myList for e in range(myList.index(i)+1,len(myList))])
print("Starting List",myList)
print("Summed List",myListFinal) 

############################################

#Question 2

myList=[2,3,4,5,5]
k=1
for i in myList:
    for j in range(myList.index(i)+1,len(myList)):
        if i == myList[j]:
            k=0
print("Starting List",myList)
if k == 0:
    print("Yes")
else:
    print("No")
	
#*****************************	

myList=[2,3,4,5]
k=1
for i in myList:
    for j in range(myList.index(i)+1,len(myList)):
        k=(i^myList[j])
        if k == 0:
            break
    if k == 0:
        break   
print("Starting List",myList)
print("yes") if k == 0 else print("No")

############################################

#Question 3

myMatrix = [[1, 2, 3, 4],
            [5, 6, 7],
            [8, 9, 10]]
myList=[i for row in myMatrix for i in row if i%2 != 0]
myList.sort(reverse=True)
print("My List: ", myList)

############################################

#Question 4

myMatrix = [[1, 2, 'aa',3, 4],
            ['dd',5, 6, 7],
            [8, 9, 10,'cc']]
myList=[i**2 for row in myMatrix for i in row if (isinstance(i,int) and (i%2 == 0))]
print("My List: ", myList)

############################################

#Question 5

myMatrix = [[21, 22, 23, 4, 16, 17, 18, 19],
            [5, 6, 7, 14, 15, 20, 1, 2, 3],
            [8, 9, 10, 11, 12, 13]]
myList=[i**2 for row in myMatrix for i in row if ( i<=3 or (i%6 == 1) or (i%6 == 5))]
print("My List: ", myList)

############################################

#Question 6

mySentence="It's the Spice Girls but not as you know them. Twenty years after it was first released, this famous girl power anthem has been given a 21st century feminist makeover. The new video is part of Project Everyone's campaign to improve the lives of women and girls everywhere, calling for an end to violence against girls, quality education for all and equal pay for equal work."
mySentence=mySentence.replace(",","")
mySentence=mySentence.replace(".","")
mySentence=mySentence.replace("'","")
mySentence=mySentence.lower()
myList=mySentence.split(' ')
myDict={}
myListFinal=[i for i in myList if len(i)>=4]
#print("My Final List: ", myListFinal)
for i in myListFinal:
    myDict[i]=myList.count(i)
print("Dict: ", myDict)

############################################

#Question 7

myList=[2,3,4,5]
myListDouble=[i << 1 for i in myList]
print("My original list:",myList)
print("My Double List: ",myListDouble)

############################################

#Question 8

myMatrix1 = [[1, 2, 3, 4],
            [5, 6, 7,6],
            [8, 9, 10,4]]

myMatrix2 = [[3, 1, 1, 4],
            [7, 7, 7,7],
            [8, 9, 10,11]]
myMatrixFinal=[]
for i in range(0,len(myMatrix1)):
    myMatrix3=[]
    for j in range(0,len(myMatrix1[i])):
        myMatrix3.insert(j,(myMatrix1[i][j]+myMatrix2[i][j]))
    myMatrixFinal.insert(i,myMatrix3)
print("Final Summation Matrix: ",myMatrixFinal)


