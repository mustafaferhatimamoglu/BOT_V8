# importing the library
import pymssql

try:
    import Common
except:
    from Operations import Common

conn = pymssql.connect(
    server="172.19.208.1",
    user="sa",
    password="sapass",
    database="BINANCE_V3_005",
    as_dict=True,
)
#conn.autocommit(True)
print('Connection Established')
cursor = conn.cursor()
conn.close()
print('Connection Closed')

def SQL_Init():
    conn = pymssql.connect(
        server="172.19.208.1",
        user="sa",
        password="sapass",
        database="BINANCE_V3_005",
        as_dict=True,
    )
    #conn.autocommit(True)
    print('Connection Established')
    cursor = conn.cursor()

def SQL(sql_Query):
    SQL_Init()
    cursor.execute(sql_Query)
    conn.close()

def SQL_Insert(sql_Query):
    SQL_Init()
    cursor.execute(sql_Query)
    conn.commit()# bu olacak mı olmayacak mı?
    conn.close()

def SQL_Select(sql_Query):
    SQL_Init()
    cursor.execute(sql_Query)
    records = cursor.fetchall()
    conn.close()
    return records