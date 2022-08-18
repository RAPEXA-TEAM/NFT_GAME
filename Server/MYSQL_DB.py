import sys
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
    print("[+] Drop all tables")
    db = connect_to_database()
    cur = db.cursor()                       
    qury = "CREATE TABLE Messages (id INT NOT NULL AUTO_INCREMENT,user VARCHAR(260),message VARCHAR(1024), PRIMARY KEY(id));"
    cur.execute(qury)
    db.commit()
    db.close()
    print("[+] Create Messages table")
    db = connect_to_database()
    cur = db.cursor()                       
    qury = "CREATE TABLE Users (id INT NOT NULL AUTO_INCREMENT,user VARCHAR(260),percentage INT, PRIMARY KEY(id));"
    cur.execute(qury)
    db.commit()
    db.close()
    print("[+] Create Users table")
    return True

if sys.argv[1] == "execute":
    if Make_Database():
        print("[+] Done!")
    else :
        print("[-] Error...")