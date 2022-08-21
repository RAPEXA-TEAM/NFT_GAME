#!/usr/bin/env

from flask import Flask, request, jsonify
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from web3 import Web3
import MYSQL_DB   #MYSQL MANAGER
import CONFIG     #SERVER CONGIG

app = Flask(__name__)
w3 = Web3(Web3.HTTPProvider(CONFIG.W3_PROVIDER))

# config
app.config.update(
    SECRET_KEY = CONFIG.SECRET_KEY
)

limiter = Limiter(
    app,
    key_func=get_remote_address,
)

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
        try :
            if Check_User(user):
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

@app.route('/users',methods=["GET", "POST"])
def handle_users():
    '''this function return users'''
    
    try:
        
        json_messages = {}
        List_Of_Users = MYSQL_DB.read_users_from_database()
        for user in List_Of_Users:

            id, user_db, nft_hash, percentage = user
            json_messages[id] = {'user' : user_db,'nft' : nft_hash,'percentage' : percentage}

        Response = {'Code':200 , 'users': json_messages}
        return jsonify(Response)      

    except:
        
        ret = {'status':'failed','error':'connect to database failed'}
        return jsonify(ret)

@app.route('/winners',methods=["GET", "POST"])
def handle_winners():
    '''this function return users'''
    
    try:
        
        json_messages = {}
        List_Of_Winers = MYSQL_DB.read_winners_from_database(CONFIG.SOURCE)
        for winer in List_Of_Winers:

            id, user, winner_wallet = winer
            json_messages[id] = {'winner' : winner_wallet}

        Response = {'Code':200 , 'users': json_messages}
        return jsonify(Response)      

    except:
        
        ret = {'status':'failed','error':'connect to database failed'}
        return jsonify(ret)

@app.route('/all_messages',methods=["GET", "POST"])
def handle_messages():
    '''this function return all user messages'''
    try:

        json_messages = {}
        List_Of_Messages = MYSQL_DB.read_users_messages()
        for message in List_Of_Messages:
            id_db, user_db, message_db = message
            
            if message_db != CONFIG.SOURCE:
                json_messages[id_db] = {'Message' : message_db}
            
            else :
                continue

        Response = {'Code':200 , 'Messages': json_messages}
        return jsonify(Response)      

    except:
        
        ret = {'status':'failed','error':'connect to database failed'}
        return jsonify(ret)

@app.route('/my_messages',methods=["GET", "POST"])
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
    '''This function pass level1 of games for one user'''
    if request.method == 'POST':
        user = request.json["user"]
        MYSQL_DB.update_user_percentage_in_database(user,CONFIG.LEVEL1,CONFIG.LEVEL1_CODE)
        ret = {'status':'ok','code':'200'}
        return jsonify(ret)
    
    ret = {'status':'failed','error':'requests not valid'}
    return jsonify(ret)

@app.route(f'/{CONFIG.LEVEL2_CODE}',methods=["GET", "POST"])
def handle_level_two_pass():
    '''This function pass level2 of games for one user'''
    if request.method == 'POST':
        user = request.json["user"]
        user_last_level = MYSQL_DB.read_user_last_level_in_database(user)
        try:

            if user_last_level[0][2] == CONFIG.LEVEL1_CODE:
                MYSQL_DB.update_user_percentage_in_database(user,CONFIG.LEVEL2,CONFIG.LEVEL2_CODE)
                ret = {'status':'ok','code':'200'}
                return jsonify(ret)
        
        except:

            ret = {'status':'failed','error':'user didnt pass level1'}
            return jsonify(ret)

    ret = {'status':'failed','error':'requests not valid'}
    return jsonify(ret)

