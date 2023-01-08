# -*- coding: utf-8 -*-
"""
Created on Fri Jun 10 20:28:54 2022

@author: yakou
"""

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("ornek.csv")
print(df)

# tek bir değişken ile piechart çıkartma.
mylabels = ["Evli", "Bekar"]
explode = (0,0.1)#dilimlere ayırma.
mycolors = ["cyan", "hotpink"]
plt.title("Cinsiyet")
plt.pie(df['Medeni Hali'].value_counts().to_list(), labels = mylabels,autopct='%1.1f%%',explode=explode,startangle=90,shadow=True,colors=mycolors)
plt.legend(title = "Medeni Hal:")
plt.show() 

# bağımsız ve bağımlı değişken belirleyerek piechart çıkartmak.
medenihal=['Evli','Bekar']
for i in medenihal:
    dfmedeni = df[df['Medeni Hali']==i]
    labels = "Erkek","Kadın"
    sizes = (dfmedeni['Cinsiyet'].value_counts()).to_list()
    mycolors = ["cyan", "hotpink"]
    explode = (0,0.1)
    plt.pie(sizes,explode=explode,labels=labels,autopct='%1.1f%%',shadow=True,startangle=90,colors=mycolors)
    plt.legend(title = "")
    plt.title("{} Olanların Cinsiyet Oranı".format(i))
    plt.show()  






