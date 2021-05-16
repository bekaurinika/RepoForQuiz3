import json
import sqlite3

import requests
from tkinter import *

resp = requests.get('https://api.coinlore.net/api/ticker/?id=90')
jsonResp = resp.json()[0]
# 1
print(resp.status_code)
print(resp.headers['content-type'])
# 2
with open('file.json', 'w') as json_file:
    json.dump(jsonResp, json_file, indent=4)
# 3
print(f"{jsonResp['name']}:{jsonResp['price_usd']}$")
# 4
conn = sqlite3.connect('file.sqlite')
cursor = conn.cursor()
# CREATE TABLE
# cursor.execute('''CREATE TABLE CryptoPriceLog(
#    CRYPTO_NAME CHAR(20) NOT NULL,
#    PRICE CHAR(20)
# )''')
# INSERT DATA
cursor.execute(
    f'INSERT INTO CryptoPriceLog (CRYPTO_NAME, PRICE) VALUES (?, ?)',
    (jsonResp['name'], jsonResp['price_usd']))

conn.commit()
conn.close()
