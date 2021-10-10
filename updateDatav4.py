import requests
import csv
import pandas as pd
import io
import json
from datetime import datetime as dt
import math
from requests import ReadTimeout, ConnectTimeout, HTTPError, Timeout, ConnectionError
import time
from os import environ, path


#db imports
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from datetime import datetime as dt

from math import ceil, floor
def float_round(num, places = 0, direction = floor):
    return direction(num * (10**places)) / float(10**places)

def buildAllStocksTable():
    
    engine = create_engine(environ.get('DATABASE_URL'))

    print("attempting connection")
    Base = automap_base()
    
    # reflect the tables
    Base.prepare(engine, reflect=True)
    print("db connection successful, starting session")
    session = Session(engine)
    
    # mapped classes are now created with names by default
    # matching that of the table name.
    
    AllStocks = {}
    tableNames = ['ArkkTable','ArkqTable', 'ArkgTable','ArkfTable', 'ArkwTable', 'PrintTable', 'IzrlTable']
    tableNameTickerMapping={'ArkkTable':"ARKK",'ArkqTable':"ARKQ", 'ArkgTable':"ARKG",'ArkfTable':"ARKF", 'ArkwTable':"ARKW", 'PrintTable':"PRNT", 'IzrlTable':"IZRL"}

    for tableName in tableNames:
        print("table in base classes: ", tableName)
        table = Base.classes[tableName]
        print("looking at rows in: ",table)
        #rows = session.query(table).all()
        for row in session.query(table).all():
            print(row.ticker, " here! ", row.companyName)
            
            if row.companyName in AllStocks:
                print("TOUCHED")
                AllStocksDict = AllStocks[row.companyName]
                AllStocksDict['shares'] += row.shares
                AllStocksDict['value'] += row.value
                AllStocksDict['shares'] += row.shares
                AllStocksDict['heldInFunds'] = AllStocksDict['heldInFunds'] + " " + tableNameTickerMapping[tableName]
            else:
                AllStocks[row.companyName] = {"shares":row.shares, "cusip":row.cusip,"companyName":row.companyName, "heldInFunds":tableNameTickerMapping[tableName], "ticker":row.ticker,"weight":row.weight, "value":row.value, "marketCap":row.marketCap, "logo":row.logo, "weburl":row.weburl, "price":row.price,"FullTimeEmployees":row.FullTimeEmployees,"PERatio":row.PERatio,"EPS":row.EPS,"DividendYield":row.DividendYield,"QuarterlyEarningsGrowthYOY":row.QuarterlyEarningsGrowthYOY,"QuarterlyRevenueGrowthYOY":row.QuarterlyRevenueGrowthYOY,"fiftyTwoWeekHigh":row.fiftyTwoWeekHigh,"fiftyTwoWeekLow":row.fiftyTwoWeekLow,"fiftyDayMovingAverage":row.fiftyDayMovingAverage,"twohundredDayMovingAverage":row.twohundredDayMovingAverage,"PercentInsiders":row.PercentInsiders,"PercentInstitutions":row.PercentInstitutions,"avg10Volume":row.avg10Volume,"avg30Volume":row.avg30Volume,"year5ChangePercent":row.year5ChangePercent,"year2ChangePercent":row.year2ChangePercent,"year1ChangePercent":row.year1ChangePercent,"month6ChangePercent":row.month6ChangePercent,"month3ChangePercent":row.month3ChangePercent,"month1ChangePercent":row.month1ChangePercent,"day5ChangePercent":row.day5ChangePercent,"nextEarningsDate":row.nextEarningsDate,"shareOutstanding":row.shareOutstanding}
        print(tableName , " done!!")

    Table = Base.classes["AllStocks"]
    for x in session.query(Table).all():
        session.delete(x)
    session.commit()

    totalValue = 0
    for key in AllStocks:
        totalValue += AllStocks[key]['value']




    for key in AllStocks:
        weight = float_round((AllStocks[key]['value'] / totalValue * 100), 3, round) #round naturally
    
        session.add(Table(date=dt.now(), cusip=AllStocks[key]['cusip'], companyName=AllStocks[key]['companyName'], ticker=AllStocks[key]['ticker'], logo=AllStocks[key]['logo'], weburl=AllStocks[key]['weburl'], value=AllStocks[key]['value'], shares=AllStocks[key]['shares'], weight=weight, heldInFunds=AllStocks[key]['heldInFunds'], price=AllStocks[key]['price'], marketCap=AllStocks[key]['marketCap'], FullTimeEmployees=AllStocks[key]['FullTimeEmployees'], PERatio=AllStocks[key]['PERatio'], EPS=AllStocks[key]['EPS'], DividendYield=AllStocks[key]['DividendYield'], QuarterlyEarningsGrowthYOY=AllStocks[key]['QuarterlyEarningsGrowthYOY'], QuarterlyRevenueGrowthYOY=AllStocks[key]['QuarterlyRevenueGrowthYOY'], fiftyTwoWeekHigh=AllStocks[key]['fiftyTwoWeekHigh'],fiftyTwoWeekLow=AllStocks[key]['fiftyTwoWeekLow'], fiftyDayMovingAverage=AllStocks[key]['fiftyDayMovingAverage'], twohundredDayMovingAverage=AllStocks[key]['twohundredDayMovingAverage'], PercentInsiders=AllStocks[key]['PercentInsiders'], PercentInstitutions=AllStocks[key]['PercentInstitutions'], avg10Volume=AllStocks[key]['avg10Volume'], avg30Volume=AllStocks[key]['avg30Volume'], year5ChangePercent=AllStocks[key]['year5ChangePercent'], year2ChangePercent=AllStocks[key]['year2ChangePercent'], year1ChangePercent=AllStocks[key]['year1ChangePercent'], month6ChangePercent=AllStocks[key]['month6ChangePercent'], month3ChangePercent=AllStocks[key]['month3ChangePercent'], month1ChangePercent=AllStocks[key]['month1ChangePercent'], day5ChangePercent=AllStocks[key]['day5ChangePercent'], nextEarningsDate=AllStocks[key]['nextEarningsDate'], shareOutstanding= AllStocks[key]['shareOutstanding']))
    session.commit()
    





