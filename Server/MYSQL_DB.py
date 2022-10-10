#!/usr/bin/env
import sys
import pymysql
import CONFIG  # SERVER CONGIG


def connect_to_database():
    '''This function make a connection with datebase'''
    db = pymysql.connect(host=CONFIG.MYSQL_HOST,
                         user=CONFIG.MYSQL_USER,
                         passwd=CONFIG.MYSQL_PASS,
                         db=CONFIG.MYSQL_DATABAS)
    return (db)


def update_user_percentage_in_database(TokenID, percentage, level):
    '''This function handle each level up MySQL query'''
    db = connect_to_database()
    cur = db.cursor()
    qury = f'INSERT INTO Timestamps (id, TokenID, level) VALUES  (null,"{TokenID}","{level}");'
    cur.execute(qury)
    db.commit()
    db.close()
    db = connect_to_database()
    cur = db.cursor()
    qury = f'UPDATE Users SET percentage = {percentage} WHERE TokenID = "{TokenID}";'
    cur.execute(qury)
    db.commit()
    db.close()


def find_user(TokenID):
    '''This function handle each level up MySQL query'''
    db = connect_to_database()
    cur = db.cursor()
    cur.execute(f'SELECT * FROM Users WHERE TokenID = "{TokenID}";')
    db.close()
    return cur.fetchone()


def read_user_last_level_in_database(TokenID):
    '''this function return one user level passed'''
    db = connect_to_database()
    cur = db.cursor()
    qury = f' select * from timestamps where TokenID = "{TokenID}";'
    cur.execute(qury)
    db.close()
    return cur.fetchall()


def write_user_to_database(user, TokenID):
    '''this function create user on database'''
    db = connect_to_database()
    cur = db.cursor()
    qury = f'INSERT INTO Users (user, TokenID, percentage) VALUES ("{user}", "{TokenID}", 10);'
    cur.execute(qury)
    db.commit()
    db.close()
    return True


def read_users_from_database():
    '''this function return all Users informations'''
    db = connect_to_database()
    cur = db.cursor()
    qury = f' select * from Users;'
    cur.execute(qury)
    db.close()
    return cur.fetchall()


def read_winners_from_database(source):
    '''this function return winners wallets '''
    db = connect_to_database()
    cur = db.cursor()
    cur.execute(f'SELECT * FROM Messages where TokenID = "{source}";')
    db.close()
    return cur.fetchall()


def read_users_messages():
    '''this function return user messages from database'''
    db = connect_to_database()
    cur = db.cursor()
    cur.execute(f"SELECT * FROM Messages;")
    db.close()
    return cur.fetchall()


def write_user_message(TokenID, msg):
    '''this function write user messages to database'''
    db = connect_to_database()
    cur = db.cursor()
    cur.execute(f'INSERT INTO messages (id, TokenID, message) VALUES (null, "{TokenID}", "{msg}");')
    db.commit()
    db.close()


def Make_Database():
    '''This function make database'''
    print("[+] Connecting to MySQl Server")
    db = connect_to_database()
    print("[+] Connected to MySQL Server")
    cur = db.cursor()
    qury = "DROP TABLE IF EXISTS Messages;"
    cur.execute(qury)
    db.commit()
    db.close()
    db = connect_to_database()
    cur = db.cursor()
    qury = "DROP TABLE IF EXISTS Users;"
    cur.execute(qury)
    db.commit()
    db.close()
    db = connect_to_database()
    cur = db.cursor()
    qury = "DROP TABLE IF EXISTS timestamps;"
    cur.execute(qury)
    db.commit()
    db.close()
    print("[+] Drop all tables")
    db = connect_to_database()
    cur = db.cursor()
    qury = "CREATE TABLE Messages (id INT NOT NULL AUTO_INCREMENT,TokenID VARCHAR(260),message VARCHAR(1024), PRIMARY KEY(id));"
    cur.execute(qury)
    db.commit()
    db.close()
    print("[+] Create Messages table")
    db = connect_to_database()
    cur = db.cursor()
    qury = "CREATE TABLE Users (id INT NOT NULL AUTO_INCREMENT,user VARCHAR(260),TokenID VARCHAR(60),percentage INT, PRIMARY KEY(id));"
    cur.execute(qury)
    db.commit()
    db.close()
    print("[+] Create Users table")
    db = connect_to_database()
    cur = db.cursor()
    qury = "CREATE TABLE Timestamps (id INT NOT NULL AUTO_INCREMENT,TokenID VARCHAR(260),level VARCHAR(260),date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP, PRIMARY KEY(id));"
    cur.execute(qury)
    db.commit()
    db.close()
    print("[+] Create Timestamps table")
    return True


try:
    if sys.argv[1] == "execute":
        if Make_Database():
            print("[+] Done!")
        else:
            print("[-] Error...")
except:
    pass
