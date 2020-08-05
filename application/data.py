import requests
import csv
import pandas as pd
import io
import json
from datetime import datetime as dt
import math
import models
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


def putARKQinDB():
    ArkqTable.query.delete()
    
    req = requests.get("https://ark-funds.com/wp-content/fundsiteliterature/csv/ARK_AUTONOMOUS_TECHNOLOGY_&_ROBOTICS_ETF_ARKQ_HOLDINGS.csv")
    
    s = req.content.decode('utf-8')
    data = pd.read_csv(io.StringIO(s))
    
    counter = 0
    for row in data.itertuples():
        counter += 1
        if(type(row.company) != str):
            break
        
        replacement = None
        for i in row:
            if type(i) == float and math.isnan(i):
                replacement = "----"
                print(i , "was a nan and has been replaced with ---- in row", row)
    
        ticker = ""
        if(replacement is not None):
            ticker = replacement + str(counter)
        else:
            ticker = row.ticker
                
        new_stock = ArkqTable(ticker=ticker, date=dt.now(), shares=row.shares, cusip=row.cusip, companyName=row.company)
        db.session.add(new_stock)
    db.session.commit()

#ARKG
def putARKGinDB():
    ArkgTable.query.delete()
    
    req = requests.get("https://ark-funds.com/wp-content/fundsiteliterature/csv/ARK_GENOMIC_REVOLUTION_MULTISECTOR_ETF_ARKG_HOLDINGS.csv")
    
    s = req.content.decode('utf-8')
    data = pd.read_csv(io.StringIO(s))

    counter = 0
    for row in data.itertuples():
        counter += 1
        if(type(row.company) != str):
            break
        
        replacement = None
        for i in row:
            if type(i) == float and math.isnan(i):
                replacement = "----"
                print(i , "was a nan and has been replaced with ---- in row", row)
    
        ticker = ""
        if(replacement is not None):
            ticker = replacement + str(counter)
        else:
            ticker = row.ticker
        
        new_stock = ArkgTable(ticker=ticker, date=dt.now(), shares=row.shares, cusip=row.cusip, companyName=row.company)
        db.session.add(new_stock)
    db.session.commit()


#ARKF
def putARKFinDB():
    ArkfTable.query.delete()
    
    req = requests.get("https://ark-funds.com/wp-content/fundsiteliterature/csv/ARK_FINTECH_INNOVATION_ETF_ARKF_HOLDINGS.csv")
    
    s = req.content.decode('utf-8')
    data = pd.read_csv(io.StringIO(s))
    
    counter = 0
    for row in data.itertuples():
        counter += 1
        if(type(row.company) != str):
            break
        
        replacement = None
        for i in row:
            if type(i) == float and math.isnan(i):
                replacement = "----"
                print(i , "was a nan and has been replaced with ---- in row", row)
    
        ticker = ""
        if(replacement is not None):
            ticker = replacement + str(counter)
        else:
            ticker = row.ticker
        
        new_stock = ArkfTable(ticker=ticker, date=dt.now(), shares=row.shares, cusip=row.cusip, companyName=row.company)
        db.session.add(new_stock)
    db.session.commit()

#ARKW
def putARKWinDB():
    ArkwTable.query.delete()
    
    req = requests.get("https://ark-funds.com/wp-content/fundsiteliterature/csv/ARK_NEXT_GENERATION_INTERNET_ETF_ARKW_HOLDINGS.csv")
    
    s = req.content.decode('utf-8')
    data = pd.read_csv(io.StringIO(s))
    
    counter = 0
    for row in data.itertuples():
        counter += 1
        if(type(row.company) != str):
            break
        
        replacement = None
        for i in row:
            if type(i) == float and math.isnan(i):
                replacement = "----"
                print(i , "was a nan and has been replaced with ---- in row", row)
    
        ticker = ""
        if(replacement is not None):
            ticker = replacement + str(counter)
        else:
            ticker = row.ticker
        
        new_stock = ArkwTable(ticker=ticker, date=dt.now(), shares=row.shares, cusip=row.cusip, companyName=row.company)
        db.session.add(new_stock)
    db.session.commit()

