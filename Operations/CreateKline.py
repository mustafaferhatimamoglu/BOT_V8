
try:
    import Common
    import Database
except:
    from Operations import Common
    from Operations import Database




def CreateTable_KlineData(var_CoinName, var_Interval):
    identifier = var_CoinName + "_" + var_Interval
    sql_Query = """
    --GO
--/****** Object:  Table [dbo].[{0}]    Script Date: 21.12.2023 19:07:21 ******/
SET ANSI_NULLS ON
--GO

SET QUOTED_IDENTIFIER ON
--GO

CREATE TABLE [dbo].[{0}](
	[Kline_open_time] [bigint] NOT NULL,
	[Open_price] [decimal](30, 15) NOT NULL,
	[High_price] [decimal](30, 15) NOT NULL,
	[Low_price] [decimal](30, 15) NOT NULL,
	[Close_price] [decimal](30, 15) NOT NULL,
	[Volume] [decimal](30, 15) NOT NULL,
	[Kline_close_time] [bigint] NOT NULL,
	[Quote_asset_volume] [decimal](30, 15) NOT NULL,
	[Number_of_trades] [int] NOT NULL,
	[Taker_buy_base_asset_volume] [decimal](30, 15) NOT NULL,
	[Taker_buy_quote_asset_volume] [decimal](30, 15) NOT NULL,
 CONSTRAINT [PK_{0}] PRIMARY KEY CLUSTERED 
(
	[Kline_open_time] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
--GO
""".format(
        identifier
    )
    # print(sql_Query)
    try:
        Database.SQL_Insert(sql_Query)
        #Database.conn.commit()
        print("Kline Table Created")
    except Exception as exp:
        # print(exp)
        if str(exp).startswith('(2714, b"There is already an object named'): 
            if(GetLastTime_PlusOne(identifier)!=0):
                DeleteLastOne(identifier)
            print("Handled-")
        else:
            print(exp)
            Common.pause()
    # Delete Last One
    startTime = GetLastTime_PlusOne(identifier)
    print(startTime)
    get_KlineData_2_MsSql(var_CoinName, var_Interval, startTime)
    # Fill KlineData





def GetLastTime_PlusOne(identifier):
    resp = Database.SQL_Select(
        "select top 1 Kline_close_time from {0} order by Kline_close_time desc".format(
            identifier
        )
    )
    # print(resp)
    if resp == []:
        time_InUse = 0
    else:
        time_InUse = resp[0]['Kline_close_time']
    print(time_InUse)
    return time_InUse


def DeleteLastOne(identifier):
    try:
        # delete last row
        sql_Query = """
                delete from {0} where Kline_open_time IN (
                select TOP 1 Kline_open_time from {0}
                order by Kline_open_time desc)
                """.format(
            identifier
        )
        print(sql_Query)
        Database.SQL_Insert(sql_Query)
        # conn.commit()
    except Exception as exp:
        if str(exp).startswith(
                "Cannot commit transaction: (3902, b'The COMMIT TRANSACTION request has no corresponding BEGIN"
        ):
            print("Handled-NOT")
            print(exp)
            Common.pause()
        else:
            print(exp)
            Common.pause()





import logging
from binance.um_futures import UMFutures
from binance.lib.utils import config_logging

import json

um_futures_client = UMFutures()

dict_BinanceTime = um_futures_client.time()
string_BinanceTime = json.dumps(dict_BinanceTime)
parsed_json = json.loads(string_BinanceTime)

# print(f"{parsed_json['serverTime']}")
# print(int((parsed_json["serverTime"]) / 1000))

serverTime = int(parsed_json["serverTime"])

# data_starttime = 0

open_time = 0.0
open_price = 0.0
high_price = 0.0
low_price = 0.0
close_price = 0.0
volume = 0.0
close_time = 0.0
quote_asset_volume = 0.0
number_of_trades = 0.0
taker_buy_base_asset_volume = 0.0
taker_buy_quote_asset_volume = 0.0


def get_KlineData_2_MsSql(var_CoinName, var_Interval, var_starttime):
    counter_kline = 0
    flag_KlineStop = False
    string_Insert = "\n"
    while True:
        kline_response = um_futures_client.klines(
            var_CoinName, var_Interval, limit=999, starttime=var_starttime
        )        
        string_Insert = """
        
        --BEGIN TRAN
        """
        for kline in kline_response:
            # open_time = kline[0]
            # open_price = kline[1]
            # high_price = kline[2]
            # low_price = kline[3]
            # close_price = kline[4]
            # volume = kline[5]
            close_time = kline[6]
            # quote_asset_volume = kline[7]
            # number_of_trades = kline[8]
            # taker_buy_base_asset_volume = kline[9]
            # taker_buy_quote_asset_volume = kline[10]
            counter_kline += 1
            string_Insert += """
                INSERT INTO [dbo].[{11}_{12}] ([Kline_open_time],[Open_price],[High_price],[Low_price],[Close_price],[Volume],[Kline_close_time],[Quote_asset_volume],[Number_of_trades],[Taker_buy_base_asset_volume],[Taker_buy_quote_asset_volume]) VALUES ({0},{1},{2},{3},{4},{5},{6},{7},{8},{9},{10})
            """.format(
                kline[0], kline[1], kline[2], kline[3], kline[4], kline[5], kline[6], kline[7], kline[8], kline[9],
                kline[10], var_CoinName, var_Interval,
            )
            if (string_Insert.find("..") != -1):
                print("BOK")
            if serverTime < close_time:
                print(counter_kline)
                flag_KlineStop = True
                break
        string_Insert += """
        --GO

        --COMMIT TRAN
        """
        #print(string_Insert)
        Database.SQL_Insert(string_Insert)
        print(counter_kline)
        if flag_KlineStop:
            break
        else:
            var_starttime = close_time + 1
            # print("aa")
        # print(string_Insert)
