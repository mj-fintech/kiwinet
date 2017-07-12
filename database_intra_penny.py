'''
axonXaxon Database #intra #penny
'''
import pandas as pd
import pymysql

# Penny stock screener: Inputs a company ticker and outputs "False" or "True"
# If the last sale price was less than $5.00, then we assign the stock as "Penny"
# else it is not a "Penny"

# 1. Check the price of all stocks #

# 2. Make a list of Pennys #


def isPenny(ticker):

    if :

        return False

    else:

        return True

def penny_stock_list():

    ticker_list = ['aapl', 'goog', 'msft', ....]
    penny_list = []
    for ticker in ticker_list:
        if isPenny(ticker) == 'True':
            penny_list.append(ticker)
    return penny_list

# 3. database work. Dynamically parse the Google Finance API and store data to
# the MySQL database.