#PRINT
def putPRINTinDB():
    PrintTable.query.delete()
    
    req = requests.get("https://ark-funds.com/wp-content/fundsiteliterature/csv/THE_3D_PRINTING_ETF_PRNT_HOLDINGS.csv")
    
    s = req.content.decode('utf-8')
    data = pd.read_csv(io.StringIO(s))
    
    counter = 0
    for row in data.itertuples():
        counter += 1
        if(type(row.company) != str):
            break
        
        replacement = None
        for i in row:
            if type(i) == float and math.isnan(i):
                replacement = "----"
                print(i , "was a nan and has been replaced with ---- in row", row)
    
        ticker = ""
        if(replacement is not None):
            ticker = replacement + str(counter)
        else:
            ticker = row.ticker
        
        new_stock = PrintTable(ticker=ticker, date=dt.now(), shares=row.shares, cusip=row.cusip, companyName=row.company)
        db.session.add(new_stock)
    db.session.commit()



def putIZRLinDB():
    IzrlTable.query.delete()
    
    req = requests.get("https://ark-funds.com/wp-content/fundsiteliterature/csv/ARK_ISRAEL_INNOVATIVE_TECHNOLOGY_ETF_IZRL_HOLDINGS.csv")
    
    s = req.content.decode('utf-8')
    data = pd.read_csv(io.StringIO(s))
    
    counter = 0
    for row in data.itertuples():
        counter += 1
        if(type(row.company) != str):
            break
        
        replacement = None
        for i in row:
            if type(i) == float and math.isnan(i):
                replacement = "----"
                print(i , "was a nan and has been replaced with ---- in row", row)
    
        ticker = ""
        if(replacement is not None):
            ticker = replacement + str(counter)
        else:
            ticker = row.ticker
        
        new_stock = IzrlTable(ticker=ticker, date=dt.now(), shares=row.shares, cusip=row.cusip, companyName=row.company)
        db.session.add(new_stock)
    db.session.commit()

#------------------------------------------------------------------------------------------------------#

def getDataFromDB(tableName, fundTicker):
    table = tableName.query.all()
    if len(table) == 0:
        print("table is empty")
        return
    dict = {"timestamp" : table[0].date, "fundTicker" : fundTicker,  "holdings" : [] }
    for row in table:
        rowDict = {"ticker" : row.ticker , "company": row.companyName, "cusip": row.cusip, "shares" : row.shares, "marketCap" : row.marketCap, "logo" : row.logo, "weburl" : row.weburl, "sharesOutstandig" : row.shareOutstanding, "fiftyTwoWeekHigh" : row.fiftyTwoWeekHigh, "fiftyTwoWeekLow" : row.fiftyTwoWeekLow, "ytdPriceReturnDaily" : row.ytdPriceReturnDaily, "fiveDayPriceReturnDaily" : row.fiveDayPriceReturnDaily, "thirteenWeekPriceReturnDaily" : row.thirteenWeekPriceReturnDaily, "twentySixWeekPriceReturnDaily" : row.twentySixWeekPriceReturnDaily, "price": row.price}
        dict["holdings"].append(rowDict)
    return dict

def getARKQDatafromDB():
    table = ArkqTable.query.all()
    dict = {"timestamp" : table[0].date, "fundTicker" : "ARKQ",  "holdings" : [] }
    for row in table:
        rowDict = {"ticker" : row.ticker , "company": row.companyName, "cusip": row.cusip, "shares" : row.shares}
        dict["holdings"].append(rowDict)
    return dict

def getARKGDatafromDB():
    table = ArkgTable.query.all()
    dict = {"timestamp" : table[0].date, "fundTicker" : "ARKG",  "holdings" : [] }
    for row in table:
        rowDict = {"ticker" : row.ticker , "company": row.companyName, "cusip": row.cusip, "shares" : row.shares}
        dict["holdings"].append(rowDict)
    return dict

