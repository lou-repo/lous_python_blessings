#!/usr/bin/python3

import requests
import json

url = "https://alpha-vantage.p.rapidapi.com/query"

crypto = input("Please enter a crypto currency symbol you would like to convert (ie. btc): ").upper()
fiat = input("Please enter a fiat currency you would like to convert crypto (ie. usd): ").upper()

querystring = {"to_currency":fiat,"function":"CURRENCY_EXCHANGE_RATE","from_currency":crypto}

headers = {
    'x-rapidapi-key': "<insert_api_key_here>",
    'x-rapidapi-host': "alpha-vantage.p.rapidapi.com"
    }

response = requests.get(url, headers=headers, params=querystring)
data = response.json()
result = data['Realtime Currency Exchange Rate']

crypto_code = result['1. From_Currency Code']
crypto_name = result['2. From_Currency Name']
fiat_code = result['3. To_Currency Code']
fiat_name = result['4. To_Currency Name']
exchange_rate = result['5. Exchange Rate']
last_refresh = result['6. Last Refreshed']
time_zone = result['7. Time Zone']
bid = result['8. Bid Price']
ask = result['9. Ask Price']

print('Cryptocurrency Name: ', crypto_name)
print('Fiat Currency Conversion: ', fiat_name)
print('Current Exchange Rate: ', float(exchange_rate))
print('Last Refresh Rate: ' , last_refresh , time_zone)
print('Current Bid: ' , float(bid) , fiat_code)
print('Current Ask: ' , float(ask) , fiat_code)

