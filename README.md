# Trading Algorithms with Technical Indicators and Sentiment Analysis

This repository implements trading algorithms based on technical indicators and sentiment analysis. It evaluates and executes strategies using historical stock data from Yahoo Finance, and real-time sentiment insights from news sources.

## Key Files
- **final.ipynb**: Contains the main code for strategies, backtesting, and performance visualizations.
- **constituents.csv**: Lists S&P500 stock symbols for retrieving data.

## Strategies

### 1. **Technical Indicator Strategies**
   - **MACD (Moving Average Convergence Divergence)**: Measures momentum through divergences in moving averages ([Learn more](https://www.investopedia.com/articles/forex/05/macddiverge.asp)).
   - **RSI (Relative Strength Index)**: Identifies overbought/oversold conditions ([Learn more](https://www.investopedia.com/terms/r/rsi.asp)).
   - **Bollinger Bands**: Highlights price volatility using bands ([Learn more](https://www.investopedia.com/terms/b/bollingerbands.asp)).
   - **Breakout Strategy**: A momentum-based strategy that buys on price increases beyond a volatility threshold ([Learn more](https://www.traderslog.com/volatility-breakout-systems)).
   - **MACD-Breakout**: Combines MACD signals with breakout patterns for trading decisions.

### 2. **Backtesting**
   - Simulates historical performance of strategies using stock data.
   - Visualizes profit/loss results and calculates:
     - **Win rate**: Proportion of profitable trades.
     - **Maximum Drawdown (MDD)**: Largest observed loss from a peak.

### 3. **Market Conditions**
   - The `bullish_bearish` function classifies market conditions.
   - Strategies are compared during **bullish** and **bearish** periods, with findings indicating outperformance in bearish markets compared to a simple buy-and-hold strategy.

### 4. **Sentiment Analysis**
   - Retrieves news headlines using GoogleNews ([Library](https://github.com/Iceloof/GoogleNews)).
   - Analyzes sentiment polarity using NLP (Natural Language Processing) with NLTK.
   - Implements a **sentiment strategy**: Buys stocks with positive sentiment and sells on negative sentiment.
   - Categorizes sentiment into five levels: extremely negative, negative, neutral, positive, and extremely positive.

## Performance Evaluation
- Strategy performance is visualized using line and bar graphs.
- **p-values** are calculated to determine statistical significance between strategy returns.
- Comparison of strategy performance across different sentiment categories and market conditions helps assess overall effectiveness.
