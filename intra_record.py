# -*- coding: utf-8 -*-
"""
@author: MJ KIM
"""
import urllib
import pandas as pd

## During Market Records ##
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

## After Market Record ##
def intra_aft_df(symbol, interval):

	f = urllib.urlopen("http://www.google.com/finance/getprices?q="+symbol+"&i="+interval+"&p=d&f=d,o,h,l,c,v&sessions=ext_hours").read().split("\n")[8:-1]
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

# This is for extracting intraday records for longer days #
def intra_stock_df_longerdays(symbol, interval, days):

	f = urllib.urlopen("http://www.google.com/finance/getprices?q="+symbol+"&i="+interval+"&p="+days+"d&f=d,o,h,l,c,v").read().split("\n")[7:-1]
	#f = urllib.urlopen("http://www.google.com/finance/getprices?q=AAPL&i=60&p=14d&f=d,o,h,l,c,v").read().split("\n")[7:-1]
	data = []
	for i in range(len(f)):
		data.append(f[i].split(","))

	pre_DATE = [data[i][0] for i in range(len(f))]

	for i in range(len(pre_DATE)):
		if len(pre_DATE[i]) > 8:
			pre_DATE[i] = pre_DATE[i][1:]

	k = []
	for i in range(len(pre_DATE)):
		if len(pre_DATE[i]) > 8:
			k.append(i)

	DATE_1 = [int(pre_DATE[k[0]:k[1]][0]) + int(pre_DATE[k[0]:k[1]][i])*int(interval) for i in range(1,int(k[1])-int(k[0]))]
	DATE_1.insert(0, int(pre_DATE[k[0]:k[1]][0]))

	DATE_2 = [int(pre_DATE[k[1]:k[2]][0]) + int(pre_DATE[k[1]:k[2]][i])*int(interval) for i in range(1,int(k[2])-int(k[1]))]
	DATE_2.insert(0, int(pre_DATE[k[1]:k[2]][0]))

	DATE_3 = [int(pre_DATE[k[2]:k[3]][0]) + int(pre_DATE[k[2]:k[3]][i])*int(interval) for i in range(1,int(k[3])-int(k[2]))]
	DATE_3.insert(0, int(pre_DATE[k[2]:k[3]][0]))

	DATE_4 = [int(pre_DATE[k[3]:k[4]][0]) + int(pre_DATE[k[3]:k[4]][i])*int(interval) for i in range(1,int(k[4])-int(k[3]))]
	DATE_4.insert(0, int(pre_DATE[k[3]:k[4]][0]))

	DATE_5 = [int(pre_DATE[k[4]:k[5]][0]) + int(pre_DATE[k[4]:k[5]][i])*int(interval) for i in range(1,int(k[5])-int(k[4]))]
	DATE_5.insert(0, int(pre_DATE[k[4]:k[5]][0]))

	DATE_6 = [int(pre_DATE[k[5]:k[6]][0]) + int(pre_DATE[k[5]:k[6]][i])*int(interval) for i in range(1,int(k[6])-int(k[5]))]
	DATE_6.insert(0, int(pre_DATE[k[5]:k[6]][0]))

	DATE_7 = [int(pre_DATE[k[6]:k[7]][0]) + int(pre_DATE[k[6]:k[7]][i])*int(interval) for i in range(1,int(k[7])-int(k[6]))]
	DATE_7.insert(0, int(pre_DATE[k[6]:k[7]][0]))

	DATE_8 = [int(pre_DATE[k[7]:k[8]][0]) + int(pre_DATE[k[7]:k[8]][i])*int(interval) for i in range(1,int(k[8])-int(k[7]))]
	DATE_8.insert(0, int(pre_DATE[k[7]:k[8]][0]))

	DATE_9 = [int(pre_DATE[k[8]:k[9]][0]) + int(pre_DATE[k[8]:k[9]][i])*int(interval) for i in range(1,int(k[9])-int(k[8]))]
	DATE_9.insert(0, int(pre_DATE[k[8]:k[9]][0]))

	DATE_10 = [int(pre_DATE[k[9]:k[10]][0]) + int(pre_DATE[k[9]:k[10]][i])*int(interval) for i in range(1,int(k[10])-int(k[9]))]
	DATE_10.insert(0, int(pre_DATE[k[9]:k[10]][0]))

	DATE_11 = [int(pre_DATE[k[10]:k[11]][0]) + int(pre_DATE[k[10]:k[11]][i])*int(interval) for i in range(1,int(k[11])-int(k[10]))]
	DATE_11.insert(0, int(pre_DATE[k[10]:k[11]][0]))

	DATE_12 = [int(pre_DATE[k[11]:k[12]][0]) + int(pre_DATE[k[11]:k[12]][i])*int(interval) for i in range(1,int(k[12])-int(k[11]))]
	DATE_12.insert(0, int(pre_DATE[k[11]:k[12]][0]))

	DATE_13 = [int(pre_DATE[k[12]:k[12]+(len(f)-k[12])][0]) + int(pre_DATE[k[12]:k[12]+(len(f)-k[12])][i])*int(interval) for i in range(1,int(k[12]+len(f)-k[12])-int(k[12]))]
	DATE_13.insert(0, int(pre_DATE[k[12]:k[12]+len(f)-k[12]][0]))


	DATE = DATE_1 + DATE_2 + DATE_3 + DATE_4 + DATE_5 + DATE_6 + DATE_7 + DATE_8 + DATE_9 + DATE_10 + DATE_11 + DATE_12 + DATE_13
	CLOSE = [float(data[i][1]) for i in range(len(DATE))]
	HIGH = [float(data[i][2]) for i in range(len(DATE))]
	LOW = [float(data[i][3]) for i in range(len(DATE))]
	OPEN = [float(data[i][4]) for i in range(len(DATE))]
	VOLUME = [float(data[i][5]) for i in range(len(DATE))]

	df = pd.DataFrame({"DATE":DATE, "CLOSE":CLOSE, "HIGH":HIGH, "LOW":LOW, "OPEN":OPEN, "VOLUME":VOLUME}).set_index("DATE")

	return df
