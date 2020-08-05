"""Data models."""
from . import db

if __name__ == '__main__':
    updateData()

import pandas as pd
import io
import json
from datetime import datetime as dt
import math
#from .models import *
from requests import ReadTimeout, ConnectTimeout, HTTPError, Timeout, ConnectionError
import time

def init_app(app):
    # add multiple commands in a bulk
    app.cli.add_command(app.cli.command()(updateData))

def updateData():
    
    tickerToLinkDict = {"ARKK": "https://ark-funds.com/wp-content/fundsiteliterature/csv/ARK_INNOVATION_ETF_ARKK_HOLDINGS.csv", "ARKQ": "https://ark-funds.com/wp-content/fundsiteliterature/csv/ARK_AUTONOMOUS_TECHNOLOGY_&_ROBOTICS_ETF_ARKQ_HOLDINGS.csv", "ARKG": "https://ark-funds.com/wp-content/fundsiteliterature/csv/ARK_GENOMIC_REVOLUTION_MULTISECTOR_ETF_ARKG_HOLDINGS.csv", "ARKF" : "https://ark-funds.com/wp-content/fundsiteliterature/csv/ARK_FINTECH_INNOVATION_ETF_ARKF_HOLDINGS.csv", "ARKW" :"https://ark-funds.com/wp-content/fundsiteliterature/csv/ARK_NEXT_GENERATION_INTERNET_ETF_ARKW_HOLDINGS.csv" , "PRINT":"https://ark-funds.com/wp-content/fundsiteliterature/csv/THE_3D_PRINTING_ETF_PRNT_HOLDINGS.csv", "IZRL":"https://ark-funds.com/wp-content/fundsiteliterature/csv/ARK_ISRAEL_INNOVATIVE_TECHNOLOGY_ETF_IZRL_HOLDINGS.csv" }
    
    putDataInDB(ArkkTable, "ARKK", tickerToLinkDict)
    ArkkHoldings = ArkkTable.query.all()
    
    putDataInDB(ArkqTable, "ARKQ", tickerToLinkDict)
    ArkqHoldings = ArkqTable.query.all()
    
    putDataInDB(ArkgTable, "ARKG", tickerToLinkDict)
    ArkgHoldings = ArkgTable.query.all()
    
    putDataInDB(ArkfTable, "ARKF", tickerToLinkDict)
    ArkfHoldings = ArkfTable.query.all()
    
    putDataInDB(ArkwTable, "ARKW", tickerToLinkDict)
    ArkwHoldings = ArkwTable.query.all()
    
    putDataInDB(PrintTable, "PRINT", tickerToLinkDict)
    PRINTHoldings = PrintTable.query.all()
    
    putDataInDB(IzrlTable, "IZRL", tickerToLinkDict)
    IZRLHoldings = IzrlTable.query.all()
    
    return [ArkkHoldings,ArkqHoldings, ArkgHoldings, ArkfHoldings, ArkwHoldings, PRINTHoldings, IZRLHoldings]
    
