# import SentimentIntensityAnalyzer class 
# from vaderSentiment.vaderSentiment module.
import pandas as pd
from pandas import ExcelWriter
import xlsxwriter
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer 

excel_file = 'Times_of_India_Healines_since_jan_2020.xlsx'
xls_file = pd.ExcelFile(excel_file)
df = xls_file.parse('List')
print(type(df))
rows = df.shape[0]
print(rows)
positive_list = []
negative_list = []
neutral_list = []
compound_list = []

for i in range(0, rows):
    sid_obj = SentimentIntensityAnalyzer() 
    sid_obj = SentimentIntensityAnalyzer()
    sentiment_dict = sid_obj.polarity_scores(df.iloc[i]['Headline'])
    Negative = sentiment_dict['neg']*100
    Neutral = sentiment_dict['neu']*100
    Positive = sentiment_dict['pos']*100
    Compound = sentiment_dict['compound']*100
    positive_list.append(Positive)
    negative_list.append(Negative)
    neutral_list.append(Neutral)
    compound_list.append(Compound)

df["Positive"] = positive_list
df["Negative"] = negative_list
df["Neutral"] = neutral_list
df["Compound"] = compound_list
print(df)
writer = ExcelWriter('Times_of_India_Healines_since_jan_2020_score.xlsx',engine='xlsxwriter')
df.to_excel(writer,sheet_name='Score')
writer.save()
