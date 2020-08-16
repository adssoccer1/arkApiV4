"""Data models."""
from . import db



class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=False, unique=True, nullable=False)
    accessKey = db.Column(db.String(36), unique=True, nullable=False)
    created = db.Column(db.DateTime,index=False,unique=False,nullable=False)
    admin = db.Column(db.Boolean,index=False,unique=False,nullable=False)

    def __str__(self):
        return f"{self.id}: username: {self.username} apikey: {self.accessKey} created: {self.created}"


class AllStocks(db.Model):
    __tablename__ = "AllStocks"

    id = db.Column(db.Integer, primary_key=True)
    
    date = db.Column(db.DateTime,index=False,unique=False, nullable=False)
    cusip = db.Column(db.String(36), unique=False)
    companyName = db.Column(db.String(64), unique=False)
    ticker = db.Column(db.String(64), index=False, unique=True, nullable=False)
    logo = db.Column(db.String(124), index=False, unique=False)
    weburl = db.Column(db.String(124), index=False)

    value = db.Column(db.Integer, unique=False, index=False)
    shares = db.Column(db.Integer, unique=False, index=False)
    weight = db.Column(db.Float, unique=False, index=False)
    heldInFunds = db.Column(db.String(64), index=False)

    
    price = db.Column(db.Float, unique=False, index=False)
    marketCap= db.Column(db.Integer, unique=False, index=False)
    
    FullTimeEmployees=db.Column(db.Integer, unique=False, index=False)
    PERatio=db.Column(db.Float, unique=False, index=False)
    EPS=db.Column(db.Float, unique=False, index=False)
    DividendYield=db.Column(db.Float, unique=False, index=False)
    QuarterlyEarningsGrowthYOY=db.Column(db.Float, unique=False, index=False)
    QuarterlyRevenueGrowthYOY=db.Column(db.Float, unique=False, index=False)
    fiftyTwoWeekHigh=db.Column(db.Float, unique=False, index=False)
    fiftyTwoWeekLow=db.Column(db.Float, unique=False, index=False)
    fiftyDayMovingAverage=db.Column(db.Float, unique=False, index=False)
    twohundredDayMovingAverage = db.Column(db.Float, unique=False, index=False)
    PercentInsiders=db.Column(db.Float, unique=False, index=False)
    PercentInstitutions=db.Column(db.Float, unique=False, index=False)
    avg10Volume=db.Column(db.Float, unique=False, index=False)
    avg30Volume=db.Column(db.Float, unique=False, index=False)
    year5ChangePercent=db.Column(db.Float, unique=False, index=False)
    year2ChangePercent=db.Column(db.Float, unique=False, index=False)
    year1ChangePercent=db.Column(db.Float, unique=False, index=False)
    month6ChangePercent=db.Column(db.Float, unique=False, index=False)
    month3ChangePercent=db.Column(db.Float, unique=False, index=False)
    month1ChangePercent=db.Column(db.Float, unique=False, index=False)
    day5ChangePercent=db.Column(db.Float, unique=False, index=False)
    nextEarningsDate=db.Column(db.String(64), unique=False)
    shareOutstanding = db.Column(db.Integer, unique=False, index=False)


