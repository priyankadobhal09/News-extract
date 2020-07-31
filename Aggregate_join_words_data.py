#used in chord chart analysis for tableau

import json
import requests
import pandas as pd
from pandas import ExcelWriter
import xlsxwriter
import numpy as np

excel_file = 'Times_of_India_Healines_words.xlsx'
xls_file = pd.ExcelFile(excel_file)
df = xls_file.parse('Words')
rows = df.shape[0]
print(rows)

df1 = df

df2 = pd.merge(df, df1, on ='S_No')
print(type(df2))
print(df2.shape[0])

df2['Concat_column'] = df2['Words_x'] + '-' + df2['Words_y']

print(df2)
#for col in df2.columns: 
#    print(col)
##    
number_of_times  = df2.groupby(['Concat_column']).agg({'Concat_column': "count"})
print(number_of_times)

writer = ExcelWriter('Times_of_India_Healines_words_aggregated.xlsx',engine='xlsxwriter')
df2.to_excel(writer,sheet_name='Words')
writer.save()
print("Saved to file")
