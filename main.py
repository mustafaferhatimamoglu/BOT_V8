from Operations import Common
from Operations import CreateKline
from Operations import Database

# CreateKline.CreateTable_KlineData('BTCUSDT', '1w')
CreateKline.CreateTable_KlineData('BTCUSDT', '1h')
CreateKline.CreateTable_KlineData('BTCUSDT', '1m')

#   df['bb_hi'] = df['bb_hi'] - df['close']



# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns; sns.set()

# sql_Query = """
# select 
# (Kline_close_time+1)/1000 as 'Timestamp'
# ,dateadd(S, (Kline_close_time+1)/1000, '1970-01-01') as 'Date_Timestamp'
# ,Open_price as 'Open'
# ,High_price as 'High'
# ,Low_price as 'Low'
# ,Close_price as 'Close'
# ,Volume as 'Volume'
# from BTCUSDT_1m
# order by Kline_open_time
# OFFSET 2200000 ROWS
# """

# records = Database.SQL_Select(sql_Query)
# df = pd.DataFrame(records)
# # df = df.apply(pd.to_numeric, downcast='float')
# print(df)

# plt.figure(figsize=(14, 5))
# sns.set_style("ticks")
# sns.lineplot(data=df, x="Date_Timestamp", y='Low', color='red')
# sns.lineplot(data=df, x="Date_Timestamp", y='High', color='green')
# sns.lineplot(data=df, x="Date_Timestamp", y='Close', color='firebrick')
# sns.despine()
# #plt.title("The Stock Price of Amazon", size='x-large', color='blue')

# import matplotlib
# matplotlib.pyplot.show()