class ArkkTable(db.Model):
    __tablename__ = "ArkkTable"
    id = db.Column(db.Integer, primary_key=True)
    
    date = db.Column(db.DateTime,index=False,unique=False, nullable=False)
    cusip = db.Column(db.String(36), unique=False)
    companyName = db.Column(db.String(64), unique=False)
    ticker = db.Column(db.String(64), index=False, unique=True, nullable=False)
    logo = db.Column(db.String(124), index=False, unique=False)
    weburl = db.Column(db.String(124), index=False)
    
    value = db.Column(db.Integer, unique=False, index=False)
    shares = db.Column(db.Integer, unique=False, index=False)
    weight = db.Column(db.Float, unique=False, index=False)
    
    price = db.Column(db.Float, unique=False, index=False)
    marketCap= db.Column(db.Integer, unique=False, index=False)
    
    FullTimeEmployees=db.Column(db.Integer, unique=False, index=False)
    PERatio=db.Column(db.Float, unique=False, index=False)
    EPS=db.Column(db.Float, unique=False, index=False)
    DividendYield=db.Column(db.Float, unique=False, index=False)
    QuarterlyEarningsGrowthYOY=db.Column(db.Float, unique=False, index=False)
    QuarterlyRevenueGrowthYOY=db.Column(db.Float, unique=False, index=False)
    fiftyTwoWeekHigh=db.Column(db.Float, unique=False, index=False)
    fiftyTwoWeekLow=db.Column(db.Float, unique=False, index=False)
    fiftyDayMovingAverage=db.Column(db.Float, unique=False, index=False)
    twohundredDayMovingAverage = db.Column(db.Float, unique=False, index=False)
    PercentInsiders=db.Column(db.Float, unique=False, index=False)
    PercentInstitutions=db.Column(db.Float, unique=False, index=False)
    avg10Volume=db.Column(db.Float, unique=False, index=False)
    avg30Volume=db.Column(db.Float, unique=False, index=False)
    year5ChangePercent=db.Column(db.Float, unique=False, index=False)
    year2ChangePercent=db.Column(db.Float, unique=False, index=False)
    year1ChangePercent=db.Column(db.Float, unique=False, index=False)
    month6ChangePercent=db.Column(db.Float, unique=False, index=False)
    month3ChangePercent=db.Column(db.Float, unique=False, index=False)
    month1ChangePercent=db.Column(db.Float, unique=False, index=False)
    day5ChangePercent=db.Column(db.Float, unique=False, index=False)
    nextEarningsDate=db.Column(db.String(64), unique=False)
    shareOutstanding = db.Column(db.Integer, unique=False, index=False)



class ArkqTable(db.Model):
    __tablename__ = "ArkqTable"
    id = db.Column(db.Integer, primary_key=True)
    
    date = db.Column(db.DateTime,index=False,unique=False, nullable=False)
    cusip = db.Column(db.String(36), unique=False)
    companyName = db.Column(db.String(64), unique=False)
    ticker = db.Column(db.String(64), index=False, unique=True, nullable=False)
    logo = db.Column(db.String(124), index=False, unique=False)
    weburl = db.Column(db.String(124), index=False)
    
    value = db.Column(db.Integer, unique=False, index=False)
    shares = db.Column(db.Integer, unique=False, index=False)
    weight = db.Column(db.Float, unique=False, index=False)
    
    price = db.Column(db.Float, unique=False, index=False)
    marketCap= db.Column(db.Integer, unique=False, index=False)
    
    FullTimeEmployees=db.Column(db.Integer, unique=False, index=False)
    PERatio=db.Column(db.Float, unique=False, index=False)
    EPS=db.Column(db.Float, unique=False, index=False)
    DividendYield=db.Column(db.Float, unique=False, index=False)
    QuarterlyEarningsGrowthYOY=db.Column(db.Float, unique=False, index=False)
    QuarterlyRevenueGrowthYOY=db.Column(db.Float, unique=False, index=False)
    fiftyTwoWeekHigh=db.Column(db.Float, unique=False, index=False)
    fiftyTwoWeekLow=db.Column(db.Float, unique=False, index=False)
    fiftyDayMovingAverage=db.Column(db.Float, unique=False, index=False)
    twohundredDayMovingAverage = db.Column(db.Float, unique=False, index=False)
    PercentInsiders=db.Column(db.Float, unique=False, index=False)
    PercentInstitutions=db.Column(db.Float, unique=False, index=False)
    avg10Volume=db.Column(db.Float, unique=False, index=False)
    avg30Volume=db.Column(db.Float, unique=False, index=False)
    year5ChangePercent=db.Column(db.Float, unique=False, index=False)
    year2ChangePercent=db.Column(db.Float, unique=False, index=False)
    year1ChangePercent=db.Column(db.Float, unique=False, index=False)
    month6ChangePercent=db.Column(db.Float, unique=False, index=False)
    month3ChangePercent=db.Column(db.Float, unique=False, index=False)
    month1ChangePercent=db.Column(db.Float, unique=False, index=False)
    day5ChangePercent=db.Column(db.Float, unique=False, index=False)
    nextEarningsDate=db.Column(db.String(64), unique=False)
    shareOutstanding = db.Column(db.Integer, unique=False, index=False)



