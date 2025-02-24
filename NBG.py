
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


# html

xml_response = requests.get(url_xml)

from bs4 import BeautifulSoup
import pandas as pd

bs = BeautifulSoup(xml_response.text, 'html.parser')
rows = bs.find_all('description')


dataftame = []

for row in rows:
    html_content = row.text.strip()
    soup = BeautifulSoup(html_content, 'html.parser')

    table_rows = soup.find_all('tr')
    for table_row in table_rows:
        cells = table_row.find_all('td')

        row_data = [
            cells[0].text.strip(),
            cells[2].text.strip()
        ]
        dataftame.append(row_data)

print(pd.DataFrame(dataftame))
