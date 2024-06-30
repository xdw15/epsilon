# -*- coding: utf-8 -*-
"""
Created on Sun Jun 30 00:17:10 2024

@author: P048168
"""


import pandas as pd
import plotly.io as pio
import plotly.express as px
pio.renderers.default='browser'

df=pd.read_excel(r'C:\Users\p048168\Downloads\Datos_TF.xlsx',
                sheet_name='Brasil')



df.head()

fig=px.line(df,x='date',y='TOT')

fig.show()
