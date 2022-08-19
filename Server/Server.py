#!/usr/bin/env
from flask import Flask, request, jsonify
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from web3 import Web3

import MYSQL_DB   #MYSQL MANAGER
import CONFIG     #SERVER CONGIG

app = Flask(__name__)
#@limiter.limit("5 per minute")

# config
app.config.update(
    SECRET_KEY = CONFIG.SECRET_KEY
)

limiter = Limiter(
    app,
    key_func=get_remote_address,
)

w3 = Web3(Web3.HTTPProvider(CONFIG.ETH))

@app.route("/ok")
def sys_check():
    '''this function check system'''
    ret = {'status':'ok','code':'200'}
    return jsonify(ret)

@app.route('/create_user',methods=["GET", "POST"])
def handle_create_user():
    '''this function create user after check'''
    if request.method == 'POST':
        user = request.json["user"]
        nfthash = request.json["nfthash"]
        try :
            if Check_User(user,nfthash):
                if MYSQL_DB.write_user_to_database(user,nfthash):
                    ret = {'status':'ok','code':'200'}
                    return jsonify(ret)
                else :
                    ret = {'status':'failed','error':'writing user to database'}
                    return jsonify(ret)
            else:
                ret = {'status':'failed','error':'user not valid'}
                return jsonify(ret)
        except:
            ret = {'status':'failed','error':'user not valid'}
            return jsonify(ret)

    ret = {'status':'failed','error':'requests not valid'}
    return jsonify(ret)

@app.route('/messages',methods=["GET", "POST"])
def handle_messages():
    '''this function return one user messages'''
    if request.method == 'POST':
        user = request.json["user"]
        json_messages = {}
        List_Of_Messages = MYSQL_DB.read_users_messages()
        for message in List_Of_Messages:
            id_db, user_db, message_db = message
            if user_db == user:
                json_messages[id_db] = {'Message' : message_db}
        
        Response = {'Code':200 , 'Messages': json_messages}
        return jsonify(Response)      

    ret = {'status':'failed','error':'requests not valid'}
    return jsonify(ret)

@app.route('/Send_message',methods=["GET","POST"])
def handle_send_message():
    '''this function is only for admin to send message to one user'''
    if request.method == "POST":
        user = request.json["user"]
        msg = request.json["message"]
        try:

            MYSQL_DB.write_user_message(user,msg)
            ret = {'status':'ok','code':'200'}
            return jsonify(ret)

        except:

            ret = {'status':'failed','error':'requests not valid'}
            return jsonify(ret)
    
    ret = {'status':'failed','error':'requests not valid'}
    return jsonify(ret)


@app.route(f'/{CONFIG.LEVEL1_CODE}',methods=["GET", "POST"])
def handle_level_one_pass():
    if request.method == 'POST':
        user = request.json["user"]
        MYSQL_DB.update_user_percentage_in_database(user,CONFIG.LEVEL1,CONFIG.LEVEL1_CODE)
    #TODO
    pass

@app.route(f'/{CONFIG.LEVEL2_CODE}',methods=["GET", "POST"])
def handle_level_two_pass():
    if request.method == 'POST':
        user = request.json["user"]
        MYSQL_DB.update_user_percentage_in_database(user,CONFIG.LEVEL2,CONFIG.LEVEL2_CODE)
    #TODO
    pass

@app.route(f'/{CONFIG.LEVEL3_CODE}',methods=["GET", "POST"])
def handle_level_three_pass():
    if request.method == 'POST':
        user = request.json["user"]
        MYSQL_DB.update_user_percentage_in_database(user,CONFIG.LEVEL3,CONFIG.LEVEL3_CODE)
    #TODO
    pass

@app.route(f'/{CONFIG.LEVEL4_CODE}',methods=["GET", "POST"])
def handle_level_four_pass():
    if request.method == 'POST':
        user = request.json["user"]
        MYSQL_DB.update_user_percentage_in_database(user,CONFIG.LEVEL4,CONFIG.LEVEL4_CODE)
    #TODO
    pass

@app.route(f'/{CONFIG.LEVEL5_CODE}',methods=["GET", "POST"])
def handle_level_five_pass():
    if request.method == 'POST':
        user = request.json["user"]
        MYSQL_DB.update_user_percentage_in_database(user,CONFIG.LEVEL5,CONFIG.LEVEL5_CODE)
    #TODO
    pass

@app.route(f'/{CONFIG.LEVEL6_CODE}',methods=["GET", "POST"])
def handle_level_six_pass():
    if request.method == 'POST':
        user = request.json["user"]
        MYSQL_DB.update_user_percentage_in_database(user,CONFIG.LEVEL6,CONFIG.LEVEL6_CODE)
    #TODO
    pass

def Check_User(user,nfthash):
    #TODO
    #try:
    #    TX = w3.eth.get_transaction(str(TXHASH))
    #    TX_FROM = TX["from"]
    #    TX_VALUE = TX["value"]
    #    if check:
    #        return True            
    #    else :
    #        return False
    
    #except:
    #    return False
    return True

if __name__ == "__main__":
    app.run("0.0.0.0",5000,debug=True)