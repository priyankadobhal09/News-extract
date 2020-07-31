import bs4
from urllib.request import urlopen
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
from pandas import ExcelWriter
import xlsxwriter
#import pandas to convert list to data frame
import pandas as pd
import datetime

Headline_list=[]
Headline_Link_list=[]
start_date_list = []
url_list = []

start_date = datetime.date(2020, 1, 1)
end_date = datetime.date(2020, 7, 19)
delta = datetime.timedelta(days=1)

date_string = 43831

while start_date <= end_date:
    #print(start_date)
    year = start_date.year
    month = start_date.month
    day = start_date.day
    my_url= 'https://timesofindia.indiatimes.com/' + str(year) + '/' + str(month) + '/' + str(day) +'/archivelist/year-' + str(year) + ',' + 'month-' + str(month) + ',starttime-' + str(date_string) + '.cms'
    uClient = uReq(my_url)
    page_html=uClient.read()
    uClient.close()
    page_soup=soup(page_html,"html.parser")
    main_container = page_soup.findAll("span",{"style":"font-family:arial ;font-size:12;color: #006699"})
    containers = main_container[0].findAll("a")

    #print(start_date)
    for container in containers:
        #print(container)
        Headline = container.text
        Headline_Link = container.get("href")
        #print(Headline)
        
        #Append to list
        Headline_list.append(Headline)
        Headline_Link_list.append(Headline_Link)
        start_date_list.append(start_date)
        url_list.append(my_url)
        
    
    date_string += 1
    start_date += delta

#Write to dataframe
df=pd.DataFrame(zip(url_list,start_date_list,Headline_list,Headline_Link_list),columns=['URL','Date','Headline','Headline Link'])
#print(df)
writer = ExcelWriter('Times_of_India_Healines_since_jan_2020.xlsx',engine='xlsxwriter')
df.to_excel(writer,sheet_name='List')
writer.save()  
