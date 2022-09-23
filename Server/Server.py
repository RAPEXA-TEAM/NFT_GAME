#!/usr/bin/env
from flask import Flask, request, jsonify, send_from_directory, render_template
import json
import requests
import hashlib
import random
import MYSQL_DB   #MYSQL MANAGER
import CONFIG     #SERVER CONGIG

list_tokens = []

for i in range(0,36001):
    list_tokens.append(i)

app = Flask(__name__)

# config
app.config.update(
    SECRET_KEY = CONFIG.SECRET_KEY
)

FLUTTER_WEB_APP = 'templates'

@app.route('/random_tokenid/06a750fd114f5fed65a8f507d0815666')
def handle_random_tokenid():
    '''this function return random tokenid''' 
    adad = random.choice(list_tokens)
    index = list_tokens.index(adad)
    list_tokens.pop(index)
    ret = {'status':'ok','code': str(adad)}
    return jsonify(ret)


@app.route('/login',methods=["GET", "POST"])
def handle_check_tokenid():
    '''this function check user and tokenid'''
    if request.method == 'POST':
        user = request.json["user"]
        TokenID = request.json["TokenID"]
        if Check_User(user,TokenID) :

            ret = {'status':'ok','code':'200'}
            return jsonify(ret) 

        else :
            
            ret = {'status':'failed','error':'user not exist'}
            return jsonify(ret)

    ret = {'status':'failed','error':'requests not valid'}
    return jsonify(ret)

@app.route('/web')
def render_page_web():
    return render_template('index.html')

@app.route('/web/<path:name>')
def return_flutter_doc(name):

    datalist = str(name).split('/')
    DIR_NAME = FLUTTER_WEB_APP

    if len(datalist) > 1:
        for i in range(0, len(datalist) - 1):
            DIR_NAME += '/' + datalist[i]

    return send_from_directory(DIR_NAME, datalist[-1])

@app.route('/')
def render_page():
    return render_template('/index.html')

@app.route("/ok",methods=["GET", "POST"])
def sys_check():
    '''this function check system'''
    if request.method == 'POST':
        password = request.json["pass"]
        hash_pass = hashlib.sha256(password.encode("utf-8")).hexdigest()
        if hash_pass == CONFIG.HASHPASS :
        
            ret = {'status':'ok','code':'200'}
            return jsonify(ret)
        
        ret = {'status':'failed','error':'password incorrect!'}
        return jsonify(ret)

    ret = {'status':'failed','error':'requests not valid'}
    return jsonify(ret)

@app.route('/create_user',methods=["GET", "POST"])
def handle_create_user():
    '''this function create user after check'''
    if request.method == 'POST':
        user = request.json["user"]
        TokenID = request.json["TokenID"]
        try :
            if Check_User(user,TokenID):
                if MYSQL_DB.write_user_to_database(user,TokenID):
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
        json_array = []
        List_Of_Users = MYSQL_DB.read_users_from_database()
        for user in List_Of_Users:

            id, user_db, TokenID, percentage = user
            json_messages[id] = {'user' : user_db,'TokenID' : TokenID,'percentage' : percentage}
            json_array.append(json.dumps({'user' : user_db,'TokenID' : TokenID,'percentage' : percentage}))

        Response = {'Code':"200" , 'users': json_messages}
        return jsonify(json_array)      

    except:
        
        ret = {'status':'failed','error':'connect to database failed'}
        return jsonify(ret)

#teturn : tokenid & user
@app.route('/winners',methods=["GET", "POST"])
def handle_winners():
    '''this function return winners'''
    
    try:
        
        json_messages = {}
        List_Of_Winers = MYSQL_DB.read_winners_from_database(CONFIG.SOURCE)
        List_Of_Users = MYSQL_DB.read_users_from_database()
        for winer in List_Of_Winers:
            id, user, TokenID = winer
            for user in List_Of_Users:
                id, user_db, TokenIDus, percentage = user
                if TokenID == TokenIDus:
                    json_messages[id] = {'TokenID' : TokenID, 'user' : user_db}
                    jsonStr = json.dumps({'TokenID' : TokenID, 'user' : user_db})

        Response = {'Code':"200" , 'users': json_messages}
        return jsonify(jsonStr)     

    except:
        
        ret = {'status':'failed','error':'connect to database failed'}
        return jsonify(ret)

