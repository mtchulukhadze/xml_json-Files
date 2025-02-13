

import configparser
import requests
import pyodbc
import pandas as pd
import time

config = configparser.ConfigParser()

try:
    config.read(r'D:\Data\Data Engineering\ETLDemo.ini')
    url = config['DEFAULT']['url']
    date = config['DEFAULT']['date']
    print("Loaded")
except Exception as e:
    print("File is Empty")
    print(e)


try:
    Res = requests.get(url + date)
    if Res.status_code == 200:
        data = Res.json() 
        print(data)
    print(Res)
except Exception as e:
    print("error")
    print(e)

# Database Connection
user = 'DESKTOP-3QJN7S3' + "\)" + "user"
user_rep = user.replace(")", "")

conn = pyodbc.connect("Driver={SQL Server};"
                          "Server=DESKTOP-3QJN7S3;" 
                          f"uid={user_rep}"
                          "Database=ETLDemo;"
                          "Trusted_Connection=yes;")
cursor = conn.cursor()

for row in data['observations']:
    v = row['FXUSDCAD']
    try:
        conn.execute('''insert into ETLDemo.dbo.Expenses (date, rate) 
                        values(?, ?)''',
                     row['d'], v['v'])
        conn.commit()
        print(f"inserted: {enumerate(row)}")
        time.sleep(0.008)
    except Exception as e:
        conn.rollback()
        print(f'error{e}')

try:
    df = pd.read_sql_query('''select * from  ETLDemo.dbo.Expenses''', conn)
    print(df)
except Exception as e:
    conn.rollback()
    print(f'error{e}')
