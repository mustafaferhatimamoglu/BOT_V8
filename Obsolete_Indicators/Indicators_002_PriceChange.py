from Operations import Common
from Operations import CreateKline
from Operations import Database

import pandas as pd

sql_Query = """
select 
(Kline_close_time+1)/1000 as 'Timestamp'
,dateadd(S, (Kline_close_time+1)/1000, '1970-01-01') as 'Date_Timestamp'
,Open_price as 'Open'
,High_price as 'High'
,Low_price as 'Low'
,Close_price as 'Close'
,Volume as 'Volume'
from BTCUSDT_1m
order by Kline_open_time
OFFSET 2328500 ROWS
"""

records = Database.SQL_Select(sql_Query)
df = pd.DataFrame(records)

from datetime import datetime



last_High = 1
last_Low = 1
last_Close = 1

for index, row in df.iterrows():
    df.loc[index, 'PriceChange_High_High'] = (row.High - last_High) / (last_High ) * 100
    df.loc[index, 'PriceChange_High_Low'] = (row.High - last_Low) / (last_Low ) * 100
    df.loc[index, 'PriceChange_High_Close'] = (row.High - last_Close) / (last_Close ) * 100

    df.loc[index, 'PriceChange_Low_High'] = (row.Low - last_High) / (last_High ) * 100
    df.loc[index, 'PriceChange_Low_Low'] = (row.Low - last_Low) / (last_Low ) * 100
    df.loc[index, 'PriceChange_Low_Close'] = (row.Low - last_Close) / (last_Close ) * 100

    df.loc[index, 'PriceChange_Close_High'] = (row.Close - last_High) / (last_High ) * 100
    df.loc[index, 'PriceChange_Close_Low'] = (row.Close - last_Low) / (last_Low ) * 100
    df.loc[index, 'PriceChange_Close_Close'] = (row.Close - last_Close) / (last_Close ) * 100
    


    last_High = row['High']
    last_Low = row['Low']
    last_Close = row['Close']
print(df)
df['Date_Timestamp'] = df["Timestamp"].apply(lambda x: datetime.utcfromtimestamp(x).strftime('%d-%m-%Y %H:%M:%S'))
print(df)
print(type(df))
print(type(df.iloc[0,0]))
print(df.iloc[4,15])
print(float(df.iloc[4,15]))
print ("%.16f" %float(df.iloc[4,15]))
#print(df_Indicator)
