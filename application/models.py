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

class ArkkTable(db.Model):
    __tablename__ = "ArkkTable"
    id = db.Column(db.Integer, primary_key=True)
    ticker = db.Column(db.String(64), index=False, unique=True, nullable=False)
    date = db.Column(db.DateTime,index=False,unique=False, nullable=False)
    shares = db.Column(db.Integer, unique=False, index=False)
    weight = db.Column(db.Integer, unique=False, index=False)
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
    value = db.Column(db.Integer, unique=False, index=False)

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
    weight = db.Column(db.Integer, unique=False, index=False)
    value = db.Column(db.Integer, unique=False, index=False)

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
    weight = db.Column(db.Integer, unique=False, index=False)
    value = db.Column(db.Integer, unique=False, index=False)

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
    weight = db.Column(db.Integer, unique=False, index=False)
    value = db.Column(db.Integer, unique=False, index=False)

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
    weight = db.Column(db.Integer, unique=False, index=False)
    value = db.Column(db.Integer, unique=False, index=False)

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
    weight = db.Column(db.Integer, unique=False, index=False)
    value = db.Column(db.Integer, unique=False, index=False)

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
    weight = db.Column(db.Integer, unique=False, index=False)
    value = db.Column(db.Integer, unique=False, index=False)


    def __str__(self):
        return f"{self.id}: ticker: {self.ticker} date: {self.date} shares: {self.shares} cusip{self.cusip} companyName: {self.companyName}"
