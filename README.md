##### Main Objective
#	Creating a Stock Trading Bot
#####

##### GITHUB TUTORIAL 
#	https://product.hubspot.com/blog/git-and-github-tutorial-for-beginners
#####

##### THIS IS OUR STOCK TRADING PLATFORM 
#	http://developer.oanda.com/
#	1. Get an account
#	2. Get an Api-Key
####

#### USE THE OANDA API
#	1. Python Setup
#	2. Api Docs
#
#

############################### DATA 
##### Objective: Create the programing that downloads the data needed for prediction.
########  Find Data Source for instrument information
###   What is the data source for the program?
# 1. Oanda
### Download the data needed to make a prediction.
# 2. GetData.py
#       Downloads the information from a random instrument

######## Add Indicators to the stock data
### What indicators do you plan on using to add to the data.
# 1. Pick indicators 
        32 indicators
Volume

    Accumulation/Distribution Index (ADI)
    On-Balance Volume (OBV)
    On-Balance Volume mean (OBV mean)
    Chaikin Money Flow (CMF)
    Force Index (FI)
    Ease of Movement (EoM, EMV)
    Volume-price Trend (VPT)
    Negative Volume Index (NVI)

Volatility

    Average True Range (ATR)
    Bollinger Bands (BB)
    Keltner Channel (KC)
    Donchian Channel (DC)

Trend

    Moving Average Convergence Divergence (MACD)
    Average Directional Movement Index (ADX)
    Vortex Indicator (VI)
    Trix (TRIX)
    Mass Index (MI)
    Commodity Channel Index (CCI)
    Detrended Price Oscillator (DPO)
    KST Oscillator (KST)
    Ichimoku Kinkō Hyō (Ichimoku)

Momentum

    Money Flow Index (MFI)
    Relative Strength Index (RSI)
    True strength index (TSI)
    Ultimate Oscillator (UO)
    Stochastic Oscillator (SR)
    Williams %R (WR)
    Awesome Oscillator (AO)

Others

    Daily Return (DR)
    Cumulative Return (CR)
    
# 2. How do you calculate each indicator?
#      https://github.com/bukosabino/ta
#       Learn this python library in order to convert panda data frames to have the inidcators created.
# 3. Calculate Indicators to an Instrument
#       Code...

######## Make the pandas data frame and do scaling
# 1. Scale the data


############################### Prediction Model
##### Objective: Create the model that can use multiple inputs to predict a single price.
#


################################ STRATEGY
##### Objective: Create the programming that will choose a position to enter
######## One Indicator
# 1. Trending Check
#       Use the indicators that define 'Trendyness'
# 2. Shorting Stock
#       
# 3. Long Position
# 4. Stop Losses



