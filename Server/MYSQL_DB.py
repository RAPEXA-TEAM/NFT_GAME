import pymysql
import CONFIG     #SERVER CONGIG

def connect_to_database():
    '''This function make a connection with datebase'''
    db = pymysql.connect(host=CONFIG.MYSQL_HOST,
                       user=CONFIG.MYSQL_USER,
                       passwd=CONFIG.MYSQL_PASS,
                       db=CONFIG.MYSQL_DATABAS)
    return(db)

def update_user_percentage_in_database(user,percentage):
    #TODO
    pass

def write_user_to_database(user):
    #TODO
    pass

def check_user_messages(user):
    #TODO
    pass

"CREATE DATABASE NFT_GAME;"

"CREATE USER 'NFTUSER'@'localhost' IDENTIFIED BY 'NFTPASS';"

"GRANT ALL PRIVILEGES ON NFT_GAME.* TO 'NFTUSER'@'localhost';"

"USE NFT_GAME;"

"DROP TABLE IF EXISTS Messages;"

"DROP TABLE IF EXISTS Users;"

"CREATE TABLE Messages (id INT NOT NULL AUTO_INCREMENT,user VARCHAR(260),message VARCHAR(1024), PRIMARY KEY(id));"

"CREATE TABLE Users (id INT NOT NULL AUTO_INCREMENT,user VARCHAR(260),percentage INT, PRIMARY KEY(id));"