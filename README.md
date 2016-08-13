# Intraday_Record
Pulling Intraday Price and Volume Data from Google Finance

# What it does?
This Python code is to pulling the intraday stock price and volume data from Google Finance. 
The function parses the Google Finance and build a DataFrame of the data. Data length varies depending on the interval (time difference between two records) you set, 
but the minimum interval is 60 seconds. I suggest you to only use either 60 or 120 intervals for the data accuracy.

# Example of usage

<code>>> intra_stock_df("AAPL", "120")</code>

This will give you a Pandas dataframe with UNIX Timestamp, Close, High, Low, Open, Volume records of "Apple. Inc" in the interval of 2 minutes of the one whole day up until the time when you run this code.

