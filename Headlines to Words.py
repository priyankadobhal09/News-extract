import json
import requests
import pandas as pd
from pandas import ExcelWriter
import xlsxwriter
import numpy as np

excel_file = 'Times_of_India_Healines_since_jan_2020.xlsx'
xls_file = pd.ExcelFile(excel_file)
df = xls_file.parse('List')
print(type(df))
rows = df.shape[0]
print(rows)


df['Headline'] = df['Headline'].str.replace("\n", " ")

#print(df)
new_df = pd.DataFrame(df.Headline.str.split(' ').tolist(), index=df.S_No).stack()

#print(new_df)

new_df = new_df.reset_index([0, 'S_No'])
#print(new_df)

new_df.columns = ['S_No', 'Words']

#print(new_df)

df_words = pd.merge(df, new_df, on='S_No', how='inner')

#print(df_words)

list = ['.', ',', '"', '?', "!", '(', ')', '2x', '<', '*']

for i in list:

    df_words['Words'] = df_words['Words'].str.replace(i, "")
    print(df_words)

df_words.dropna()

#print(df_words)

writer = ExcelWriter('Times_of_India_Healines_words.xlsx',engine='xlsxwriter')
df_words.to_excel(writer,sheet_name='Words')
writer.save()

print("Saved to file")
