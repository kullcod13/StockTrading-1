####  Get the data from oanda in minute data


##########  IMPORTS

import oandapyV20
from oandapyV20 import API 
import oandapyV20.endpoints.instruments as instruments
import numpy as np
import pandas as pd
import random
import requests
from datetime import timedelta
import v20
#import ta
import math
import talib
from talib import MA_Type
from talib import TSF
from talib import ADX
from talib import MIDPRICE
from talib import MIDPOINT
from talib import TEMA



import matplotlib.pyplot as plt
import mplfinance as mpf
import matplotlib.ticker as mticker

import statsmodels.api as sm
import statsmodels.formula.api as smf


import matplotlib.dates as mpl_dates

plt.style.use('ggplot')

########## GLOBALS





########## FUNCTIONS


#### This uses my account information to give to the request
def Get_Api_Key():
    access_token = 'd5698e5908e8b7989f50c40bac0f1c53-6fbc07c1ea7dad76a287069fb4f931e5'
    return access_token

def Get_AccountId():
    accountID = '101-001-14704433-001'
    return accountID

def Get_Account_Info():
    accountID = '101-001-14704433-001'
    access_token = 'd5698e5908e8b7989f50c40bac0f1c53-6fbc07c1ea7dad76a287069fb4f931e5'
    client = oandapyV20.API(access_token=access_token)
    return client


def  Currency_Pairs():
    pairs = ['EUR_USD', 'EUR_CHF', 'EUR_GBP', 'EUR_JPY', 'EUR_AUD', 'USD_CAD', 'USD_CHF', 'USD_JPY', 'USD_MXN', 'GBP_CHF', 'GBP_JPY', 'GBP_USD', 'AUD_JPY', 'AUD_USD', 'CHF_JPY', 'NZD_JPY', 'NZD_USD', 'XAU_USD', 'EUR_CAD', 'AUD_CAD', 'CAD_JPY', 'EUR_NZD', 'GRX_EUR', 'NZD_CAD', 'SGD_JPY', 'USD_HKD', 'USD_NOK', 'USD_TRY', 'XAU_AUD', 'AUD_CHF', 'AUX_AUD', 'EUR_HUF', 'EUR_PLN', 'FRX_EUR', 'HKX_HKD', 'NZD_CHF', 'SPX_USD', 'USD_HUF', 'USD_PLN', 'USD_ZAR', 'XAU_CHF', 'ZAR_JPY', 'BCO_USD', 'ETX_EUR', 'CAD_CHF', 'EUR_DKK', 'EUR_NOK', 'EUR_TRY', 'GBP_CAD', 'NSX_USD', 'UKX_GBP', 'USD_DKK', 'USD_SGD', 'XAG_USD', 'XAU_GBP', 'EUR_CZK', 'EUR_SEK', 'GBP_AUD', 'GBP_NZD', 'JPX_JPY', 'UDX_USD', 'USD_CZK', 'USD_SEK', 'WTI_USD', 'XAU_EUR', 'AUD_NZD']
    stock = random.sample(pairs,1)
    return stock
    



def Format_Data(data,pair,SiMA,Bu,Bm,Bl,MoM5,TSF14,ADX,MIDPRICE5,MIDPRICE1,MIDPRICE3,TEMA):


    inc = 0
    dat = []
    for oo in data['candles']:
        dat.append([
        oo['time'], 
        oo['volume'], 
        oo['mid']['o'], 
        oo['mid']['h'], 
        oo['mid']['l'], 
        oo['mid']['c'],
        SiMA[inc],
        Bu[inc],
        Bm[inc],
        Bl[inc],
        MoM5[inc],
        TSF14[inc],
        ADX[inc],
        MIDPRICE5[inc],
        MIDPRICE1[inc],
        MIDPRICE3[inc],
        TEMA[inc]
        
        ])
        inc +=1
        #print(inc)
    df = pd.DataFrame(dat)
    df.columns = ['Time',
    'Volume', 
    'Open', 
    'High', 
    'Low', 'Close','SiMA','BolUp','BolMid','BolLow','Momentum',
    'TSF14','ADX','MIDPRICE5','MIDPRICE1','MIDPRICE3','TEMA']
    df['Time'] = pd.to_datetime(df['Time'])
    df['Time'] = df['Time'].dt.strftime('%Y-%m-%d %I:%M:%S')
    df['Time'] = pd.to_datetime(df['Time'])
    df = df.set_index('Time')
    graph(df)
    

    #output = talib.SMA(df['Close'])
    #output2 = talib.MOM(df['Close'], timeperiod=5)
    #print(output)
    #print(output2)
    pd.set_option('display.max_rows', 500)
    pd.set_option('display.max_columns', 500)
    pd.set_option('display.width', 1500)
    print(pair)
    #print(df)

    #graph(df)
    
    return df





