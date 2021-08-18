#!/usr/bin/python3

import requests
import json

url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/market/v2/get-quotes"

symbol = input('Please enter a ticker for a us company: ' )

querystring = {"region":"US","symbols":symbol}

headers = {
    'x-rapidapi-key': "insert_api_key_here",
    'x-rapidapi-host': "apidojo-yahoo-finance-v1.p.rapidapi.com"
    }

response = requests.get(url,headers=headers,params=querystring)

##quoteresponse { 'result': [{your_data_points]]

data = response.json()
result = data['quoteResponse']['result'][0]


#values that we are interested in
name = result['longName']
ticker = result['symbol']
current_market_price = result['regularMarketPrice']
market_high = result['regularMarketDayHigh']
market_low = result['regularMarketDayLow']
market_cap = result['marketCap']
volume = result['regularMarketVolume']



print('Company Name: ', name)
print('Ticker: ', ticker)
print('Current Market Price: ', current_market_price)
print('Market High: ', market_high)
print('Market Low: ', market_low)
print('Market Cap:', market_cap)
print('Volume: ', volume)

print("Stonks Never Go Down")
