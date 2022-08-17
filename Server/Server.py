#!/usr/bin/env
from flask import Flask, request, jsonify
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from web3 import Web3

import pymysql
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