@app.route('/all_messages',methods=["GET", "POST"])
def handle_messages():
    '''this function return all user messages'''
    try:

        json_messages = {}
        jsonStr = []
        List_Of_Messages = MYSQL_DB.read_users_messages()
        for message in List_Of_Messages:
            id_db, TokenID, message_db = message
            
            if TokenID != CONFIG.SOURCE:
                json_messages[id_db] = {'TokenID' : TokenID , 'Message' : message_db}
                jsonStr.append(json.dumps({'TokenID' : TokenID , 'Message' : message_db}))
            
            else :
                continue

        Response = {'Code':"200" , 'Messages': json_messages}
        return jsonify(jsonStr)      

    except:
        
        ret = {'status':'failed','error':'connect to database failed'}
        return jsonify(ret)

@app.route('/my_messages',methods=["GET", "POST"])
def handle_my_messages():
    '''this function return one user messages'''
    if request.method == 'POST':
        TokenID = request.json["TokenID"]
        json_messages = {}
        json_array = []
        List_Of_Messages = MYSQL_DB.read_users_messages()
        for message in List_Of_Messages:
            id_db, user_db, message_db = message
            if user_db == TokenID:
                json_messages[id_db] = {'Message' : message_db}
                json_array.append(json.dumps({'Message' : message_db}))

        Response = {'Code':"200" , 'Messages': json_messages}
        return jsonify(json_array)      

    ret = {'status':'failed','error':'requests not valid'}
    return jsonify(ret)

@app.route('/Send_message',methods=["GET","POST"])
def handle_send_message():
    '''this function is only for admin to send message to one user'''
    if request.method == "POST":
        TokenID = request.json["TokenID"]
        msg = request.json["message"]
        try:

            MYSQL_DB.write_user_message(TokenID,msg)
            ret = {'status':'ok','code':'200'}
            return jsonify(ret)

        except:

            ret = {'status':'failed','error':'requests not valid'}
            return jsonify(ret)
    
    ret = {'status':'failed','error':'requests not valid'}
    return jsonify(ret)

