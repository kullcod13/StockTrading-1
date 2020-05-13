####  Get the data from oanda in minute data


##########  IMPORTS

import oandapyV20
from oandapyV20 import API 
import oandapyV20.endpoints.instruments as instruments
import pandas as pd
import random
########## GLOBALS





########## FUNCTIONS
def Flow():
    Format_Data()

#### This uses my account information to give to the request
def Get_Account_Info():
    accountID = ''
    access_token = ''
    client = oandapyV20.API(access_token=access_token)
    return client


def  Currency_Pairs():
    pairs = ['EUR_USD', 'EUR_CHF', 'EUR_GBP', 'EUR_JPY', 'EUR_AUD', 'USD_CAD', 'USD_CHF', 'USD_JPY', 'USD_MXN', 'GBP_CHF', 'GBP_JPY', 'GBP_USD', 'AUD_JPY', 'AUD_USD', 'CHF_JPY', 'NZD_JPY', 'NZD_USD', 'XAU_USD', 'EUR_CAD', 'AUD_CAD', 'CAD_JPY', 'EUR_NZD', 'GRX_EUR', 'NZD_CAD', 'SGD_JPY', 'USD_HKD', 'USD_NOK', 'USD_TRY', 'XAU_AUD', 'AUD_CHF', 'AUX_AUD', 'EUR_HUF', 'EUR_PLN', 'FRX_EUR', 'HKX_HKD', 'NZD_CHF', 'SPX_USD', 'USD_HUF', 'USD_PLN', 'USD_ZAR', 'XAU_CHF', 'ZAR_JPY', 'BCO_USD', 'ETX_EUR', 'CAD_CHF', 'EUR_DKK', 'EUR_NOK', 'EUR_TRY', 'GBP_CAD', 'NSX_USD', 'UKX_GBP', 'USD_DKK', 'USD_SGD', 'XAG_USD', 'XAU_GBP', 'EUR_CZK', 'EUR_SEK', 'GBP_AUD', 'GBP_NZD', 'JPX_JPY', 'UDX_USD', 'USD_CZK', 'USD_SEK', 'WTI_USD', 'XAU_EUR', 'AUD_NZD']
    stock = random.sample(pairs,1)
    return stock
    

#### This makes the request to oanda
def Make_Request():
    client = Get_Account_Info()
    pair = Currency_Pairs()
    pair = pair[0]
    #print(pair,pair[0])
    print(pair)

    params = {
          "count": 250,
          "granularity": "D"}


    try:
        r = instruments.InstrumentsCandles(instrument=pair, params=params)
        data = client.request(r)
    except:
        print('That stock isnt supported')
    
    return data


def Format_Data():
    data = Make_Request()
    #print(data)


    dat = []
    for oo in data['candles']:
        dat.append([oo['time'], oo['volume'], oo['mid']['o'], oo['mid']['h'], oo['mid']['l'], oo['mid']['c']])
    
    df = pd.DataFrame(dat)
    df.columns = ['Time', 'Volume', 'Open', 'High', 'Low', 'Close']
    df = df.set_index('Time')
    df.head()
    print(df)


def Get_Historical_Data():
    client = Get_Account_Info()
    data = oanda.get_history(instrument='ZAR_USD',  # our instrument
                         start='2016-12-08',  # start data
                         end='2016-12-10',  # end date
                         granularity='M1')  # minute bars  # 7


##########  RUN
Flow()
Get_Account_Info()


