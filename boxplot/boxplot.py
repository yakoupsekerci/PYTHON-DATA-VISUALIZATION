# -*- coding: utf-8 -*-
"""
Created on Sat Jun 25 15:32:02 2022

@author: yakou
"""

import pandas as pd
import seaborn as sns

df = pd.read_csv("ornek.csv")
print(df)

sns.boxplot(x=df["Score"], width=0.5)




