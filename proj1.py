import pandas as pd
import datetime as dt
import yfinance as yf

assets = ['AAPL','TSLA','NVDA','K','CRSP','NEM','PLTR']
benchmarks = ['spy']
tickers = assets + benchmarks

startdate = '2009-09-18'
enddate = '2019-09-18'

data = yf.download(tickers, start=startdate, end=enddate)['Adj Close']

data.head(10) 

spy = data[benchmarks]
spy['old'] = spy.shift(252) 
old = spy.SPY.shift()
spy['change'] = (spy.SPY - old) / old

spy_returns = data[benchmarks].pct_change()
spy_returns.head()

spy.change / spy.old

metrics[]
riskfree = ((3.79**(1/252))-1)

for ticker in benchmarks:
    # Correlation
    correlation = spy['assets'].corr(spy_returns[ticker])
    
    # Covariance
    covariance = spy['assets'].cov(spy_returns[ticker])
    
    # Tracking error (standard deviation of the difference between portfolio and ETF returns)
    track_err = np.sqrt(((spy['assets'] - spy[ticker]) ** 2).mean())
    
    # Sharpe ratio (mean excess return divided by portfolio volatility)
    excessreturns = spy['assets'].mean() - riskfree / 252  # Adjust risk-free rate for daily returns
    portfoliovol = spy['assets'].std()
    sharpe_ratio = excessreturns / portfoliovol
    
    # Annualized volatility spread (portfolio volatility - ETF volatility)
    annualvol = portfoliovol * np.sqrt(252)
    tick_annualvol = spy_returns[ticker].std() * np.sqrt(252)
    volatility_spread = portfoliovol - annualvol
    
    metrics.append([ticker, correlation, covariance, track_err, sharpe_ratio, volatility_spread])