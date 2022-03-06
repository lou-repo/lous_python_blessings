#!/usr/bin/python3

import tkinter
from tkinter import *
from tkinter import Label
import json
import requests



window = Tk()
window.geometry("250x300")
window.configure(background='#242B2E')
window.title("")


URLAPI = "https://alpha-vantage.p.rapidapi.com/query"

CRYPTO = "BTC"
FIAT = "USD"

querystring = {"to_currency":FIAT,"function":"CURRENCY_EXCHANGE_RATE","from_currency":CRYPTO}

headers = {
    'x-rapidapi-key': "<insert_api_key_here>",
    'x-rapidapi-host': "alpha-vantage.p.rapidapi.com"
    }

response = requests.get(URLAPI, headers=headers, params=querystring)
data = response.json()
result = data['Realtime Currency Exchange Rate']


EXCHANGE_RATE = result['5. Exchange Rate']
CRYPTO_CURRENT = (1/float(EXCHANGE_RATE))


def conversion():
    btc=(float(dollars.get())*CRYPTO_CURRENT)
    bitcoin_conversion_result.delete("1.0")
    bitcoin_conversion_result.insert(END, btc)


title_of_app = StringVar()
title_of_app.set("CrypoConverter v.1")
title_of_app_label = Label(window, font='times 20', background='#242B2E', fg='#e74c3c' , textvariable=title_of_app)
title_of_app_label.grid(row=1, column=0, padx=10, pady=10)

dollars = StringVar()
dollar_exchange_entry = Entry(window, textvariable=dollars)
dollar_exchange_entry.grid(row=2, column=0, padx=10, pady=10)

dollar_text = StringVar()
dollar_text.set("Dollars: ")
dollar_label = Label(window, font='times 15', background='#242B2E', fg='#fffdd0', textvariable=dollar_text, justify=LEFT, anchor="w")
dollar_label.grid( sticky = W,row=3, column=0, pady=5)


bitcoin_conversion_result = Text(window, height=1, width=20)
bitcoin_conversion_result.grid(row=4, column=0, padx=30, pady=10) 

btc_text = StringVar()
btc_text.set("Bitcoin: ")
btc_label = Label(window, font='times 15', background='#242B2E', fg='#fffdd0', textvariable=btc_text, justify=LEFT, anchor="w")
btc_label.grid( sticky = W,row=5, column=0, pady=5)


convert_button = Button(window, text="Convert", bg='#75DA8B', command=conversion)
convert_button.grid(row=6, column=0)


window.mainloop()