class ArkgTable(db.Model):
    __tablename__ = "ArkgTable"
    id = db.Column(db.Integer, primary_key=True)
    
    date = db.Column(db.DateTime,index=False,unique=False, nullable=False)
    cusip = db.Column(db.String(36), unique=False)
    companyName = db.Column(db.String(64), unique=False)
    ticker = db.Column(db.String(64), index=False, unique=True, nullable=False)
    logo = db.Column(db.String(124), index=False, unique=False)
    weburl = db.Column(db.String(124), index=False)
    
    value = db.Column(db.Integer, unique=False, index=False)
    shares = db.Column(db.Integer, unique=False, index=False)
    weight = db.Column(db.Float, unique=False, index=False)
    
    price = db.Column(db.Float, unique=False, index=False)
    marketCap= db.Column(db.Integer, unique=False, index=False)
    
    FullTimeEmployees=db.Column(db.Integer, unique=False, index=False)
    PERatio=db.Column(db.Float, unique=False, index=False)
    EPS=db.Column(db.Float, unique=False, index=False)
    DividendYield=db.Column(db.Float, unique=False, index=False)
    QuarterlyEarningsGrowthYOY=db.Column(db.Float, unique=False, index=False)
    QuarterlyRevenueGrowthYOY=db.Column(db.Float, unique=False, index=False)
    fiftyTwoWeekHigh=db.Column(db.Float, unique=False, index=False)
    fiftyTwoWeekLow=db.Column(db.Float, unique=False, index=False)
    fiftyDayMovingAverage=db.Column(db.Float, unique=False, index=False)
    twohundredDayMovingAverage = db.Column(db.Float, unique=False, index=False)
    PercentInsiders=db.Column(db.Float, unique=False, index=False)
    PercentInstitutions=db.Column(db.Float, unique=False, index=False)
    avg10Volume=db.Column(db.Float, unique=False, index=False)
    avg30Volume=db.Column(db.Float, unique=False, index=False)
    year5ChangePercent=db.Column(db.Float, unique=False, index=False)
    year2ChangePercent=db.Column(db.Float, unique=False, index=False)
    year1ChangePercent=db.Column(db.Float, unique=False, index=False)
    month6ChangePercent=db.Column(db.Float, unique=False, index=False)
    month3ChangePercent=db.Column(db.Float, unique=False, index=False)
    month1ChangePercent=db.Column(db.Float, unique=False, index=False)
    day5ChangePercent=db.Column(db.Float, unique=False, index=False)
    nextEarningsDate=db.Column(db.String(64), unique=False)
    shareOutstanding = db.Column(db.Integer, unique=False, index=False)



class ArkfTable(db.Model):
    __tablename__ = "ArkfTable"
    id = db.Column(db.Integer, primary_key=True)
    
    date = db.Column(db.DateTime,index=False,unique=False, nullable=False)
    cusip = db.Column(db.String(36), unique=False)
    companyName = db.Column(db.String(64), unique=False)
    ticker = db.Column(db.String(64), index=False, unique=True, nullable=False)
    logo = db.Column(db.String(124), index=False, unique=False)
    weburl = db.Column(db.String(124), index=False)
    
    value = db.Column(db.Integer, unique=False, index=False)
    shares = db.Column(db.Integer, unique=False, index=False)
    weight = db.Column(db.Float, unique=False, index=False)
    
    price = db.Column(db.Float, unique=False, index=False)
    marketCap= db.Column(db.Integer, unique=False, index=False)
    
    FullTimeEmployees=db.Column(db.Integer, unique=False, index=False)
    PERatio=db.Column(db.Float, unique=False, index=False)
    EPS=db.Column(db.Float, unique=False, index=False)
    DividendYield=db.Column(db.Float, unique=False, index=False)
    QuarterlyEarningsGrowthYOY=db.Column(db.Float, unique=False, index=False)
    QuarterlyRevenueGrowthYOY=db.Column(db.Float, unique=False, index=False)
    fiftyTwoWeekHigh=db.Column(db.Float, unique=False, index=False)
    fiftyTwoWeekLow=db.Column(db.Float, unique=False, index=False)
    fiftyDayMovingAverage=db.Column(db.Float, unique=False, index=False)
    twohundredDayMovingAverage = db.Column(db.Float, unique=False, index=False)
    PercentInsiders=db.Column(db.Float, unique=False, index=False)
    PercentInstitutions=db.Column(db.Float, unique=False, index=False)
    avg10Volume=db.Column(db.Float, unique=False, index=False)
    avg30Volume=db.Column(db.Float, unique=False, index=False)
    year5ChangePercent=db.Column(db.Float, unique=False, index=False)
    year2ChangePercent=db.Column(db.Float, unique=False, index=False)
    year1ChangePercent=db.Column(db.Float, unique=False, index=False)
    month6ChangePercent=db.Column(db.Float, unique=False, index=False)
    month3ChangePercent=db.Column(db.Float, unique=False, index=False)
    month1ChangePercent=db.Column(db.Float, unique=False, index=False)
    day5ChangePercent=db.Column(db.Float, unique=False, index=False)
    nextEarningsDate=db.Column(db.String(64), unique=False)
    shareOutstanding = db.Column(db.Integer, unique=False, index=False)



