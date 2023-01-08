# -*- coding: utf-8 -*-
"""
Created on Fri Jun 24 20:42:09 2022

@author: yakou
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("ornek.csv")
print(df.head()) 

df.plot.bar(x='car', y='total', rot=0)
df.plot.bar(x="car")


df.plot.bar( x = 'car' ,  rot = 0 , color =[(240/255,83/255,101/255), (250/255,188/255,42/255)], title="BAR CHART", figsize=(10,4) )