def putDataInDB(tableName, fundTicker, tickerToLinkDict):
    if len(tableName.query.all()) > 0:
        tableName.query.delete()
    
    req = requests.get(tickerToLinkDict[fundTicker])
    
    s = req.content.decode('utf-8')
    ArkkData = pd.read_csv(io.StringIO(s))
    
    
    
    counter = 0
    for row in ArkkData.itertuples():
        counter += 1
        if(type(row.company) != str):
            break
    
    
    
        replacement = None
        for i in row:
            if type(i) == float and math.isnan(i):
                replacement = "----"
                print(i , "was a nan and has been replaced with ---- in row", row)
    
        print(row.ticker, "and", row.cusip)
        ticker = ""
        jsonResponse = None
        marketCap = -1
        logo = ""
        weburl = ""
        shareOutstanding = -1
        
        FiftyTwoWeekHigh = -1
        FiftyTwoWeekLow = -1
        ytdPriceReturnDaily = -1
        FiveDayPriceReturnDaily = -1
        ThirteenWeekPriceReturnDaily = -1
        TwentySixWeekPriceReturnDaily = -1
        price = -1
        if(replacement is not None):  #there is no ticker
            ticker = replacement + str(counter)
        else:
    
            ticker = row.ticker
    
            r = requests.get('https://finnhub.io/api/v1/stock/profile2?cusip='+row.cusip+'&token=bsjiihnrh5r9fp4arl20')
    
            print("     status code for profile: ", r.status_code)
            if r.status_code == 200:
                jsonResponse = r.json()
                if len(jsonResponse) > 0:
    
                    marketCap = jsonResponse['marketCapitalization']
                    logo = jsonResponse['logo']
                    weburl = jsonResponse['weburl']
                    shareOutstanding = jsonResponse['shareOutstanding']
                else:
                    print("error at profile json was empty response")
                
            time.sleep(1)
    
    
            r = requests.get('https://finnhub.io/api/v1/stock/metric?symbol=' + ticker + '&metric=price&token=bsjiihnrh5r9fp4arl20')
            print("     status code for financial data request: ", r.status_code)
            if r.status_code == 200:
                jsonResponse = r.json()
                #    print("     " , jsonResponse)
                if len(jsonResponse['metric']) > 0:
                    FiftyTwoWeekHigh = jsonResponse['metric']['52WeekHigh']
                    FiftyTwoWeekLow = jsonResponse['metric']['52WeekLow']
                    ytdPriceReturnDaily = jsonResponse['metric']['yearToDatePriceReturnDaily']
                    FiveDayPriceReturnDaily = jsonResponse['metric']['5DayPriceReturnDaily']
                    ThirteenWeekPriceReturnDaily = jsonResponse['metric']['13WeekPriceReturnDaily']
                    TwentySixWeekPriceReturnDaily = jsonResponse['metric']['26WeekPriceReturnDaily']
                else:
                    print("error at financial data. json was empty response")
                    
            time.sleep(1)
    
            r = requests.get('https://finnhub.io/api/v1/quote?symbol='+ticker+'&token=bsjiihnrh5r9fp4arl20')
            print("     status code for price request: ", r.status_code)
            if r.status_code == 200:
                jsonResponse = r.json()
                if len(jsonResponse) > 0:
                    price = jsonResponse['c']
                else:
                    print("error at price. json was empty response")
    
    
        time.sleep(1)
    
        new_stock = tableName(ticker=ticker, date=dt.now(), shares=row.shares, cusip=row.cusip, companyName=row.company, marketCap=marketCap, logo=logo, weburl=weburl, shareOutstanding=shareOutstanding, fiftyTwoWeekHigh=FiftyTwoWeekHigh, fiftyTwoWeekLow=FiftyTwoWeekLow, ytdPriceReturnDaily=ytdPriceReturnDaily, fiveDayPriceReturnDaily=FiveDayPriceReturnDaily, thirteenWeekPriceReturnDaily=ThirteenWeekPriceReturnDaily, twentySixWeekPriceReturnDaily=TwentySixWeekPriceReturnDaily, price=price)
        db.session.add(new_stock)
    db.session.commit()
    


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=False, unique=True, nullable=False)
    accessKey = db.Column(db.String(36), unique=True, nullable=False)
    created = db.Column(db.DateTime,index=False,unique=False,nullable=False)
    admin = db.Column(db.Boolean,index=False,unique=False,nullable=False)

    def __str__(self):
        return f"{self.id}: username: {self.username} apikey: {self.accessKey} created: {self.created}"

class ArkkTable(db.Model):
    __tablename__ = "ArkkTable"
    id = db.Column(db.Integer, primary_key=True)
    ticker = db.Column(db.String(64), index=False, unique=True, nullable=False)
    date = db.Column(db.DateTime,index=False,unique=False, nullable=False)
    shares = db.Column(db.Integer, unique=False, index=False)
    cusip = db.Column(db.String(36), unique=False)
    companyName = db.Column(db.String(64), unique=False)
    marketCap= db.Column(db.Integer, unique=False, index=False)
    logo = db.Column(db.String(124), index=False, unique=False)
    weburl = db.Column(db.String(124), index=False)
    shareOutstanding = db.Column(db.Integer, unique=False, index=False)
    fiftyTwoWeekHigh = db.Column(db.Integer, unique=False, index=False)
    fiftyTwoWeekLow = db.Column(db.Integer, unique=False, index=False)
    ytdPriceReturnDaily = db.Column(db.Integer, unique=False, index=False)
    fiveDayPriceReturnDaily = db.Column(db.Integer, unique=False, index=False)
    thirteenWeekPriceReturnDaily = db.Column(db.Integer, unique=False, index=False)
    twentySixWeekPriceReturnDaily = db.Column(db.Integer, unique=False, index=False)
    price = db.Column(db.Integer, unique=False, index=False)

    def __str__(self):
        return f"{self.id}: ticker: {self.ticker} date: {self.date} shares: {self.shares} cusip{self.cusip} companyName: {self.companyName} price: {self.price}"