def getARKFDatafromDB():
    table = ArkfTable.query.all()
    dict = {"timestamp" : table[0].date, "fundTicker" : "ARKF",  "holdings" : [] }
    for row in table:
        rowDict = {"ticker" : row.ticker , "company": row.companyName, "cusip": row.cusip, "shares" : row.shares}
        dict["holdings"].append(rowDict)
    return dict

def getARKWDatafromDB():
    table = ArkwTable.query.all()
    dict = {"timestamp" : table[0].date, "fundTicker" : "ARKW",  "holdings" : [] }
    for row in table:
        rowDict = {"ticker" : row.ticker , "company": row.companyName, "cusip": row.cusip, "shares" : row.shares}
        dict["holdings"].append(rowDict)
    return dict

def getPRINTDatafromDB():
    table = PrintTable.query.all()
    dict = {"timestamp" : table[0].date, "fundTicker" : "PRINT",  "holdings" : [] }
    for row in table:
        rowDict = {"ticker" : row.ticker , "company": row.companyName, "cusip": row.cusip, "shares" : row.shares}
        dict["holdings"].append(rowDict)
    return dict

def getIZRLDatafromDB():
    table = IzrlTable.query.all()
    dict = {"timestamp" : table[0].date, "fundTicker" : "IZRL",  "holdings" : [] }
    for row in table:
        rowDict = {"ticker" : row.ticker , "company": row.companyName, "cusip": row.cusip, "shares" : row.shares}
        dict["holdings"].append(rowDict)
    return dict
    