@app.route(f'/{CONFIG.LEVEL3_CODE}',methods=["GET", "POST"])
def handle_level_three_pass():
    '''This function pass level3 of games for one user'''
    if request.method == 'POST':
        user = request.json["user"]
        user_last_level = MYSQL_DB.read_user_last_level_in_database(user)
        try:

            if user_last_level[1][2] == CONFIG.LEVEL2_CODE:
                MYSQL_DB.update_user_percentage_in_database(user,CONFIG.LEVEL3,CONFIG.LEVEL3_CODE)
                ret = {'status':'ok','code':'200'}
                return jsonify(ret)
        
        except:

            ret = {'status':'failed','error':'user didnt pass level2'}
            return jsonify(ret)

    ret = {'status':'failed','error':'requests not valid'}
    return jsonify(ret)

@app.route(f'/{CONFIG.LEVEL4_CODE}',methods=["GET", "POST"])
def handle_level_four_pass():
    '''This function pass level4 of games for one user'''
    if request.method == 'POST':
        user = request.json["user"]
        user_last_level = MYSQL_DB.read_user_last_level_in_database(user)
        try:

            if user_last_level[2][2] == CONFIG.LEVEL3_CODE:
                MYSQL_DB.update_user_percentage_in_database(user,CONFIG.LEVEL4,CONFIG.LEVEL4_CODE)
                ret = {'status':'ok','code':'200'}
                return jsonify(ret)
        
        except:

            ret = {'status':'failed','error':'user didnt pass level3'}
            return jsonify(ret)

    ret = {'status':'failed','error':'requests not valid'}
    return jsonify(ret)

@app.route(f'/{CONFIG.LEVEL5_CODE}',methods=["GET", "POST"])
def handle_level_five_pass():
    '''This function pass level5 of games for one user'''
    if request.method == 'POST':
        user = request.json["user"]
        user_last_level = MYSQL_DB.read_user_last_level_in_database(user)
        try:

            if user_last_level[3][2] == CONFIG.LEVEL4_CODE:
                MYSQL_DB.update_user_percentage_in_database(user,CONFIG.LEVEL5,CONFIG.LEVEL5_CODE)
                ret = {'status':'ok','code':'200'}
                return jsonify(ret)
        
        except:

            ret = {'status':'failed','error':'user didnt pass level4'}
            return jsonify(ret)

    ret = {'status':'failed','error':'requests not valid'}
    return jsonify(ret)

@app.route(f'/{CONFIG.LEVEL6_CODE}',methods=["GET", "POST"])
def handle_level_six_pass():
    '''This function pass level6 of games for one user'''
    if request.method == 'POST':
        user = request.json["user"]
        user_last_level = MYSQL_DB.read_user_last_level_in_database(user)
        try:

            if user_last_level[4][2] == CONFIG.LEVEL5_CODE:

                MYSQL_DB.update_user_percentage_in_database(user,CONFIG.LEVEL6,CONFIG.LEVEL6_CODE)
                if Send_Winner(user):
                    
                    ret = {'status':'ok','code':'200'}
                    return jsonify(ret)

                else:

                    ret = {'status':'failed','error':'connect to database failed'}
                    return jsonify(ret)

        except:

            ret = {'status':'failed','error':'user didnt pass level4'}
            return jsonify(ret)

    ret = {'status':'failed','error':'requests not valid'}
    return jsonify(ret)

def Send_Winner(user):
    '''this function send message to winner'''
    
    admin_user = CONFIG.SOURCE
    message = f"Top Secret! ,congratulations dear, you have done all levels! ,please send your wallet address : [{user}] code to [Greatspa81@gmail.com]."

    try:
        
        MYSQL_DB.write_user_message(user,message)
        MYSQL_DB.write_user_message(admin_user,user) # set winner - internal rule
        return True

    except:

        return False

def Check_User(user):
    #TODO
    '''This function check user address and user nft to validate user'''
    contract = w3.eth.contract(address = CONFIG.CONTRACT_ADDRESS , abi = CONFIG.CONTRACT_ABI)
    BalanceOfUser = contract.functions.balanceOf(user).call()
    if BalanceOfUser == 0:
        return False
    else:
        return True

if __name__ == "__main__":
    app.run("0.0.0.0",5000,debug=True)