@app.route('/book',methods=["GET", "POST"])
def handle_book():
    '''this function return users'''
    if request.method == "POST":

        TokenID = request.json["TokenID"]
        Device = request.json["Device"]

        try:
            
            List_Of_Users = MYSQL_DB.read_users_from_database()
            for user in List_Of_Users:
                id, user_db, nft, percentage = user
                
                if Device == "L":

                    if TokenID == nft and percentage == CONFIG.LEVEL1:
                        Response = {'Code':"200" , 'level1': f"{CONFIG.LEVEL1_LINK_L}"}
                        return jsonify(Response)

                    if TokenID == nft and percentage == CONFIG.LEVEL2:
                        Response = {'Code':"200" , 'level1': f"{CONFIG.LEVEL1_LINK_L}" , 'level2': f"{CONFIG.LEVEL2_LINK_L}"}
                        return jsonify(Response)

                    if TokenID == nft and percentage == CONFIG.LEVEL3:
                        Response = {'Code':"200" , 'level1': f"{CONFIG.LEVEL1_LINK_L}" , 'level2': f"{CONFIG.LEVEL2_LINK_L}" , 'level3': f"{CONFIG.LEVEL3_LINK_L}"}
                        return jsonify(Response)

                    if TokenID == nft and percentage == CONFIG.LEVEL4:
                        Response = {'Code':"200" , 'level1': f"{CONFIG.LEVEL1_LINK_L}" , 'level2': f"{CONFIG.LEVEL2_LINK_L}" , 'level3': f"{CONFIG.LEVEL3_LINK_L}" , 'level4': f"{CONFIG.LEVEL4_LINK_L}"}
                        return jsonify(Response)
            
                    if TokenID == nft and percentage == CONFIG.LEVEL5:
                        Response = {'Code':"200" , 'level1': f"{CONFIG.LEVEL1_LINK_L}" , 'level2': f"{CONFIG.LEVEL2_LINK_L}" , 'level3': f"{CONFIG.LEVEL3_LINK_L}" , 'level4': f"{CONFIG.LEVEL4_LINK_L}" , 'level5': f"{CONFIG.LEVEL5_LINK_L}"}
                        return jsonify(Response)

                if Device == "P":

                    if TokenID == nft and percentage == CONFIG.LEVEL1:
                        Response = {'Code':"200" , 'level1': f"{CONFIG.LEVEL1_LINK_P}"}
                        return jsonify(Response)

                    if TokenID == nft and percentage == CONFIG.LEVEL2:
                        Response = {'Code':"200" , 'level1': f"{CONFIG.LEVEL1_LINK_P}" , 'level2': f"{CONFIG.LEVEL2_LINK_P}"}
                        return jsonify(Response)

                    if TokenID == nft and percentage == CONFIG.LEVEL3:
                        Response = {'Code':"200" , 'level1': f"{CONFIG.LEVEL1_LINK_P}" , 'level2': f"{CONFIG.LEVEL2_LINK_P}" , 'level3': f"{CONFIG.LEVEL3_LINK_P}"}
                        return jsonify(Response)

                    if TokenID == nft and percentage == CONFIG.LEVEL4:
                        Response = {'Code':"200" , 'level1': f"{CONFIG.LEVEL1_LINK_P}" , 'level2': f"{CONFIG.LEVEL2_LINK_P}" , 'level3': f"{CONFIG.LEVEL3_LINK_P}" , 'level4': f"{CONFIG.LEVEL4_LINK_P}"}
                        return jsonify(Response)
            
                    if TokenID == nft and percentage == CONFIG.LEVEL5:
                        Response = {'Code':"200" , 'level1': f"{CONFIG.LEVEL1_LINK_P}" , 'level2': f"{CONFIG.LEVEL2_LINK_P}" , 'level3': f"{CONFIG.LEVEL3_LINK_P}" , 'level4': f"{CONFIG.LEVEL4_LINK_P}" , 'level5': f"{CONFIG.LEVEL5_LINK_P}"}
                        return jsonify(Response)

        except:
            
            ret = {'status':'failed','error':'connect to database failed'}
            return jsonify(ret)

    ret = {'status':'failed','error':'requests not valid'}
    return jsonify(ret)

@app.route(f'/{CONFIG.LEVEL1_CODE}',methods=["GET", "POST"])
def handle_level_one_pass():
    '''This function pass level1 of games for one user'''
    if request.method == 'POST':
        TokenID = request.json["TokenID"]
        user = request.json["user"]
        List_Of_Users = MYSQL_DB.read_users_from_database()
        for user_dbb in List_Of_Users:
            id, user_db, TokenIDdb, percentage = user_dbb
            if TokenIDdb == TokenID and Check_User(user,TokenID):

                MYSQL_DB.update_user_percentage_in_database(TokenID,CONFIG.LEVEL1,CONFIG.LEVEL1_CODE)
                ret = {'status':'ok','code':'200'}
                return jsonify(ret)

            ret = {'status':'failed','error':'user or TokenID not valid'}
            return jsonify(ret)

    ret = {'status':'failed','error':'requests not valid'}
    return jsonify(ret)

@app.route(f'/{CONFIG.LEVEL2_CODE}',methods=["GET", "POST"])
def handle_level_two_pass():
    '''This function pass level2 of games for one user'''
    if request.method == 'POST':
        TokenID = request.json["TokenID"]
        user = request.json["user"]
        List_Of_Users = MYSQL_DB.read_users_from_database()
        for user_dbb in List_Of_Users:
            id, user_db, TokenIDdb, percentage = user_dbb
            if TokenIDdb == TokenID and percentage == CONFIG.LEVEL1 and Check_User(user_db,TokenID):

                MYSQL_DB.update_user_percentage_in_database(TokenID,CONFIG.LEVEL2,CONFIG.LEVEL2_CODE)
                ret = {'status':'ok','code':'200'}
                return jsonify(ret)

            ret = {'status':'failed','error':'user or TokenID not valid'}
            return jsonify(ret)

    ret = {'status':'failed','error':'requests not valid'}
    return jsonify(ret)