class ArkqTable(db.Model):
    __tablename__ = "ArkqTable"
    id = db.Column(db.Integer, primary_key=True)
    ticker = db.Column(db.String(64), index=False, unique=True, nullable=False)
    date = db.Column(db.DateTime,index=False,unique=False, nullable=False)
    shares = db.Column(db.Integer, unique=False, index=False)
    cusip = db.Column(db.String(36), unique=False)
    companyName = db.Column(db.String(64), unique=False)
    marketCap= db.Column(db.Integer, unique=False, index=False)
    logo = db.Column(db.String(124), index=False, unique=False)
    weburl = db.Column(db.String(124), index=False)
    shareOutstanding = db.Column(db.Integer, unique=False, index=False)
    fiftyTwoWeekHigh = db.Column(db.Integer, unique=False, index=False)
    fiftyTwoWeekLow = db.Column(db.Integer, unique=False, index=False)
    ytdPriceReturnDaily = db.Column(db.Integer, unique=False, index=False)
    fiveDayPriceReturnDaily = db.Column(db.Integer, unique=False, index=False)
    thirteenWeekPriceReturnDaily = db.Column(db.Integer, unique=False, index=False)
    twentySixWeekPriceReturnDaily = db.Column(db.Integer, unique=False, index=False)
    price = db.Column(db.Integer, unique=False, index=False)

    def __str__(self):
        return f"{self.id}: ticker: {self.ticker} date: {self.date} shares: {self.shares} cusip{self.cusip} companyName: {self.companyName}"


class ArkgTable(db.Model):
    __tablename__ = "ArkgTable"
    id = db.Column(db.Integer, primary_key=True)
    ticker = db.Column(db.String(64), index=False, unique=True, nullable=False)
    date = db.Column(db.DateTime,index=False,unique=False, nullable=False)
    shares = db.Column(db.Integer, unique=False, index=False)
    cusip = db.Column(db.String(36), unique=False)
    companyName = db.Column(db.String(64), unique=False)
    marketCap= db.Column(db.Integer, unique=False, index=False)
    logo = db.Column(db.String(124), index=False, unique=False)
    weburl = db.Column(db.String(124), index=False)
    shareOutstanding = db.Column(db.Integer, unique=False, index=False)
    fiftyTwoWeekHigh = db.Column(db.Integer, unique=False, index=False)
    fiftyTwoWeekLow = db.Column(db.Integer, unique=False, index=False)
    ytdPriceReturnDaily = db.Column(db.Integer, unique=False, index=False)
    fiveDayPriceReturnDaily = db.Column(db.Integer, unique=False, index=False)
    thirteenWeekPriceReturnDaily = db.Column(db.Integer, unique=False, index=False)
    twentySixWeekPriceReturnDaily = db.Column(db.Integer, unique=False, index=False)
    price = db.Column(db.Integer, unique=False, index=False)

    def __str__(self):
        return f"{self.id}: ticker: {self.ticker} date: {self.date} shares: {self.shares} cusip{self.cusip} companyName: {self.companyName}"


class ArkfTable(db.Model):
    __tablename__ = "ArkfTable"
    id = db.Column(db.Integer, primary_key=True)
    ticker = db.Column(db.String(64), index=False, unique=True, nullable=False)
    date = db.Column(db.DateTime,index=False,unique=False, nullable=False)
    shares = db.Column(db.Integer, unique=False, index=False)
    cusip = db.Column(db.String(36), unique=False)
    companyName = db.Column(db.String(64), unique=False)
    marketCap= db.Column(db.Integer, unique=False, index=False)
    logo = db.Column(db.String(124), index=False, unique=False)
    weburl = db.Column(db.String(124), index=False)
    shareOutstanding = db.Column(db.Integer, unique=False, index=False)
    fiftyTwoWeekHigh = db.Column(db.Integer, unique=False, index=False)
    fiftyTwoWeekLow = db.Column(db.Integer, unique=False, index=False)
    ytdPriceReturnDaily = db.Column(db.Integer, unique=False, index=False)
    fiveDayPriceReturnDaily = db.Column(db.Integer, unique=False, index=False)
    thirteenWeekPriceReturnDaily = db.Column(db.Integer, unique=False, index=False)
    twentySixWeekPriceReturnDaily = db.Column(db.Integer, unique=False, index=False)
    price = db.Column(db.Integer, unique=False, index=False)

    def __str__(self):
        return f"{self.id}: ticker: {self.ticker} date: {self.date} shares: {self.shares} cusip{self.cusip} companyName: {self.companyName}"