class ArkwTable(db.Model):
    __tablename__ = "ArkwTable"
    id = db.Column(db.Integer, primary_key=True)
    
    date = db.Column(db.DateTime,index=False,unique=False, nullable=False)
    cusip = db.Column(db.String(36), unique=False)
    companyName = db.Column(db.String(64), unique=False)
    ticker = db.Column(db.String(64), index=False, unique=True, nullable=False)
    logo = db.Column(db.String(124), index=False, unique=False)
    weburl = db.Column(db.String(124), index=False)
    
    value = db.Column(db.Integer, unique=False, index=False)
    shares = db.Column(db.Integer, unique=False, index=False)
    weight = db.Column(db.Float, unique=False, index=False)
    
    price = db.Column(db.Float, unique=False, index=False)
    marketCap= db.Column(db.Integer, unique=False, index=False)
    
    FullTimeEmployees=db.Column(db.Integer, unique=False, index=False)
    PERatio=db.Column(db.Float, unique=False, index=False)
    EPS=db.Column(db.Float, unique=False, index=False)
    DividendYield=db.Column(db.Float, unique=False, index=False)
    QuarterlyEarningsGrowthYOY=db.Column(db.Float, unique=False, index=False)
    QuarterlyRevenueGrowthYOY=db.Column(db.Float, unique=False, index=False)
    fiftyTwoWeekHigh=db.Column(db.Float, unique=False, index=False)
    fiftyTwoWeekLow=db.Column(db.Float, unique=False, index=False)
    fiftyDayMovingAverage=db.Column(db.Float, unique=False, index=False)
    twohundredDayMovingAverage = db.Column(db.Float, unique=False, index=False)
    PercentInsiders=db.Column(db.Float, unique=False, index=False)
    PercentInstitutions=db.Column(db.Float, unique=False, index=False)
    avg10Volume=db.Column(db.Float, unique=False, index=False)
    avg30Volume=db.Column(db.Float, unique=False, index=False)
    year5ChangePercent=db.Column(db.Float, unique=False, index=False)
    year2ChangePercent=db.Column(db.Float, unique=False, index=False)
    year1ChangePercent=db.Column(db.Float, unique=False, index=False)
    month6ChangePercent=db.Column(db.Float, unique=False, index=False)
    month3ChangePercent=db.Column(db.Float, unique=False, index=False)
    month1ChangePercent=db.Column(db.Float, unique=False, index=False)
    day5ChangePercent=db.Column(db.Float, unique=False, index=False)
    nextEarningsDate=db.Column(db.String(64), unique=False)
    shareOutstanding = db.Column(db.Integer, unique=False, index=False)