def putDataInDB(tableName, fundTicker, tickerToLinkDict, AllStocks, engine):
    
    print("attempting connection")
    Base = automap_base()
    
    
    # reflect the tables
    Base.prepare(engine, reflect=True)
    # mapped classes are now created with names by default
    # matching that of the table name.
    Table = Base.classes[tableName]
    print("db connection successful, starting session")
    session = Session(engine)
    
    # rudimentary relationships are produced
    print(session.query(Table).first())
    
    
    """
        if len(table.query.all()) > 0:
        tableName.query.delete()
        """
    
    #delete previous data
    for x in session.query(Table).all():
        session.delete(x)
    session.commit()
    print("table data deleted")
    

    #database is not connected so get data from Ark
    url = tickerToLinkDict[fundTicker]
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'}
    s=requests.get(url, headers=headers).content
    ArkkData=pd.read_csv(io.StringIO(s.decode('utf-8')), sep=',', error_bad_lines=False)

    #this will loop us over all of the stocks in this row.
    counter = 0
    for row in ArkkData.itertuples():
        counter += 1
        if(type(row.company) != str):
            break

        #deal with rows that dont have a ticker
        replacement = None
        for i in row:
            if type(i) == float and math.isnan(i):
                replacement = "----"
                print(i , "was a nan and has been replaced with ---- in row", row)
        print(row.ticker, "and", row.cusip)

        #declare the variables for the columns.
        cusip = ""
        companyName = ""
        ticker = ""
        logo = ""
        weburl = ""

        value = -1
        shares = -1
        weight = -1.0

        price = -1.0
        marketCap= -1

        FullTimeEmployees=-1
        PERatio=-1.0
        EPS=-1.0
        DividendYield=-1.0
        QuarterlyEarningsGrowthYOY=-1.0
        QuarterlyRevenueGrowthYOY=-1.0
        fiftyTwoWeekHigh=-1.0
        fiftyTwoWeekLow=-1.0
        fiftyDayMovingAverage=-1.0
        twohundredDayMovingAverage = -1.0
        PercentInsiders=-1.0
        PercentInstitutions=-1.0
        avg10Volume=-1.0
        avg30Volume=-1.0
        year5ChangePercent=-1.0
        year2ChangePercent=-1.0
        year1ChangePercent=-1.0
        month6ChangePercent=-1.0
        month3ChangePercent=-1.0
        month1ChangePercent=-1.0
        day5ChangePercent=-1.0
        nextEarningsDate=""
        shareOutstanding=-1

        #update the ticker
        if(replacement is not None):  #there is no ticker
            ticker = replacement + str(counter)
        else:
            ticker = row.ticker



        #first request goes to iex.
        r = requests.get('https://cloud.iexapis.com/stable/stock/'+ticker+'/stats?token=pk_70c832e6a3464a7482c7af18b2eaa02a')
        print("     status code for keystats from iex: ", r.status_code)
        if r.status_code == 200:
            jsonResponse = r.json()
            if len(jsonResponse) > 0:
                if 'employees' in jsonResponse:
                    FullTimeEmployees=jsonResponse['employees']
                if 'peRatio' in jsonResponse:
                    PERatio=jsonResponse['peRatio']
                if 'ttmEPS' in jsonResponse:
                    EPS=jsonResponse['ttmEPS']
                if 'dividendYield' in jsonResponse:
                    DividendYield=jsonResponse['dividendYield']
                if 'week52high' in jsonResponse:
                    fiftyTwoWeekHigh=jsonResponse['week52high']
                if 'week52low' in jsonResponse:
                    fiftyTwoWeekLow=jsonResponse['week52low']
                if 'day50MovingAvg' in jsonResponse:
                    fiftyDayMovingAverage=jsonResponse['day50MovingAvg']
                if 'day200MovingAvg' in jsonResponse:
                    twohundredDayMovingAverage=jsonResponse['day200MovingAvg']
                if 'avg10Volume' in jsonResponse:
                    avg10Volume=jsonResponse['avg10Volume']
                if 'avg30Volume' in jsonResponse:
                    avg30Volume=jsonResponse['avg30Volume']
                if 'year5ChangePercent' in jsonResponse:
                    year5ChangePercent=jsonResponse['year5ChangePercent']
                if 'year2ChangePercent' in jsonResponse:
                    year2ChangePercent=jsonResponse['year2ChangePercent']
                if 'year1ChangePercent' in jsonResponse:
                    year1ChangePercent=jsonResponse['year1ChangePercent']
                if 'month6ChangePercent' in jsonResponse:
                    month6ChangePercent=jsonResponse['month6ChangePercent']
                if 'month3ChangePercent' in jsonResponse:
                    month3ChangePercent=jsonResponse['month3ChangePercent']
                if 'month1ChangePercent' in jsonResponse:
                    month1ChangePercent=jsonResponse['month1ChangePercent']
                if 'day5ChangePercent' in jsonResponse:
                    day5ChangePercent=jsonResponse['day5ChangePercent']
                if 'nextEarningsDate' in jsonResponse:
                    nextEarningsDate=jsonResponse['nextEarningsDate']
                if 'marketcap' in jsonResponse:
                    marketCap = jsonResponse['marketcap'] / 100000
            else:
                print("error at profile json was empty response")

        #second requenst goes to finnhub
        r = requests.get('https://finnhub.io/api/v1/stock/profile2?symbol='+ticker+'&token=bsjiihnrh5r9fp4arl20')

        print("     status code for profile from finnhub: ", r.status_code)
        if r.status_code == 200:
            jsonResponse = r.json()
            if len(jsonResponse) > 0:
                if 'logo' in jsonResponse:
                    logo = jsonResponse['logo']
                if 'weburl' in jsonResponse:
                    weburl = jsonResponse['weburl']
                if 'shareOutstanding' in jsonResponse:
                    shareOutstanding = jsonResponse['shareOutstanding']
            else:
                print("error json was empty response")

        time.sleep(1)

        #fourth request to alpha advantage
        """
        r = requests.get('https://www.alphavantage.co/query?function=OVERVIEW&symbol='+ticker+'&apikey=9EAVREWPSGORFHYG')
        print("     status code for overview from aplhaadvantage: ", r.status_code)
        if r.status_code == 200:
            jsonResponse = r.json()
            if len(jsonResponse) > 0:
                print(jsonResponse)
                QuarterlyEarningsGrowthYOY=jsonResponse['QuarterlyEarningsGrowthYOY']
                QuarterlyRevenueGrowthYOY=jsonResponse['QuarterlyRevenueGrowthYOY']
                PercentInsiders=jsonResponse['PercentInsiders']
                PercentInstitutions=jsonResponse['PercentInstitutions']
            else:
                print("error json was empty response")
        """
        time.sleep(1)

        #third request to finnhub for price
        r = requests.get('https://finnhub.io/api/v1/quote?symbol='+ticker+'&token=bsjiihnrh5r9fp4arl20')
        print("     status code for price request from finnhub: ", r.status_code)
        if r.status_code == 200:
            jsonResponse = r.json()
            if len(jsonResponse) > 0:
                if 'c' in jsonResponse:
                    price = jsonResponse['c']
            else:
                print("error at price. json was empty response")

        if row.company in AllStocks:
            AllStocksDict = AllStocks[row.company]
            AllStocksDict['shares'] += row.shares
            AllStocksDict['value'] += (row[7] / 1000)
            
            AllStocksDict['shares'] += row.shares
            AllStocksDict['heldInFunds'] = AllStocksDict['heldInFunds'] + "" + fundTicker
        else:
            AllStocks[row.company] = {"shares":row.shares, "cusip":row.cusip,"companyName":row.company, "heldInFunds":fundTicker, "ticker":ticker,"weight":row[8], "value":row[7], "marketCap":marketCap, "logo":logo, "weburl":weburl, "price":price,"FullTimeEmployees":FullTimeEmployees,"PERatio":PERatio,"EPS":EPS,"DividendYield":DividendYield,"QuarterlyEarningsGrowthYOY":QuarterlyEarningsGrowthYOY,"QuarterlyRevenueGrowthYOY":QuarterlyRevenueGrowthYOY,"fiftyTwoWeekHigh":fiftyTwoWeekHigh,"fiftyTwoWeekLow":fiftyTwoWeekLow,"fiftyDayMovingAverage":fiftyDayMovingAverage,"twohundredDayMovingAverage":twohundredDayMovingAverage,"PercentInsiders":PercentInsiders,"PercentInstitutions":PercentInstitutions,"avg10Volume":avg10Volume,"avg30Volume":avg30Volume,"year5ChangePercent":year5ChangePercent,"year2ChangePercent":year2ChangePercent,"year1ChangePercent":year1ChangePercent,"month6ChangePercent":month6ChangePercent,"month3ChangePercent":month3ChangePercent,"month1ChangePercent":month1ChangePercent,"day5ChangePercent":day5ChangePercent,"nextEarningsDate":nextEarningsDate,"shareOutstanding":shareOutstanding}
        time.sleep(1)

        session.add(Table(date=dt.now(), shares=row.shares, cusip=row.cusip,companyName=row.company, ticker=ticker,weight=row[8], value=(row[7] / 1000), marketCap=marketCap, logo=logo, weburl=weburl, price=price, FullTimeEmployees=FullTimeEmployees,PERatio=PERatio,EPS=EPS,DividendYield=DividendYield,QuarterlyEarningsGrowthYOY=QuarterlyEarningsGrowthYOY,QuarterlyRevenueGrowthYOY=QuarterlyRevenueGrowthYOY,fiftyTwoWeekHigh=fiftyTwoWeekHigh,fiftyTwoWeekLow=fiftyTwoWeekLow,fiftyDayMovingAverage=fiftyDayMovingAverage,twohundredDayMovingAverage=twohundredDayMovingAverage,PercentInsiders=PercentInsiders,PercentInstitutions=PercentInstitutions,avg10Volume=avg10Volume,avg30Volume=avg30Volume,year5ChangePercent=year5ChangePercent,year2ChangePercent=year2ChangePercent,year1ChangePercent=year1ChangePercent,month6ChangePercent=month6ChangePercent,month3ChangePercent=month3ChangePercent,month1ChangePercent=month1ChangePercent,day5ChangePercent=day5ChangePercent,nextEarningsDate=nextEarningsDate,shareOutstanding=shareOutstanding))
            
    session.commit()




