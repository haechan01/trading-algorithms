# Trading algorithms based on technical indicators and sentiment analysis

The main codes are in 'final.ipynb' file. 'constituents.csv' file has stock symbols of S&P500 companies. Using the symbols, we retrieve data from yahoo finance. 


## strategies
There are three strategies based on technical indicators: MACD (moving average convergence divergence), RSI (relative strenth index), and bollinger band. 
More information about the indicators: MACD (https://www.investopedia.com/articles/forex/05/macddiverge.asp)
RSI (https://www.investopedia.com/terms/r/rsi.asp)
Bollinger band (https://www.investopedia.com/terms/b/bollingerbands.asp)
Breakout strategy is a momentum-based strategy developed by Larry Williams, where we buy when the price increase more than certain percentage of yesterday's vollatility. (https://www.traderslog.com/volatility-breakout-systems)
MACD-breakout strategy combines MACD and vollatility breakout strategy. It buys when there is an upward divergence in MACD or when there is a breakout signal, and sells when there is downward diveregence in MACD. 

## backtesting
We calculate how much profit the strategies would have made given a stock and time range through a backtesting simulation based on the stock's historical data. 
We compare the results by visualizing the profits in line graph. Also, we randomly sample 50 stocks from S&P 500, select a random range of time between 2012 and 2022, and calculate the average profit of the strategies.
The average profit is compared using bar graph, and calculating p-value can indicate whether the differences in means are statistically significant. 

## Bullish and bearish market
The function 'bullish_bearish' finds bullish and bearish period of length k, given an array of price changes. We compare the strategies in bullish and bearish periods, and find out that the strategies outperform the benchmark (buy-and-hold strategy) in a bearish market, but not as profitable in a bullish market. 

## Sentiment analysis
To conduct a sentiment analysis of a stock, we get news titles from Google using GoogleNews(https://github.com/Iceloof/GoogleNews). After we do natural language processing of the title texts, we get the polarity scores of the titles usign NLTK. 

# Application of sentiment analysis in trading
sentiment_strategy is a simple trading strategy that buys a stock when sentiment is positive and sells when the sentiment is bad. 
We categorize monthly sentiments into 5 different categories: extremely negative, negative, neutral, positive, and extremely positive. 
Then, we compare the performances of the strategies in the 5 different sentiment categories. 