def candleoptions():
    Candle_Sticks_Options = '''

    Name 	                Located         Type 	                Description

    Authorization 	        header 	        string 	                The authorization bearer token previously obtained by the client [required]
    Accept-Datetime-Format 	header          AcceptDatetimeFormat 	Format of DateTime fields in the request and response.
    instrument 	            path 	        InstrumentName 	        Name of the Instrument [required]
    price 	                query 	        PricingComponent 	    The Price component(s) to get candlestick data for. [default=M]
    granularity 	        query 	        CandlestickGranularity 	The granularity of the candlesticks to fetch [default=S5]
    count 	                query 	        integer 	            The number of candlesticks to return in the response. Count should not be specified if both the start and end parameters are provided, as the time range combined with the granularity will determine the number of candlesticks to return. [default=500, maximum=5000]
    from 	                query 	        DateTime 	            The start of the time range to fetch candlesticks for.
    to 	                    query 	        DateTime 	            The end of the time range to fetch candlesticks for.
    smooth 	                query 	        boolean 	            A flag that controls whether the candlestick is “smoothed” or not. A smoothed candlestick uses the previous candle’s close price as its open price, while an un-smoothed candlestick uses the first price from its time range as its open price. [default=False]
    includeFirst 	        query 	        boolean 	            A flag that controls whether the candlestick that is covered by the from time should be included in the results. This flag enables clients to use the timestamp of the last completed candlestick received to poll for future candlesticks but avoid receiving the previous candlestick repeatedly. [default=True]
    dailyAlignment 	        query 	        integer 	            The hour of the day (in the specified timezone) to use for granularities that have daily alignments. [default=17, minimum=0, maximum=23]
    alignmentTimezone 	    query 	        string 	                The timezone to use for the dailyAlignment parameter. Candlesticks with daily alignment will be aligned to the dailyAlignment hour within the alignmentTimezone. Note that the returned times will still be represented in UTC. [default=America/New_York]
    weeklyAlignment 	    query 	        WeeklyAlignment 	    The day of the week used for granularities that have weekly alignment. [default=Friday] 

    ##DATE TIME FORMATS
    d = timedelta(microseconds=-1)
    (d.days, d.seconds, d.microseconds)
    (-1, 86399, 999999)
    datetime.timedelta(days=0, seconds=86400, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0)
    '''
    #'key1': 'value1',
    #'key2': ['value2', 'value3'],
    #“12345678.000000123”


#### This makes the request to oanda
def Make_Request():
    client = Get_Account_Info()
    pair = Currency_Pairs()
    pair = pair[0]
    #print(pair,pair[0])
    #print(pair)

    params = {
        #"Accept-Datetime-Format":['unix','555.555'],   
        "count": 300,
        #"granularity":''
        }

    data = 'none'
    try:
        r = instruments.InstrumentsCandles(instrument=pair, params=params)
        data = client.request(r)
    except:
        print('That stock isnt supported')

    if data == 'none':
        Make_Request()

    return data,pair

def Calculate_100DayMovingAverage(data):
    MOVING_AVERAGE_DOC = '''
    The MA – or ‘simple moving average’ (SMA) – is an indicator used to identify the direction of a current price trend, 
    without the interference of shorter-term price spikes. 
    The MA indicator combines price points of a financial instrument over a specified time frame 
    and divides it by the number of data points to present a single trend line.
    The data used depends on the length of the MA. For example, a 200-day MA requires 200 days of data. 
    By using the MA indicator, 
    you can study levels of support and resistance and see previous price action (the history of the market). 
    This means you can also determine possible future patterns.
    '''

    numz = []
    Moving_Average_100 = []
    
    Time = []
    incr = 0
    for i in data['candles']:
        numz.append(float(i['mid']['c']))
        try:
            v = numz[numz.__len__()-100:]
            #print(numz[numz.__len__()-100:])
            a = math.fsum(v)
            MovAve = a/100.0
            #print(MovAve)
            #tyme  = i['mid']['Time'][inc]
            Moving_Average_100.append((MovAve))
            incr = incr + 1
            #print(incr, MovAve)
        except:
            +1
    ma100 = np.array(Moving_Average_100)
    MA100 = np.insert(ma100, 0, values=np.zeros(99))#, axis=0)
    Moving_Average_100 = MA100.tolist()
    #print(Moving_Average_100)
    return Moving_Average_100

