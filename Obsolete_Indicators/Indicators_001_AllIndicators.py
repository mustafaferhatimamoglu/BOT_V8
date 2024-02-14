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
OFFSET 2200000 ROWS
"""

records = Database.SQL_Select(sql_Query)
df = pd.DataFrame(records)


print(df.head())
df = df.apply(pd.to_numeric, downcast='float')
print(df.head())
import ta
df = ta.utils.dropna(df)
print(df.head())
df = ta.add_all_ta_features(
    df, "Open", "High", "Low", "Close", "Volume", fillna=True
)
print(df.head())
from datetime import datetime

df['Date_Timestamp'] =df["Timestamp"].apply(lambda x: datetime.utcfromtimestamp(x).strftime('%d-%m-%Y %H:%M:%S'))
print(df.head())