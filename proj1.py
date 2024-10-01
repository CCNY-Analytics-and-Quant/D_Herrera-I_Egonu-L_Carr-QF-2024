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

# Calculate 52-week rolling high and low
weekly_high = data['Adj Close'].rolling(window=252).max()
weekly_low = data['Adj Close'].rolling(window=252).min()

# Calculate weekly drawdown
weekly_drawdown = (weekly_low - weekly_high) / weekly_high

# Average weekly drawdown
average_weekly_drawdown = weekly_drawdown.mean()
print("Average Weekly Drawdown:", average_weekly_drawdown)

# Maximum weekly drawdown
max_weekly_drawdown = weekly_drawdown.min()
print("Maximum Weekly Drawdown:", max_weekly_drawdown)

# Calculate total return over 10 years
start_price = data['Adj Close'].iloc[0]  # Starting price 10 years ago
end_price = data['Adj Close'].iloc[-1]  # Current price

total_return = (end_price / start_price) - 1
print("Total Return:", total_return)

# Number of trading days in 10 years (approx. 252 trading days per year)
years = 10

# Calculate annualized total return
annualized_return = (end_price / start_price) ** (1 / years) - 1
print("Annualized Return:", annualized_return)

# Assuming 'tickers' contains your assets and 'benchmarks' contains your ETFs
all_tickers = tickers + benchmarks

# Calculate percentage changes for each asset
returns = data[all_tickers].pct_change()

# Calculate the correlation matrix
correlation_matrix = returns.corr()

# Display the correlation matrix
print(correlation_matrix)
