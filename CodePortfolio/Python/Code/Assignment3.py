#Question 1

import pandas
import os
import matplotlib.pyplot as plt
import numpy as np

relativePath=os.getcwd()
dataFilePath=relativePath+"/Resources/barGraph.csv"
data = pandas.read_csv(dataFilePath)
df = (data.groupby('Business').sum())
ax = df.T.plot.bar(width=0.25, alpha=0.6, figsize=(12,10),subplots=True,
        layout=(3, 2), sharex=True, sharey=True )


#*****************************************************

Question 2

import pandas
import os
import matplotlib.pyplot as plt

relativePath=os.getcwd()
dataFilePath=relativePath+"/Resources/barGraph.csv"
data = pandas.read_csv(dataFilePath)
fig,axs = plt.subplots(2,3,figsize=(12, 8))
count = 0
colors = ['#ff9999','#99ff99','#ff1970','#AA55D4','#66b3ff','#23cc99','#aaE28E','#737380']
for (idx, row) in (data.set_index('Business').iterrows()):
    ax = axs[count // 3, count % 3]
    ax.pie(row, startangle=30,autopct='%.1f%%',radius=1.3, pctdistance=.7, colors=colors)
    count += 1
    ax.set(title=idx,aspect='equal')
plt.legend(labels=row.index, bbox_to_anchor = (1,1))
fig.subplots_adjust(wspace=.5)
plt.show()

#*****************************************************

Question 3

import os
import re
import matplotlib.pyplot as plt
from wordcloud import WordCloud

relativePath = os.getcwd()
filePath = relativePath + "/Resources/Gandhi_Speech.txt"

mySentence = ''
mySentence = open(filePath, "r", encoding="utf8").read()
mySentence = re.sub(r"[,.;@#?!&$']+\ *", " ", mySentence)
mySentence.lower()
myListFinal = [i for i in mySentence.split(' ') if len(i) >= 4]
mySentence = ' '.join(myListFinal)

wordcloud = WordCloud(width=600, height=400, max_font_size=75, max_words=200, background_color="white").generate(mySentence)
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")

#*****************************************************

Question 4

import os
import pandas as pd
import re
import matplotlib.pyplot as plt

relativePath = os.getcwd()
filePath = relativePath + "/Resources/ReviewID.txt"

data = pd.read_csv(filePath,sep=":",names = ["RevId" , "lang"])
df = (data.groupby('lang').count()).sort_values('RevId',ascending=False)
prcntg = df.apply(lambda RevId: 100*RevId/float(RevId.sum()))
ax = prcntg.plot(kind='bar', colormap='Paired', figsize=(12,10))
plt.show()