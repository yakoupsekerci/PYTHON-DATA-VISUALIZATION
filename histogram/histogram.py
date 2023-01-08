# -*- coding: utf-8 -*-
"""
Created on Sun Jun 12 19:36:24 2022

@author: yakou
"""
"""
Histogram ile bar plot aynı şey değildir, ilk bilinmesi gereken nokta olarak bunu belirtmek gerek. 
Görsel olarak birbirlerine çok benzeyebilirler fakat kullanım alanları ve mantıkları birbirinden 
farklıdır. Bar plotı zaten görmüştük, bar plot kategorik değişkenlerin görselleştirmesinde her bir 
gruba ait bilgilerin sunulmasında kullanılıyordu. Histogram ise sayısal değişkenlerin aralıklara 
indirilerek gösteriminden oluşuyor. Bar plot direkt olarak “hayvanlar” değişkeninin değerleri olan 
“memeliler”, “sürüngenler”, “deniz canlıları” gibi gruplara ait grupların bilgilerini çubuklar ile 
sunuyor ve karşılaştırma yapmamızı sağlıyor iken; Histogram “yaş” gibi sayısal bir değişkenin “0-9”,
“10-19″,”20-29” … “60-69”, “70-79” gibi aralıkları çubuklayarak bu aralıkların dağılımı/yoğunluğu 
hakkında bilgi sahibi olmamızı sağlıyor. Görsellere dikkat ederseniz de barplot çubukları arasında
boşluklar bulunurken histogram çubukları arasında boşluk olmaksızın çubuklar dipdibe sıralanır.
"""


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

df = pd.read_csv("ornek.csv")
print(df)


print(df.describe())

#tek değişken histogram
examgrade = df['Vize']
plt.hist(examgrade, edgecolor="black", color ="Gray",bins=5,label="Not")
plt.xlabel("Sınav Notları")
plt.ylabel("Frekans")
plt.legend()
plt.title("Sınav Notları Dağılımı")
plt.show()

df = pd.read_csv("lessons.csv")
print(df)

#normal dağılımın histogramda belirmesi...
mathscore = df['Maths']
plt.hist(mathscore,bins=10,color="cyan",ec="Black",density=1,alpha=0.5,label="Not")

mu, sigma = stats.norm.fit(mathscore)
best_fit_line = stats.norm.pdf(mathscore, mu, sigma)
print(f"Rastgele Normal Dagılım Ortalaması...: {mu},Dağılımın Ortalaması...:{df['Maths'].mean()}")
print(f"Rastgele Normal Dagılım Ortalaması...: {sigma},Dağılımın Ortalaması...:{df['Maths'].std()}")
plt.plot(mathscore, best_fit_line, 'g-o')
plt.xlabel("Sınav Notları")
plt.ylabel("Frekans")
plt.legend()
plt.title("Sınav Notları Dağılımı")
plt.show()









