import os
import CONFIG

os.system("pip3 install pymysql")

import pymysql

os.system("pip3 install -r ..\\requirements.txt")

# Connection parameters and access credentials
ipaddress   = CONFIG.MYSQL_HOST  # MySQL server is running on local machine
usr_root         = "root"       
passwd_root      = ""            
charset     = "utf8mb4"     
curtype    = pymysql.cursors.DictCursor

# Define a method to create a database connection
def getDatabaseConnection(ipaddress, usr, passwd, charset, curtype):
    sqlCon  = pymysql.connect(host=ipaddress, user=usr, password=passwd, charset=charset, cursorclass=curtype);
    return sqlCon

# Define a method to create MySQL users
def createUser(cursor, userName, password,
               querynum=0, 
               updatenum=0, 
               connection_num=0):
    try:
        sqlCreateUser = "CREATE USER '%s'@'localhost' IDENTIFIED BY '%s';"%(userName, password)
        cursor.execute(sqlCreateUser)
        print("[+] Done creating MYSQL User...")
    except Exception as Ex:
        print("[-] Error creating MySQL User: %s"%(Ex))    

mySQLConnection = getDatabaseConnection(ipaddress, usr_root, passwd_root, charset, curtype)
mySQLCursor     = mySQLConnection.cursor()
createUser(mySQLCursor, CONFIG.MYSQL_USER, CONFIG.MYSQL_PASS)
mySQLConnection.commit()
mySQLConnection.close()

db = getDatabaseConnection(ipaddress, usr_root, passwd_root, charset, curtype)
mycursor = db.cursor()
mycursor.execute(f"CREATE DATABASE {CONFIG.MYSQL_DATABAS}")
db.commit()
db.close()

connection = getDatabaseConnection(ipaddress, usr_root, passwd_root, charset, curtype)
mycursor = connection.cursor()
mycursor.execute(f"GRANT ALL PRIVILEGES ON {CONFIG.MYSQL_DATABAS}.* TO '{CONFIG.MYSQL_USER}'@'localhost';")
mycursor.execute("Flush Privileges")
connection.commit()
connection.close()

os.system('python3 MYSQL_DB.py execute')
os.system("python3 Server.py")