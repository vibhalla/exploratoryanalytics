#Question 1

val = 5
rem = []
while val//2 != 0:
    rem.append(val%2)
    val = val//2
rem.append(1)
rem.reverse();
while len(rem)<4:
    rem.insert(0,0)
print(*rem,sep='')

#***************************************

#Question 2

def binToDec(val):
    if val == []:
        return 0
    else:
        first = (val[0]*(2**(len(val)-1)))
        rem = val[1:]
        return first + binToDec(rem)


testVal = [1,0,0,1]
ans = binToDec(testVal)
print("Decimal for ", testVal , " is : ",ans)

#********************************************

#Question 3

import datetime

myMedDict={
  "Abelcet":"Aug 1 2016",
"Azithromycin":"Dec 24 2016",
"Arava":"Jan 1 2019",
"Arixtra":"May 31 2022",
"Aplenzin":"Jan 3 2020",
"Antizol":"Aug 31 2023",
"Anadrol-50":"Nov 14 2010"
}


def expiredList(val):
    myExp =[]
    for key in val:
        dateExp = datetime.datetime.strptime(val[key], '%b %d %Y')
        if dateExp < datetime.datetime.now():
            myExp.append(key)
    return myExp

myExpiredList = expiredList(myMedDict)

print("List of expired medicines: ",myExpiredList)

#********************************************

#Question 4

def decToBin(val):
    rem=1
    if val//2 != 0:
	rem=val%2
        return [rem] + decToBin(val//2)
    return [val]  
ans=decToBin(9)
ans.reverse();
while len(ans)<4:
    ans.insert(0,0)
print(*ans,sep='')

#********************************************

#Question 5

import csv
import os

relativePath = os.getcwd()
filePath = relativePath + "/Resources/crimeData.csv"

def getCrimeData(colName):
    with open(filePath) as csvfile:
        reader = csv.DictReader(csvfile)
        header = next(reader)
        recCnt = 0
        incCnt = 0
        addLst = []
        for row in reader:
            colInt = int(row[colName])
            recCnt += 1
            incCnt = incCnt + colInt
        avgCnt = incCnt / recCnt
        csvfile.seek(0)
        next(reader)
        for row in reader:
            colInt1 = int(row[colName])
            if avgCnt < colInt1:
                addLst.append(row['Address'])
        print(colName, recCnt, incCnt, avgCnt)
    return addLst

    csvfile.close()

theList = getCrimeData('NON-CRIMINAL')
for row in theList:
    print(row)
	
#********************************************

#Question 6


import os
import pandas
import datetime
relativePath = os.getcwd()
filePath = relativePath + "/Resources/timeData2.csv"
data = pandas.read_csv(filePath)
data.set_index('Dates',inplace=True)
data.index = pandas.to_datetime(data.index)

def getDetails(fromTime,toTime):
    start = datetime.datetime.strptime(fromTime, '%m/%d/%Y %H:%M')
    ends = datetime.datetime.strptime(toTime, '%m/%d/%Y %H:%M')
    print(start,ends)
    crimeData = data.sort_index().loc[start:ends]
    print(crimeData.groupby(['Category'], as_index=False)['Descript'].count().max())
    return 0


getDetails('5/13/2015 9:36','5/18/2015 10:30')