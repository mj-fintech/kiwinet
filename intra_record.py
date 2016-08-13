# -*- coding: utf-8 -*-
"""
@author: MJ
"""
import urllib
import pandas as pd


def intra_stock_df(symbol, interval):
	
	f = urllib.urlopen("http://www.google.com/finance/getprices?q="+symbol+"&i="+interval+"&p=d&f=d,o,h,l,c,v").read().split("\n")[7:-1]
	data = []
	for i in range(len(f)):
		data.append(f[i].split(","))
	
	pre_DATE = [data[i][0] for i in range(len(f))]
	DATE = [int(pre_DATE[0][1:]) + int(pre_DATE[i])*int(interval) for i in range(1,len(f))]
	DATE.insert(0, int(pre_DATE[0][1:]))
	CLOSE = [float(data[i][1]) for i in range(len(f))]
	HIGH = [float(data[i][2]) for i in range(len(f))]
	LOW = [float(data[i][3]) for i in range(len(f))]
	OPEN = [float(data[i][4]) for i in range(len(f))]
	VOLUME = [float(data[i][5]) for i in range(len(f))]
	
	df = pd.DataFrame({"DATE":DATE, "CLOSE":CLOSE, "HIGH":HIGH, "LOW":LOW, "OPEN":OPEN, "VOLUME":VOLUME}).set_index("DATE")
	
	return df
