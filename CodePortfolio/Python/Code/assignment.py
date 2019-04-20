import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model as ln
import os

relativePath=os.getcwd()
dataFilePath=relativePath+"/googleplaystore.csv"
data = pd.read_csv(dataFilePath)
lnrm = ln.LinearRegression()
#print(data.columns)
#print(data.head())
print("Select Rating as independent variable and reviews as dependent variable")
rating = data['Rating']
review = data['Reviews']
#print(rating,review)
lnrm.fit(rating, review)
plt.plot(rating, review, 'ro')
plt.title("Ratings vs. Review on AppStore")
plt.xlabel("Reviews")
plt.ylabel("Ratings")
plt.show()