"""
def getARKKData():
    req = requests.get("https://ark-funds.com/wp-content/fundsiteliterature/csv/ARK_INNOVATION_ETF_ARKK_HOLDINGS.csv")

    s = req.content.decode('utf-8')
    ArkkData = pd.read_csv(io.StringIO(s))
    
    #begin building dictionary to return in JSON response
    ArkkDict = {"timestamp" : ArkkData['date'][0], "fundTicker" : "ARKK",  "holdings" : [] }

    for row in ArkkData.itertuples():
        if(type(row.company) != str):
            break
        
        replacement = None
        for i in row:
            if type(i) == float and math.isnan(i):
                replacement = "----"
                print(i , "was a nan and has been replaced with ---- in row", row)
                            
        ticker = ""
        if(replacement is not None):
            ticker = replacement
        else:
            ticker = row.ticker
                                                
        #new_stock = ArkkTable(ticker=ticker, date=ArkkData['date'][0], shares=row.shares, cusip=row.cusip, companyName=row.company)
        #db.session.add(new_stock)

        stock = {"ticker" : ticker , "company": row.company,'cusip': row.cusip, 'shares':row.shares}
        ArkkDict["holdings"].append(stock)

    print("dcitionary: ", ArkkDict)
    return(ArkkDict)


def getARKQData():
    req = requests.get("https://ark-funds.com/wp-content/fundsiteliterature/csv/ARK_AUTONOMOUS_TECHNOLOGY_&_ROBOTICS_ETF_ARKQ_HOLDINGS.csv")
    
    s = req.content.decode('utf-8')
    ArkkData = pd.read_csv(io.StringIO(s))
    
    #begin building dictionary to return in JSON response
    ArkkDict = {"timestamp" : ArkkData['date'][0], "fundTicker" : "ARKQ",  "holdings" : [] }
    
    for row in ArkkData.itertuples():
        if(type(row.company) != str):
            break
        stock = {"ticker" : row.ticker , "company": row.company,'cusip': row.cusip, 'shares':row.shares}
        ArkkDict["holdings"].append(stock)
    
    print("dcitionary: ", ArkkDict)
    return(ArkkDict)

def getARKWData():
    req = requests.get("https://ark-funds.com/wp-content/fundsiteliterature/csv/ARK_NEXT_GENERATION_INTERNET_ETF_ARKW_HOLDINGS.csv")
    
    s = req.content.decode('utf-8')
    ArkkData = pd.read_csv(io.StringIO(s))
    
    #begin building dictionary to return in JSON response
    ArkkDict = {"timestamp" : ArkkData['date'][0], "fundTicker" : "ARKW",  "holdings" : [] }
    
    for row in ArkkData.itertuples():
        if(type(row.company) != str):
            break
        stock = {"ticker" : row.ticker , "company": row.company,'cusip': row.cusip, 'shares':row.shares}
        ArkkDict["holdings"].append(stock)
    
    print("dcitionary: ", ArkkDict)
    return(ArkkDict)


def getARKGData():
    req = requests.get("https://ark-funds.com/wp-content/fundsiteliterature/csv/ARK_GENOMIC_REVOLUTION_MULTISECTOR_ETF_ARKG_HOLDINGS.csv")
    
    s = req.content.decode('utf-8')
    ArkkData = pd.read_csv(io.StringIO(s))
    
    #begin building dictionary to return in JSON response
    ArkkDict = {"timestamp" : ArkkData['date'][0], "fundTicker" : "ARKG",  "holdings" : [] }
    
    for row in ArkkData.itertuples():
        if(type(row.company) != str):
            break
        stock = {"ticker" : row.ticker , "company": row.company,'cusip': row.cusip, 'shares':row.shares}
        ArkkDict["holdings"].append(stock)
    
    print("dcitionary: ", ArkkDict)
    return(ArkkDict)

def getARKFData():
    req = requests.get("https://ark-funds.com/wp-content/fundsiteliterature/csv/ARK_FINTECH_INNOVATION_ETF_ARKF_HOLDINGS.csv")
    
    s = req.content.decode('utf-8')
    ArkkData = pd.read_csv(io.StringIO(s))
    
    #begin building dictionary to return in JSON response
    ArkkDict = {"timestamp" : ArkkData['date'][0], "fundTicker" : "ARKF",  "holdings" : [] }
    
    for row in ArkkData.itertuples():
        if(type(row.company) != str):
            break
        stock = {"ticker" : row.ticker , "company": row.company,'cusip': row.cusip, 'shares':row.shares}
        ArkkDict["holdings"].append(stock)
    
    print("dcitionary: ", ArkkDict)
    return(ArkkDict)

def getPRINTData():
    req = requests.get("https://ark-funds.com/wp-content/fundsiteliterature/csv/THE_3D_PRINTING_ETF_PRNT_HOLDINGS.csv")
    
    s = req.content.decode('utf-8')
    ArkkData = pd.read_csv(io.StringIO(s))
    
    #begin building dictionary to return in JSON response
    ArkkDict = {"timestamp" : ArkkData['date'][0], "fundTicker" : "PRINT",  "holdings" : [] }
    
    for row in ArkkData.itertuples():
        if(type(row.company) != str):
            break
        stock = {"ticker" : row.ticker , "company": row.company,'cusip': row.cusip, 'shares':row.shares}
        ArkkDict["holdings"].append(stock)
    
    print("dcitionary: ", ArkkDict)
    return(ArkkDict)
def getIZRLData():
    req = requests.get("https://ark-funds.com/wp-content/fundsiteliterature/csv/ARK_ISRAEL_INNOVATIVE_TECHNOLOGY_ETF_IZRL_HOLDINGS.csv")
    
    s = req.content.decode('utf-8')
    ArkkData = pd.read_csv(io.StringIO(s))
    
    #begin building dictionary to return in JSON response
    ArkkDict = {"timestamp" : ArkkData['date'][0], "fundTicker" : "IZRL",  "holdings" : [] }
    
    for row in ArkkData.itertuples():
        if(type(row.company) != str):
            break
        stock = {"ticker" : row.ticker , "company": row.company,'cusip': row.cusip, 'shares':row.shares}
        ArkkDict["holdings"].append(stock)

    return(ArkkDict)
    
    """
if __name__ == '__main__':
    print("here")
    updateData()