def calcBOLBAND(data):
    close=[]
    for i in data['candles']:
        #print(i['mid']['c'])
        close.append(i['mid']['c'])
    closeA = np.array(close)
    closeB = pd.Series(closeA)    
    upper, middle, lower = talib.BBANDS(closeB, matype=MA_Type.T3)
    return upper,middle,lower

def calcSMA(data):
    close=[]
    for i in data['candles']:
        #print(i['mid']['c'])
        close.append(i['mid']['c'])
    closeA = np.array(close)
    closeB = pd.Series(closeA)
    output = talib.SMA(closeB)
    return output

def Calculate_ADX15(data):
    ADX_DOC = ''' 
         What is the Average Directional Index (ADX)?
        The average directional index (ADX) is a technical analysis indicator used by some traders 
        to determine the strength of a trend. 
        The trend can be either up or down, and this is shown by two accompanying indicators, 
        the Negative Directional Indicator (-DI) and the Positive Directional Indicator (+DI). 
        Therefore, ADX commonly includes three separate lines. 
        These are used to help assess whether a trade should be taken long or short, or if a trade should be taken at all.
        
                 
        Designed by Welles Wilder for commodity daily charts, but can be used in other markets or other timeframes.
        The price is moving up when +DI is above -DI, and the price is moving down when -DI is above +DI.
        Crosses between +DI and -DI are potential trading signals as bears or bulls gain the upper hand.
        The trend has strength when ADX is above 25. The trend is weak or the price is trendless when ADX is below 20, 
        according to Wilder.
        Non-trending doesn't mean the price isn't moving. 
        It may not be, but the price could also be making a trend change or is too volatile for a clear direction to be present.
        

        Calculating the Average Directional Movement Index (ADX)

        Calculate +DM, -DM, and True Range (TR) for each period. 14 periods are typically used.
        +DM = Current High - Previous High.
        -DM = Previous Low - Current Low.
        Use +DM when Current High - Previous High > Previous Low - Current Low. Use -DM when Previous Low - Current Low > Current High - Previous High.
        TR is the greater of the Current High - Current Low, Current High - Previous Close, or Current Low - Previous Close.
        Smooth the 14-period averages of +DM, -DM, and TR. The TR formula is below. Insert the -DM and +DM values to calculate the smoothed averages of those.
        First 14TR = Sum of first 14 TR readings.
        Next 14TR value = First 14TR - (Prior 14TR/14) + Current TR
        Next, divide the smoothed +DM value by the smoothed TR value to get +DI. Multiply by 100.
        Divide the smoothed -DM value by the smoothed TR value to get-DI. Multiply by 100.
        The Directional Movement Index (DX) is +DI minus -DI, divided by the sum of +DI and -DI (all absolute values). Multiply by 100.
        To get the ADX, continue to calculate DX values for at least 14 periods. Then, smoothe the results to get ADX
        First ADX = sum 14 periods of DX / 14
        After that, ADX = ((Prior ADX * 13) + Current DX) /14

        ADX LINE = STRENGTH OF A TREND
        PDI = POSITIVE TREND OR NEGATIVE TREND
        3 Crossover markes a buy or sell point
        ADX = 100x(14EMA(abs(PDI-NDI)/(PDI+NDI)))

        
        '''
    numz = []
    ADX15 = []
    Time = []
    incr = 0
    #for i in data['candles']:
    #    print(i['mid'])
    for i in data['candles']:
        numz.append(float(i['mid']['c']))
        #print(numz)
        #input()
        incr +=1
    return ADX15
    

def calcMoM5(data):
    close=[]
    for i in data['candles']:
        #print(i['mid']['c'])
        close.append(i['mid']['c'])
    closeA = np.array(close)
    closeB = pd.Series(closeA)


    MOM5 = talib.MOM(closeB, timeperiod=5)
    return MOM5
def calcTSF14(data):
    close=[]
    for i in data['candles']:
        #print(i['mid']['c'])
        close.append(i['mid']['c'])
    closeA = np.array(close)
    closeB = pd.Series(closeA)
    real = TSF(closeB, timeperiod=14)
    return real
def calcADX(data):
    high=[]
    low=[]
    close=[]
    for i in data['candles']:
        #print(i['mid']['c'])
        high.append(i['mid']['h'])
        low.append(i['mid']['l'])
        close.append(i['mid']['c'])
        

    highA = np.array(high)
    highB = pd.Series(highA)
    lowA = np.array(low)
    lowB = pd.Series(lowA)
    closeA = np.array(close)
    closeB = pd.Series(closeA)


    real = ADX(highB, lowB, closeB, timeperiod=14)
    return real