class PrintTable(db.Model):
    __tablename__ = "PrintTable"
    id = db.Column(db.Integer, primary_key=True)
    
    date = db.Column(db.DateTime,index=False,unique=False, nullable=False)
    cusip = db.Column(db.String(36), unique=False)
    companyName = db.Column(db.String(64), unique=False)
    ticker = db.Column(db.String(64), index=False, unique=True, nullable=False)
    logo = db.Column(db.String(124), index=False, unique=False)
    weburl = db.Column(db.String(124), index=False)
    
    value = db.Column(db.Integer, unique=False, index=False)
    shares = db.Column(db.Integer, unique=False, index=False)
    weight = db.Column(db.Float, unique=False, index=False)
    
    price = db.Column(db.Float, unique=False, index=False)
    marketCap= db.Column(db.Integer, unique=False, index=False)
    
    FullTimeEmployees=db.Column(db.Integer, unique=False, index=False)
    PERatio=db.Column(db.Float, unique=False, index=False)
    EPS=db.Column(db.Float, unique=False, index=False)
    DividendYield=db.Column(db.Float, unique=False, index=False)
    QuarterlyEarningsGrowthYOY=db.Column(db.Float, unique=False, index=False)
    QuarterlyRevenueGrowthYOY=db.Column(db.Float, unique=False, index=False)
    fiftyTwoWeekHigh=db.Column(db.Float, unique=False, index=False)
    fiftyTwoWeekLow=db.Column(db.Float, unique=False, index=False)
    fiftyDayMovingAverage=db.Column(db.Float, unique=False, index=False)
    twohundredDayMovingAverage = db.Column(db.Float, unique=False, index=False)
    PercentInsiders=db.Column(db.Float, unique=False, index=False)
    PercentInstitutions=db.Column(db.Float, unique=False, index=False)
    avg10Volume=db.Column(db.Float, unique=False, index=False)
    avg30Volume=db.Column(db.Float, unique=False, index=False)
    year5ChangePercent=db.Column(db.Float, unique=False, index=False)
    year2ChangePercent=db.Column(db.Float, unique=False, index=False)
    year1ChangePercent=db.Column(db.Float, unique=False, index=False)
    month6ChangePercent=db.Column(db.Float, unique=False, index=False)
    month3ChangePercent=db.Column(db.Float, unique=False, index=False)
    month1ChangePercent=db.Column(db.Float, unique=False, index=False)
    day5ChangePercent=db.Column(db.Float, unique=False, index=False)
    nextEarningsDate=db.Column(db.String(64), unique=False)
    shareOutstanding = db.Column(db.Integer, unique=False, index=False)


class IzrlTable(db.Model):
    __tablename__ = "IzrlTable"
    id = db.Column(db.Integer, primary_key=True)
    
    date = db.Column(db.DateTime,index=False,unique=False, nullable=False)
    cusip = db.Column(db.String(36), unique=False)
    companyName = db.Column(db.String(64), unique=False)
    ticker = db.Column(db.String(64), index=False, unique=True, nullable=False)
    logo = db.Column(db.String(124), index=False, unique=False)
    weburl = db.Column(db.String(124), index=False)
    
    value = db.Column(db.Integer, unique=False, index=False)
    shares = db.Column(db.Integer, unique=False, index=False)
    weight = db.Column(db.Float, unique=False, index=False)
    
    price = db.Column(db.Float, unique=False, index=False)
    marketCap= db.Column(db.Integer, unique=False, index=False)
    
    FullTimeEmployees=db.Column(db.Integer, unique=False, index=False)
    PERatio=db.Column(db.Float, unique=False, index=False)
    EPS=db.Column(db.Float, unique=False, index=False)
    DividendYield=db.Column(db.Float, unique=False, index=False)
    QuarterlyEarningsGrowthYOY=db.Column(db.Float, unique=False, index=False)
    QuarterlyRevenueGrowthYOY=db.Column(db.Float, unique=False, index=False)
    fiftyTwoWeekHigh=db.Column(db.Float, unique=False, index=False)
    fiftyTwoWeekLow=db.Column(db.Float, unique=False, index=False)
    fiftyDayMovingAverage=db.Column(db.Float, unique=False, index=False)
    twohundredDayMovingAverage = db.Column(db.Float, unique=False, index=False)
    PercentInsiders=db.Column(db.Float, unique=False, index=False)
    PercentInstitutions=db.Column(db.Float, unique=False, index=False)
    avg10Volume=db.Column(db.Float, unique=False, index=False)
    avg30Volume=db.Column(db.Float, unique=False, index=False)
    year5ChangePercent=db.Column(db.Float, unique=False, index=False)
    year2ChangePercent=db.Column(db.Float, unique=False, index=False)
    year1ChangePercent=db.Column(db.Float, unique=False, index=False)
    month6ChangePercent=db.Column(db.Float, unique=False, index=False)
    month3ChangePercent=db.Column(db.Float, unique=False, index=False)
    month1ChangePercent=db.Column(db.Float, unique=False, index=False)
    day5ChangePercent=db.Column(db.Float, unique=False, index=False)
    nextEarningsDate=db.Column(db.String(64), unique=False)
    shareOutstanding = db.Column(db.Integer, unique=False, index=False)
