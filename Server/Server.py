#!/usr/bin/env
from flask import Flask, request, jsonify
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from web3 import Web3

import MYSQL_DB   #MYSQL MANAGER
import CONFIG     #SERVER CONGIG

app = Flask(__name__)

# config
app.config.update(
    SECRET_KEY = CONFIG.secret_key
)

limiter = Limiter(
    app,
    key_func=get_remote_address,
)

w3 = Web3(Web3.HTTPProvider(CONFIG.ETH))

@app.route("/ok")
def sys_check():
    '''this function is for check system'''
    ret = {'status':'ok','code':'200'}
    return jsonify(ret)

@app.route('/start_game',methods=["GET", "POST"])
def handle_start_game():
    if request.method == 'POST':
        user = request.form["user"]
        MYSQL_DB.write_user_to_database(user)
    #TODO
    pass

@app.route('/level_one_pass',methods=["GET", "POST"])
def handle_level_one_pass():
    if request.method == 'POST':
        user = request.form["user"]
        MYSQL_DB.update_user_percentage_in_database(user,15)
    #TODO
    pass

@app.route('/level_two_pass',methods=["GET", "POST"])
def handle_level_two_pass():
    if request.method == 'POST':
        user = request.form["user"]
        MYSQL_DB.update_user_percentage_in_database(user,15)
    #TODO
    pass

@app.route('/level_three_pass',methods=["GET", "POST"])
def handle_level_three_pass():
    if request.method == 'POST':
        user = request.form["user"]
        MYSQL_DB.update_user_percentage_in_database(user,15)
    #TODO
    pass

@app.route('/level_four_pass',methods=["GET", "POST"])
def handle_level_four_pass():
    if request.method == 'POST':
        user = request.form["user"]
        MYSQL_DB.update_user_percentage_in_database(user,15)
    #TODO
    pass

@app.route('/level_five_pass',methods=["GET", "POST"])
def handle_level_five_pass():
    if request.method == 'POST':
        user = request.form["user"]
        MYSQL_DB.update_user_percentage_in_database(user,20)
    #TODO
    pass

@app.route('/level_six_pass',methods=["GET", "POST"])
def handle_level_six_pass():
    if request.method == 'POST':
        user = request.form["user"]
        MYSQL_DB.update_user_percentage_in_database(user,20)
    #TODO
    pass

@app.route('/messages',methods=["GET", "POST"])
@limiter.limit("5 per minute")
def handle_messages():
    if request.method == 'POST':
        user = request.form["user"]
        json_messages = {}
        List_Of_Messages = MYSQL_DB.check_user_messages(user)
        for message in List_Of_Messages:
            id_db, user_db, message_db = message
            json_messages[id_db] = {'Message' : message_db}
        Response = {'Code':200 , 'Messages': json_messages}
        return jsonify(Response)      
    return "ERROR"

if __name__ == "__main__":
    app.run("0.0.0.0",5000,debug=True)