# importing the library
import pymssql
import pandas as pd

try:
    import Common
except:
    from Operations import Common

string_Server = "172.19.208.1"
string_User="sa"
string_Password="sapass"
string_Database="BINANCE_V3_006"

def SQL(sql_Query):
    with pymssql.connect(
        server=string_Server,
        user=string_User,
        password=string_Password,
        database=string_Database,
        as_dict=True,
    ) as conn:
        with conn.cursor(as_dict=True) as cursor:
            cursor.execute(sql_Query)

def SQL_Insert(sql_Query):
    with pymssql.connect(
        server=string_Server,
        user=string_User,
        password=string_Password,
        database=string_Database,
        as_dict=True,
    ) as conn:
        with conn.cursor(as_dict=True) as cursor:
            cursor.execute(sql_Query)
            conn.commit()

def SQL_Select(sql_Query):
    with pymssql.connect(
        server=string_Server,
        user=string_User,
        password=string_Password,
        database=string_Database,
        as_dict=True,
    ) as conn:
        with conn.cursor(as_dict=True) as cursor:
            cursor.execute(sql_Query)
            records = cursor.fetchall()
            return records

