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
import ta
import math

########## GLOBALS





########## FUNCTIONS
def Flow():
    Format_Data()

#### This uses my account information to give to the request
def Get_Api_Key():
    access_token = ''
    return access_token

def Get_AccountId():
    accountID = ''
    return accountID

def Get_Account_Info():
    api_key = ''
    client = oandapyV20.API(access_token=api_key)
    return client


def  Currency_Pairs():
    pairs = ['EUR_USD', 'EUR_CHF', 'EUR_GBP', 'EUR_JPY', 'EUR_AUD', 'USD_CAD', 'USD_CHF', 'USD_JPY', 'USD_MXN', 'GBP_CHF', 'GBP_JPY', 'GBP_USD', 'AUD_JPY', 'AUD_USD', 'CHF_JPY', 'NZD_JPY', 'NZD_USD', 'XAU_USD', 'EUR_CAD', 'AUD_CAD', 'CAD_JPY', 'EUR_NZD', 'GRX_EUR', 'NZD_CAD', 'SGD_JPY', 'USD_HKD', 'USD_NOK', 'USD_TRY', 'XAU_AUD', 'AUD_CHF', 'AUX_AUD', 'EUR_HUF', 'EUR_PLN', 'FRX_EUR', 'HKX_HKD', 'NZD_CHF', 'SPX_USD', 'USD_HUF', 'USD_PLN', 'USD_ZAR', 'XAU_CHF', 'ZAR_JPY', 'BCO_USD', 'ETX_EUR', 'CAD_CHF', 'EUR_DKK', 'EUR_NOK', 'EUR_TRY', 'GBP_CAD', 'NSX_USD', 'UKX_GBP', 'USD_DKK', 'USD_SGD', 'XAG_USD', 'XAU_GBP', 'EUR_CZK', 'EUR_SEK', 'GBP_AUD', 'GBP_NZD', 'JPX_JPY', 'UDX_USD', 'USD_CZK', 'USD_SEK', 'WTI_USD', 'XAU_EUR', 'AUD_NZD']
    stock = random.sample(pairs,1)
    return stock
    



def Format_Data(data,MA100,ADX15):

    #print(data)
    #print(MA100)
    inc = 0
    dat = []
    for oo in data['candles']:
        dat.append([oo['time'], oo['volume'], oo['mid']['o'], oo['mid']['h'], oo['mid']['l'], oo['mid']['c'], MA100[inc]])
        inc +=1
        #print(inc)
    df = pd.DataFrame(dat)
    df.columns = ['Time', 'Volume', 'Open', 'High', 'Low', 'Close','MA100']
    df = df.set_index('Time')
    print(df.head(200))
    return df


def Get_Historical_Data():
    client = Get_Account_Info()
    data = oanda.get_history(instrument='ZAR_USD',  # our instrument
                         start='2016-12-08',  # start data
                         end='2016-12-10',  # end date
                         granularity='M1')  # minute bars  # 7

def Get_Oanda_Account_Info():
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer d5698e5908e8b7989f50c40bac0f1c53-6fbc07c1ea7dad76a287069fb4f931e5',
    }

    response = requests.get('https://api-fxpractice.oanda.com/v3/accounts', headers=headers)

    print(response.text, response.content)

def Get_Account_Summary():

    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer d5698e5908e8b7989f50c40bac0f1c53-6fbc07c1ea7dad76a287069fb4f931e5',
    }

    response = requests.get('https://api-fxpractice.oanda.com/v3/accounts/101-001-14704433-001/summary', headers=headers)
    print(response)

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
    print(pair)

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
    
    return data

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
            #print('not long enuf yet')
    #df = Create_DF_Column(Moving_Average_100)
    ma100 = np.array(Moving_Average_100)
    MA100 = np.insert(ma100, 0, values=np.zeros(99))#, axis=0)
    Moving_Average_100 = MA100.tolist()
    #print(Moving_Average_100)
    return Moving_Average_100

def Create_DF_Column(data):
    +1
    ma100 = np.array(data)
    ma100 = np.insert(ma100, 0, values=np.zeros(100))#, axis=0)
    #print(ma100)
    #print(type(ma100))
    dfma100 = pd.Series(ma100)
    df = pd.DataFrame(dfma100)
    #df.columns = ['MA100']
    df['MA100'] = df
    #print(dfma100['MA100'].head(104))
    print(df)
    return df
    



    +1
    #print(df,df_100MA)
    #print(len(df['Time']))
    #df['MA100'] = df['Volume'] + df['Open'] + df['High'] + df['Low'] + df['Close'] + df_100MA['MA100']
    #print(df)

def Calculate_ADX15(data):
    +1
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
    
def TR(d,c,h,l,o,yc):
    x=h-l
    y=abs(h-yc)
    z=abs(l-yc)

    if y <= x >=z:
        TR = x
    elif x <= y >=z:
        TR = y
    elif x<=z>=y:
        TR = z
    return d, TR

def DM(d,o,h,l,c,yo,yh,yl,yc):
    moveUp = h -yh
    moveDown = yl - l
    if 0 < moveUp > moveDown:
        PDM = moveUp
    else:
        PDM = 0
    if 0 < moveDown > moveUp:
        NDM = moveDown
    else:
        NDM = 0
    return d,PDM,NDM

def ExpMovingAverage(values,window):
    weights = np.exp(np.linspace(-1.,0., window))
    weights /= weights.sum()
    a = np.convolve(values,weights, mode='full')[:len(values)]
    a[:window] = a[window]


def Add_Indicators():
    data = Make_Request()
    MA100 = Calculate_100DayMovingAverage(data)
    ADX15 = Calculate_ADX15(data)
    df = Format_Data(data,MA100,ADX15)
    
    
  
    
  


##########  RUN
#Flow()
Add_Indicators()

#a = ['5.824', '5.822', '5.820', '5.818', '5.818', '5.817', '5.818', '5.820', '5.822', '5.822']
#b = math.fsum(float(a))
#print(b)