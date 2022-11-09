#yahoo-finance-Getting-Historical-Data

import warnings
warnings.simplefilter('ignore')

try:
  import yfinance
except:
  !pip install -q yfinance
  import yfinance

import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

import datetime
from datetime import date, timedelta
import numpy as np

# df = yf.download("SPY", start = date.today() - timedelta(days = 365*10), end=date.today(), progress=false, )

spyticker = yf.Ticker("SPY")
df = spyticker.history(period="max", interval="1d", start=date.today() - timedelta(days = 365*10), end=date.today())

df = df.dropna()

print (df.head())

df.plot(y='High')
#=================

#=================

# Basic Metrics Analysis 1 : Return Analysis
df['Returns'] = df['Open'].shift(-1) / df['Open']

# Mean an Std.dev of Return
mean_returns = df['Returns'].mean()

#  0.04%     print 1.0005307195239594 
print(mean_returns)

std_dev = df['Returns'].std()

#0 and 1.04%
print("Mean Return of SPY + 1Std.dev: ",mean_returns + std_dev) 

#0 and 0.990%
print("Mean Return of SPY + 1Std.dev: ",mean_returns - std_dev)
#=================
# 1.0005307194912998
# Mean Return of SPY + 1Std.dev:  1.0108527248037755
# Mean Return of SPY + 1Std.dev:  0.990208714178824
#=================


#advance Plot
plt.figure(figsize=(15,8))
plt.title('Analysis of SPY Returns')
plt.plot(df['Returns'], color="black", label="Percentage Returns")
plt.axhline(y=mean_returns + (std_dev*2), color='red', linestyle='-')
plt.axhline(y=mean_returns + (std_dev*1), color='red', linestyle='-')
plt.axhline(y=mean_returns - (std_dev*1), color='red', linestyle='-')
plt.axhline(y=mean_returns - (std_dev*2), color='red', linestyle='-')
plt.legend(loc='upper left')
plt.grid()
plt.show()