def updateData():
    
    tickerToLinkDict = {"ARKK": "https://ark-funds.com/wp-content/uploads/2021/08/ARK_INNOVATION_ETF_ARKK_HOLDINGS-7.csv", "ARKQ": "https://ark-funds.com/wp-content/uploads/2021/08/ARK_AUTONOMOUS_TECHNOLOGY__ROBOTICS_ETF_ARKQ_HOLDINGS-2.csv","ARKG": "https://ark-funds.com/wp-content/uploads/2021/08/ARK_GENOMIC_REVOLUTION_MULTISECTOR_ETF_ARKG_HOLDINGS-1.csv", "ARKF" : "https://ark-funds.com/wp-content/uploads/2021/08/ARK_FINTECH_INNOVATION_ETF_ARKF_HOLDINGS-1.csv", "ARKW" :"https://ark-funds.com/wp-content/uploads/2021/08/ARK_NEXT_GENERATION_INTERNET_ETF_ARKW_HOLDINGS-1.csv" , "PRINT":"https://ark-funds.com/wp-content/uploads/2021/08/THE_3D_PRINTING_ETF_PRNT_HOLDINGS.csv", "IZRL":"https://ark-funds.com/wp-content/uploads/2021/08/ARK_ISRAEL_INNOVATIVE_TECHNOLOGY_ETF_IZRL_HOLDINGS.csv" }
    
    AllStocks = {}
    
    print("creeating engine")
    engine = create_engine(environ.get('DATABASE_URL'))
    print("engine created")

    putDataInDB("ArkkTable", "ARKK", tickerToLinkDict, AllStocks, engine)
    print("Done with ArkkTable!")
    
    putDataInDB("ArkqTable", "ARKQ", tickerToLinkDict, AllStocks, engine)
    print("Done with ArkqTable!")
    
    putDataInDB("ArkgTable", "ARKG", tickerToLinkDict, AllStocks, engine)
    print("Done with ArkgTable!")
    
    
    putDataInDB("ArkfTable", "ARKF", tickerToLinkDict, AllStocks, engine)
    print("Done with ArkfTable!")

    putDataInDB("ArkwTable", "ARKW", tickerToLinkDict, AllStocks, engine)
    print("Done with ArkwTable!")
    
    putDataInDB("PrintTable", "PRINT", tickerToLinkDict, AllStocks, engine)
    print("Done with PrintTable!")

    putDataInDB("IzrlTable", "IZRL", tickerToLinkDict, AllStocks, engine)
    print("Done with IzrlTable!")
    
    print("Done with all the tables!")
    print("uploading stock information into db....")









updateData()
buildAllStocksTable()
