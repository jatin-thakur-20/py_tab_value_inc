# -*- coding: utf-8 -*-
"""
Created on Sat Jul  1 15:48:00 2023

@author: jatin
"""

import pandas as pd

data = pd.read_csv('transaction2.csv',sep=';')

#summary of data
data.info()


data['CostPerTransaction']=data['CostPerItem']*data['NumberOfItemsPurchased']

data['SalesPerTransaction']=data['SellingPricePerItem']*data['NumberOfItemsPurchased']

data['ProfitPerTransaction']=data['SalesPerTransaction']-data['CostPerTransaction']

data['Markup']=round(data['ProfitPerTransaction']/data['CostPerTransaction'],4)

data['Day']=data['Day'].astype('str')

data['Year']=data['Year'].astype('str')

data['Date']=data['Day']+'-'+data['Month']+'-'+data['Year']

data['ClientAge']=data['ClientKeywords'].str.split(',',expand=True)[0]

data['ClientType']=data['ClientKeywords'].str.split(',',expand=True)[1]

data['ClientContractLength']=data['ClientKeywords'].str.split(',',expand=True)[2]

data['ClientAge']=data['ClientAge'].str.replace('[','')

data['ClientContractLength']=data['ClientContractLength'].str.replace(']','')

data['ItemDescription']=data['ItemDescription'].str.lower()

seasons = pd.read_csv(r'C:\Users\jatin\Downloads\Python+Tableau Project\Value_inc/value_inc_seasons.csv',sep=';')

seasons

data = pd.merge(data,seasons,on='Month')

drop_columns = ['Day','Month','Year','ClientKeywords']
data.drop(drop_columns,axis=1,inplace=True)

data.to_csv('ValueInc_cleaned.csv',index=False)




