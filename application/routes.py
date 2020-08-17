from flask import request, render_template, make_response, jsonify
from datetime import datetime as dt
from flask import current_app as app
from .models import *
from .data import *
import uuid
import requests

#helper to check if key parameter is in the users db
def isKeyValid(key):
    return (User.query.filter_by(accessKey=key).first() != None)


#-------------Routes--------------------#

@app.route('/', methods=['GET'])
def sign_up():
    """Create a user via query string parameters."""
    email = request.args.get('email')
    if email:
        #check username is in db.
        if(User.query.filter_by(username=email).first() != None):
            apiAccessKey = User.query.filter_by(username=email).first().accessKey
            return render_template("userAccessKey.html", username=email, apiAccessKey=apiAccessKey)
    
        #generate api access key for user
        apiAccessKey = str(uuid.uuid4())
        #create new user and commit to db

        new_user = User(username=email,accessKey=str(apiAccessKey), created=dt.now(),admin=False)
        print("HERE")
        db.session.add(new_user)  # Adds new User record to database
        db.session.commit()  # Commits all changes
        return render_template("userAccessKey.html", username=email, apiAccessKey=apiAccessKey)
    
    return render_template("index.html")

@app.route('/applePie')
def initDBRoute():
    initDBv2()
    ArkkHoldings = ArkkTable.query.all()
    
    ArkqHoldings = ArkqTable.query.all()
    
    ArkgHoldings = ArkgTable.query.all()
    
    ArkfHoldings = ArkfTable.query.all()
    
    ArkwHoldings = ArkwTable.query.all()
    
    PRINTHoldings = PrintTable.query.all()
    
    IZRLHoldings = IzrlTable.query.all()
    return render_template("updateDB.html", ArkkQuery=ArkkHoldings, ArkqQuery=ArkqHoldings, ArkgQuery=ArkgHoldings, ArkfQuery=ArkfHoldings, ArkwQuery=ArkwHoldings, PrintQuery=PRINTHoldings,IzrlQuery=IZRLHoldings)

#This method is used to update all the data in the database
"""
@app.route('/applePie')
def routeUpdateData():
    
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
    

    #return render_template("updateDB.html", ArkkQuery=ArkkHoldings)
    return render_template("updateDB.html", ArkkQuery=ArkkHoldings, ArkqQuery=ArkqHoldings, ArkgQuery=ArkgHoldings, ArkfQuery=ArkfHoldings, ArkwQuery=ArkwHoldings, PrintQuery=PRINTHoldings,IzrlQuery=IZRLHoldings)
"""

@app.route('/All/<key>')
def routeAll(key):
    if(isKeyValid(key)):
        return make_response(jsonify(getDatafromAllStocks()), 200)
    return make_response(jsonify({"invalid" : "key :/"}), 400)

@app.route('/ARKK/<key>')
def routeARKK(key):
    if(isKeyValid(key)):
        print(User.query.filter_by(accessKey=key).first().username)
        print("test of getarkkdata")
        return make_response(jsonify(getDataFromDB(ArkkTable, "ARKK")), 200)
    return make_response(jsonify({"invalid" : "key :/"}), 400)


@app.route('/ARKQ/<key>')
def routeARKQ(key):
    if(isKeyValid(key)):
        return make_response(jsonify(getDataFromDB(ArkqTable, "ARKQ")), 200)
    return make_response(jsonify({"invalid" : "key :/"}), 400)


@app.route('/ARKW/<key>')
def routeARKW(key):
    if(isKeyValid(key)):
        return make_response(jsonify(getDataFromDB(ArkwTable, "ARKW")), 200)
    return make_response(jsonify({"invalid" : "key :/"}), 400)

@app.route('/ARKG/<key>')
def routeARKG(key):
    if(isKeyValid(key)):
        return make_response(jsonify(getDataFromDB(ArkgTable, "ARKG")), 200)
    return make_response(jsonify({"invalid" : "key :/"}), 400)

@app.route('/ARKF/<key>')
def routeARKF(key):
    if(isKeyValid(key)):
        return make_response(jsonify(getDataFromDB(ArkfTable, "ARKF")), 200)
    return make_response(jsonify({"invalid" : "key :/"}), 400)

@app.route('/PRINT/<key>')
def routePRINT(key):
    if(isKeyValid(key)):
        return make_response(jsonify(getDataFromDB(PrintTable, "PRINT")), 200)
    return make_response(jsonify({"invalid" : "key :/"}), 400)

@app.route('/IZRL/<key>')
def routeIZRL(key):
    if(isKeyValid(key)):
        return make_response(jsonify(getDataFromDB(IzrlTable, "IZRL")), 200)
    return make_response(jsonify({"invalid" : "key :/"}), 400)


