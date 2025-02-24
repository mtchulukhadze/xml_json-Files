
import configparser
import datetime

import requests
import json

config = configparser.ConfigParser()
config.read(r'D:\Data\Data Engineering\NBG.ini')
url = config['DEFAULT']['url']

try:
    data = requests.get(url)
    data1 = json.loads(data.text)
    print(url)
    print(data1)
except Exception as e:
    print("File is Empty")
    print(e)

for i in data1:
    curr = i['currencies']
    for c in curr:
        data = c['code'], c['rateFormated'], c['date'], c['validFromDate']
        if c['code'] == 'USD':
            print(data[0], data[1], datetime.datetime.strptime(data[2], '%Y-%m-%dT%H:%M:%S.%fZ').strftime('%y-%m-%d'), datetime.datetime.strptime(data[3], '%Y-%m-%dT%H:%M:%S.%fZ').strftime('%y-%m-%d'))