def calcTEMA(data):
    close=[]
    for i in data['candles']:
        #print(i['mid']['c'])
        close.append(i['mid']['c'])
    closeA = np.array(close)
    closeB = pd.Series(closeA)
    real = TEMA(closeB, timeperiod=30)
    return real
    
def calcMIDPRICE5(data):
    high=[]
    low=[]
    for i in data['candles']:
        high.append(i['mid']['h'])
        low.append(i['mid']['l'])

    lowA = np.array(low)
    lowB = pd.Series(lowA)
    highA = np.array(high)
    highB = pd.Series(highA)
    real = MIDPRICE(highB, lowB, timeperiod=50)

    return real


def calcMIDPRICE1(data):
    high=[]
    low=[]
    for i in data['candles']:
        high.append(i['mid']['h'])
        low.append(i['mid']['l'])

    lowA = np.array(low)
    lowB = pd.Series(lowA)
    highA = np.array(high)
    highB = pd.Series(highA)
    real = MIDPRICE(highB, lowB, timeperiod=100)

    return real


def calcMIDPRICE3(data):
    high=[]
    low=[]
    for i in data['candles']:
        high.append(i['mid']['h'])
        low.append(i['mid']['l'])

    lowA = np.array(low)
    lowB = pd.Series(lowA)
    highA = np.array(high)
    highB = pd.Series(highA)
    real = MIDPRICE(highB, lowB, timeperiod=300)

    return real

def graph2(df):
    df.fillna(df.mean(), inplace=True)
    #df.fillna(df.zeros)
    print(df)
    df.plot()
    plt.show()






    df['Upper'] = df['Close'] + 2*(df['Close'].rolling(20).std())
    df.rolling(window=70).mean()['High'].plot()
    plt.figure(figsize=(10,10))
    
    plt.plot(df['TSF14'], 'o--', label="TSF14")

    plt.plot(df['upper'], 'g--', label="upper")
    plt.plot(df['BolMid'], 'r--', label="middle")
    plt.plot(df['BolLow'], 'y--', label="lower")
    plt.plot(df['SiMA'], 'y--', label="Sima")
    plt.plot(df['Close'], 'r-',label="Close")
    
    plt.plot(df['Momentum'], 'o--',label = 'Momentum')
    plt.plot(df['ADX'], 'b--',label = 'ADX')
    
    plt.xlabel("Time")
    plt.ylabel("Price")
    plt.title("Cool Data Plot")
    plt.legend()
    plt.show()
    ## LEFT BOTTOW WIDTH HIEGHT
    fig,axes = plt.subplots(nrows=3,ncols=1)
    axes[0].plot(df['Close'])
    axes[1].plot(df['Close'])
    axes[1].plot(df['Volume'])
    axes[2].plot(df['ADX'])

    #ax2.set_xlim\sety_lim
    plt.subplot(3,1,1)
    plt.plot(df['BolUp'])
    plt.plot(df['BolMid'])
    plt.plot(df['BolLow'])

    plt.subplot(3,1,2)
    plt.plot(df['Close'])
    plt.plot(df['Volume'])

    plt.subplot(3,1,3)
    plt.plot(df['ADX'])


    fig,ax = plt.subplots()
    ax.plot_date

    plt.show()


def graph(df):
    #df  = sm.datasets.macrodata.load_pandas().data
    #print(sm.datasets.macrodata.NOTE)
    #hp_cycle, hp_trend = sm.tsa.filters.hpfilter(endog, lamb=129600)
    df.plot()
    plt.show()

    #print(df.head())
    #df['Close'].plot()
    #gdpcycle, gdptrend = sm.tsa.filters.hpfilter(df['Close'])
   # type(result)
    #df['trend'] = gdptrend
    #df['trend'].plot()
    #plt.subplots()
    #plt.show()


def Flow():
    data,pair = Make_Request()
    #MA100 = Calculate_100DayMovingAverage(data)
    SiMA = calcSMA(data)
    Bu,Bm,Bl = calcBOLBAND(data)
    MoM5 = calcMoM5(data)
    TSF14 = calcTSF14(data) 
    ADX = calcADX(data)
    MIDPRICE5 = calcMIDPRICE5(data)
    MIDPRICE1 = calcMIDPRICE1(data)
    MIDPRICE3 = calcMIDPRICE3(data)
    TEMA = calcTEMA(data)
    
    Format_Data(data,pair,SiMA,Bu,Bm,Bl,MoM5,TSF14,ADX,MIDPRICE5,MIDPRICE1,MIDPRICE3,TEMA)
    #graph(df)
    
    
  


##########  RUN
Flow()
