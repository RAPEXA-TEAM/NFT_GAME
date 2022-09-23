# Notice :this file is for testing server on localhost
# run this first :
# ---- python MYSQL_DB.py execute

#!/usr/bin/env
import requests
import os

base_url = "http://127.0.0.1:5511"
user = "0x6B957a2791f6e88C99Ca0e58d866075430Daf31D" #TODO : change this with valid user in contract
TokenID = "4560"                                    #TODO : change this with valid token id that user had
password = '1234'

def ok(base_url,password):
    print("[+] Test basic login Server start.")
    route = "/ok"
    aa = {'pass':password}
    print(f"[+] Test basic login Server with password : {password}")
    r = requests.post(url = base_url+route, json=aa)
    print(f"[+] response : {r.text}")
    print("[+] Test basic login Server done.")

def create_user(base_url,user,TokenID):
    print("[+] Test (Create user) start.")
    route = "/create_user"
    aa = {'user':user , 'TokenID':TokenID}
    print(f"[+] Test (Create user) with user : {user}.")
    r = requests.post(url = base_url+route, json=aa)
    print(f"[+] response : {r.text}")
    print("[+] Test (Create user) done.")

def read_users(base_url):
    print("[+] Test (read users) start.")
    route = "/users"
    r = requests.get(url =base_url+route)
    print(f"[+] response : {r.text}")
    print("[+] Test (read users) start.")

def Send_message(base_url,TokenID):
    print("[+] Test (Send message) start.")
    route = "/Send_message"
    aa = {'TokenID':TokenID ,'message':'TEST'}
    print(f"[+] Test (Send message) to [{TokenID}].")
    r = requests.post(url = base_url+route, json=aa)
    print(f"[+] response : {r.text}")
    print("[+] Test (Send message) done.")

def read_user_messages(base_url,TokenID):
    print("[+] Test (read a user Messages) start.")
    route = "/my_messages"
    aa = {'TokenID':TokenID}
    print(f"[+] Test (read a user Messages) for [{user}].")
    r = requests.post(url = base_url+route, json=aa)
    print(f"[+] response : {r.text}")
    print("[+] Test (read a user Messages) done.")

def read_all_messages(base_url):
    print("[+] Test (read all Messages) start.")
    route = "/all_messages"
    r = requests.get(url =base_url+route)
    print(f"[+] response : {r.text}")
    print("[+] Test (read all Messages) start.")

def pass_level1(base_url,user,TokenID):
    print("[+] Test (Pass Level 1) start.")
    route = "/de96871ca5ea490075a009ebd50177a6210cc91186f145db7ec20093f881bee3"
    aa = {'TokenID':TokenID, 'user':user}
    print(f"[+] Test (Pass Level 1) for [{user}].")
    r = requests.post(url = base_url+route, json=aa)
    print(f"[+] response : {r.text}")
    print("[+] Test (Pass Level 1) done.")

def pass_level2(base_url,user,TokenID):
    print("[+] Test (Pass Level 2) start.")
    route = "/5e472b3f5aa7f44438b3d83fd72ee3fbf4411e88ced3e045d748176fb3e4403f"
    aa = {'TokenID':TokenID, 'user':user}
    print(f"[+] Test (Pass Level 2) for [{user}].")
    r = requests.post(url = base_url+route, json=aa)
    print(f"[+] response : {r.text}")
    print("[+] Test (Pass Level 2) done.")

def pass_level3(base_url,user,TokenID):
    print("[+] Test (Pass Level 3) start.")
    route = "/6e30d713bb138b798061ce581b23ecbc23eda84b7676820b5729cbe2035c9fdb"
    aa = {'TokenID':TokenID, 'user':user}
    print(f"[+] Test (Pass Level 3) for [{user}].")
    r = requests.post(url = base_url+route, json=aa)
    print(f"[+] response : {r.text}")
    print("[+] Test (Pass Level 3) done.")

def pass_level4(base_url,user,TokenID):
    print("[+] Test (Pass Level 4) start.")
    route = "/f25d0521e7fa4ef8cbd04ff2c6fe674c5d30c3ce194565a18002280fa51b5e67"
    aa = {'TokenID':TokenID, 'user':user}
    print(f"[+] Test (Pass Level 4) for [{user}].")
    r = requests.post(url = base_url+route, json=aa)
    print(f"[+] response : {r.text}")
    print("[+] Test (Pass Level 4) done.")

def pass_level5(base_url,user,TokenID):
    print("[+] Test (Pass Level 5) start.")
    route = "/d9c9ec77c2377df2be249eabc9413905ca5960608ade94d667497102b12942ba"
    aa = {'TokenID':TokenID, 'user':user}
    print(f"[+] Test (Pass Level 5) for [{user}].")
    r = requests.post(url = base_url+route, json=aa)
    print(f"[+] response : {r.text}")
    print("[+] Test (Pass Level 5) done.")

def read_winners(base_url):
    print("[+] Test (read winners) start.")
    route = "/winners"
    r = requests.get(url =base_url+route)
    print(f"[+] response : {r.text}")
    print("[+] Test (read winners) done.")

def book(base_url,TokenID):
    print("[+] Test (get book text) start.")
    route = "/book"
    aa = {'TokenID':TokenID , 'Device' : 'L'}
    print(f"[+] Test (get book text) for [{TokenID}].")
    r = requests.post(url = base_url+route, json=aa)
    print(f"[+] response : {r.text}")
    print("[+] Test (get book text) done.")

if __name__ == "__main__":
    ok(base_url,password)
    create_user(base_url,user,TokenID)
    read_users(base_url)
    Send_message(base_url,TokenID)
    read_user_messages(base_url,TokenID)
    read_all_messages(base_url)
    pass_level1(base_url,user,TokenID)
    book(base_url,TokenID)
    pass_level2(base_url,user,TokenID)
    book(base_url,TokenID)
    pass_level3(base_url,user,TokenID)
    book(base_url,TokenID)
    pass_level4(base_url,user,TokenID)
    book(base_url,TokenID)
    pass_level5(base_url,user,TokenID)
    book(base_url,TokenID)
    read_user_messages(base_url,TokenID)
    read_winners(base_url)
    print("[+] Test done.")
    os.system('python MYSQL_DB.py execute')