class ArkwTable(db.Model):
    __tablename__ = "ArkwTable"
    id = db.Column(db.Integer, primary_key=True)
    ticker = db.Column(db.String(64), index=False, unique=True, nullable=False)
    date = db.Column(db.DateTime,index=False,unique=False, nullable=False)
    shares = db.Column(db.Integer, unique=False, index=False)
    cusip = db.Column(db.String(36), unique=False)
    companyName = db.Column(db.String(64), unique=False)
    marketCap= db.Column(db.Integer, unique=False, index=False)
    logo = db.Column(db.String(124), index=False, unique=False)
    weburl = db.Column(db.String(124), index=False)
    shareOutstanding = db.Column(db.Integer, unique=False, index=False)
    fiftyTwoWeekHigh = db.Column(db.Integer, unique=False, index=False)
    fiftyTwoWeekLow = db.Column(db.Integer, unique=False, index=False)
    ytdPriceReturnDaily = db.Column(db.Integer, unique=False, index=False)
    fiveDayPriceReturnDaily = db.Column(db.Integer, unique=False, index=False)
    thirteenWeekPriceReturnDaily = db.Column(db.Integer, unique=False, index=False)
    twentySixWeekPriceReturnDaily = db.Column(db.Integer, unique=False, index=False)
    price = db.Column(db.Integer, unique=False, index=False)


    def __str__(self):
        return f"{self.id}: ticker: {self.ticker} date: {self.date} shares: {self.shares} cusip{self.cusip} companyName: {self.companyName}"

class PrintTable(db.Model):
    __tablename__ = "PrintTable"
    id = db.Column(db.Integer, primary_key=True)
    ticker = db.Column(db.String(64), index=False, unique=True, nullable=False)
    date = db.Column(db.DateTime,index=False,unique=False, nullable=False)
    shares = db.Column(db.Integer, unique=False, index=False)
    cusip = db.Column(db.String(36), unique=False)
    companyName = db.Column(db.String(64), unique=False)
    marketCap= db.Column(db.Integer, unique=False, index=False)
    logo = db.Column(db.String(124), index=False, unique=False)
    weburl = db.Column(db.String(124), index=False)
    shareOutstanding = db.Column(db.Integer, unique=False, index=False)
    fiftyTwoWeekHigh = db.Column(db.Integer, unique=False, index=False)
    fiftyTwoWeekLow = db.Column(db.Integer, unique=False, index=False)
    ytdPriceReturnDaily = db.Column(db.Integer, unique=False, index=False)
    fiveDayPriceReturnDaily = db.Column(db.Integer, unique=False, index=False)
    thirteenWeekPriceReturnDaily = db.Column(db.Integer, unique=False, index=False)
    twentySixWeekPriceReturnDaily = db.Column(db.Integer, unique=False, index=False)
    price = db.Column(db.Integer, unique=False, index=False)


    def __str__(self):
        return f"{self.id}: ticker: {self.ticker} date: {self.date} shares: {self.shares} cusip{self.cusip} companyName: {self.companyName}"

class IzrlTable(db.Model):
    __tablename__ = "IzrlTable"
    id = db.Column(db.Integer, primary_key=True)
    ticker = db.Column(db.String(64), index=False, unique=True, nullable=False)
    date = db.Column(db.DateTime,index=False,unique=False, nullable=False)
    shares = db.Column(db.Integer, unique=False, index=False)
    cusip = db.Column(db.String(36), unique=False)
    companyName = db.Column(db.String(64), unique=False)
    marketCap= db.Column(db.Integer, unique=False, index=False)
    logo = db.Column(db.String(124), index=False, unique=False)
    weburl = db.Column(db.String(124), index=False)
    shareOutstanding = db.Column(db.Integer, unique=False, index=False)
    fiftyTwoWeekHigh = db.Column(db.Integer, unique=False, index=False)
    fiftyTwoWeekLow = db.Column(db.Integer, unique=False, index=False)
    ytdPriceReturnDaily = db.Column(db.Integer, unique=False, index=False)
    fiveDayPriceReturnDaily = db.Column(db.Integer, unique=False, index=False)
    thirteenWeekPriceReturnDaily = db.Column(db.Integer, unique=False, index=False)
    twentySixWeekPriceReturnDaily = db.Column(db.Integer, unique=False, index=False)
    price = db.Column(db.Integer, unique=False, index=False)


    def __str__(self):
        return f"{self.id}: ticker: {self.ticker} date: {self.date} shares: {self.shares} cusip{self.cusip} companyName: {self.companyName}"