@app.route(f'/{CONFIG.LEVEL3_CODE}',methods=["GET", "POST"])
def handle_level_three_pass():
    '''This function pass level3 of games for one user'''
    if request.method == 'POST':
        TokenID = request.json["TokenID"]
        user = request.json["user"]
        List_Of_Users = MYSQL_DB.read_users_from_database()
        for user_dbb in List_Of_Users:
            id, user_db, TokenIDdb, percentage = user_dbb
            if TokenIDdb == TokenID and percentage == CONFIG.LEVEL2 and Check_User(user,TokenID):

                MYSQL_DB.update_user_percentage_in_database(TokenID,CONFIG.LEVEL3,CONFIG.LEVEL3_CODE)
                ret = {'status':'ok','code':'200'}
                return jsonify(ret)

            ret = {'status':'failed','error':'user or TokenID not valid'}
            return jsonify(ret)

    ret = {'status':'failed','error':'requests not valid'}
    return jsonify(ret)

@app.route(f'/{CONFIG.LEVEL4_CODE}',methods=["GET", "POST"])
def handle_level_four_pass():
    '''This function pass level4 of games for one user'''
    if request.method == 'POST':
        TokenID = request.json["TokenID"]
        user = request.json["user"]
        List_Of_Users = MYSQL_DB.read_users_from_database()
        for user_dbb in List_Of_Users:
            id, user_db, TokenIDdb, percentage = user_dbb
            if TokenIDdb == TokenID and percentage == CONFIG.LEVEL3 and Check_User(user,TokenID):

                MYSQL_DB.update_user_percentage_in_database(TokenID,CONFIG.LEVEL4,CONFIG.LEVEL4_CODE)
                ret = {'status':'ok','code':'200'}
                return jsonify(ret)

            ret = {'status':'failed','error':'user or TokenID not valid'}
            return jsonify(ret)

    ret = {'status':'failed','error':'requests not valid'}
    return jsonify(ret)

@app.route(f'/{CONFIG.LEVEL5_CODE}',methods=["GET", "POST"])
def handle_level_five_pass():
    '''This function pass level5 of games for one user'''
    if request.method == 'POST':
        TokenID = request.json["TokenID"]
        user = request.json["user"]
        try:
            List_Of_Users = MYSQL_DB.read_users_from_database()
            for user_dbb in List_Of_Users:
                id, user_db, TokenIDdb, percentage = user_dbb
                if TokenIDdb == TokenID and percentage == CONFIG.LEVEL4 and Check_User(user,TokenID):

                    MYSQL_DB.update_user_percentage_in_database(TokenID,CONFIG.LEVEL5,CONFIG.LEVEL5_CODE)
                    if Send_Winner(TokenID):
                            
                        ret = {'status':'ok','code':'200'}
                        return jsonify(ret)

                    else:

                        ret = {'status':'failed','error':'connect to database failed'}
                        return jsonify(ret)
                
            ret = {'status':'failed','error':'user or TokenID not valid'}
            return jsonify(ret)

        except:

            ret = {'status':'failed','error':'user didnt pass level 4'}
            return jsonify(ret)

    ret = {'status':'failed','error':'requests not valid'}
    return jsonify(ret)

def Send_Winner(TokenID):
    '''this function send message to winner'''
    
    admin_user = CONFIG.SOURCE
    message = f"Top Secret! ,congratulations dear, you have done all levels! ,please send [{TokenID}] code to [Greatspa81@gmail.com]."

    try:
        
        MYSQL_DB.write_user_message(TokenID,message)
        MYSQL_DB.write_user_message(admin_user,TokenID) # set winner - internal rule
        return True

    except:

        return False

def Check_User(user,TokenID):
    '''This function check user address and user nft to validate user'''
    
    contract = CONFIG.CONTRACT_ADDRESS
    apikey = CONFIG.APIKEY
    baseurl = CONFIG.APIURL
    query = f"?module=account&action=tokennfttx&contractaddress={contract}&address={user}&page=1&offset=100&startblock=0&endblock=99999999&sort=asc&apikey={apikey}"

    url = baseurl + query
    response = requests.get(url)

    try:

        if response.json()['result'][0]['tokenID'] == str(TokenID) : 
            return True

        else:
            return False

    except:
        return False

if __name__ == "__main__":
    app.run("0.0.0.0",80,debug=False)