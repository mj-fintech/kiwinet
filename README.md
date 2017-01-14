# Intraday_Record
Pulling Intraday Price and Volume Data from Google Finance

# What it does?
This Python code is to pulling the intraday stock price and volume data from Google Finance. 
The function parses the Google Finance and build a DataFrame of the data. Data length varies depending on the interval (time difference between two records) you set, 
but the minimum interval is 60 seconds. I suggest you to use either 60 or 120 intervals for the data accuracy. 

# Example of usage

<code>>> intra_stock_df("AAPL", "120")</code>
<code>>> intra_aft_df("AAPL", "120")</code>

This will give you a Pandas dataframe with UNIX Timestamp, Close, High, Low, Open, Volume records of "Apple. Inc" in the interval of 2 minutes of the one whole day up until the time when you run this code. And the second commend will give you the after market records.

# For extracting longer day records

I suggest to create a empty panda DataFrame first with a base-index that might be the time-frame that covers the longest available time, because some records have missing data, and we want to take care of it.

If you have a list of Symbols you want to extract the data for:


<code>Data = pd.DataFrame(index=base_index)
error = []
for i in symbol_list:
	try:
		Data[i] = intra_stock_df_longerdays(i,"60","14")['CLOSE']
		print i + " record has been parsed"
	
	except Exception as e:
		print i + " ------------------------- " +str(e)		
		error.append(i)		
		
	Data = Data.fillna(method='ffill')
	Data = Data.fillna(method='bfill')
	Data.to_csv("Data.csv")</code>
