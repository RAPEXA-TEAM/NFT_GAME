# Notice :this file is for testing server on localhost
# run this first :
# ---- python MYSQL_DB.py execute

#!/usr/bin/env
import requests
import os

#TODO
base_url = "http://127.0.0.1:5000"
user = "0xC883A79E8e4594C4f89434EDb754a10Da2311139"
nft_hash = "e50b08fa1a1ceeec6bc85381020e99eb"

def ok(base_url):
    print("[+] Test Server start.")
    route = "/ok"
    r = requests.get(url =base_url+route)
    print(f"[+] response : {r.text}")
    print("[+] Test Server done.")

def create_user(base_url,user,nft_hash):
    print("[+] Test (Create user) start.")
    route = "/create_user"
    aa = {'user':user , 'nfthash':nft_hash}
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

def Send_message(base_url,user):
    print("[+] Test (Send message) start.")
    route = "/Send_message"
    aa = {'user':user ,'message':'TEST'}
    print(f"[+] Test (Send message) to [{user}].")
    r = requests.post(url = base_url+route, json=aa)
    print(f"[+] response : {r.text}")
    print("[+] Test (Send message) done.")

def read_user_messages(base_url,user):
    print("[+] Test (read a user Messages) start.")
    route = "/my_messages"
    aa = {'user':user}
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

def pass_level1(base_url,user):
    print("[+] Test (Pass Level 1) start.")
    route = "/de96871ca5ea490075a009ebd50177a6210cc91186f145db7ec20093f881bee3"
    aa = {'user':user}
    print(f"[+] Test (Pass Level 1) for [{user}].")
    r = requests.post(url = base_url+route, json=aa)
    print(f"[+] response : {r.text}")
    print("[+] Test (Pass Level 1) done.")

def pass_level2(base_url,user):
    print("[+] Test (Pass Level 2) start.")
    route = "/5e472b3f5aa7f44438b3d83fd72ee3fbf4411e88ced3e045d748176fb3e4403f"
    aa = {'user':user}
    print(f"[+] Test (Pass Level 2) for [{user}].")
    r = requests.post(url = base_url+route, json=aa)
    print(f"[+] response : {r.text}")
    print("[+] Test (Pass Level 2) done.")

def pass_level3(base_url,user):
    print("[+] Test (Pass Level 3) start.")
    route = "/6e30d713bb138b798061ce581b23ecbc23eda84b7676820b5729cbe2035c9fdb"
    aa = {'user':user}
    print(f"[+] Test (Pass Level 3) for [{user}].")
    r = requests.post(url = base_url+route, json=aa)
    print(f"[+] response : {r.text}")
    print("[+] Test (Pass Level 3) done.")

def pass_level4(base_url,user):
    print("[+] Test (Pass Level 4) start.")
    route = "/f25d0521e7fa4ef8cbd04ff2c6fe674c5d30c3ce194565a18002280fa51b5e67"
    aa = {'user':user}
    print(f"[+] Test (Pass Level 4) for [{user}].")
    r = requests.post(url = base_url+route, json=aa)
    print(f"[+] response : {r.text}")
    print("[+] Test (Pass Level 4) done.")

def pass_level5(base_url,user):
    print("[+] Test (Pass Level 5) start.")
    route = "/d9c9ec77c2377df2be249eabc9413905ca5960608ade94d667497102b12942ba"
    aa = {'user':user}
    print(f"[+] Test (Pass Level 5) for [{user}].")
    r = requests.post(url = base_url+route, json=aa)
    print(f"[+] response : {r.text}")
    print("[+] Test (Pass Level 5) done.")

def pass_level6(base_url,user):
    print("[+] Test (Pass Level 6) start.")
    route = "/b5f9c2da0c206aee28ab92cfc00cdb1e97d01c8987f1bb7c9f4735ddf4d13a8b"
    aa = {'user':user}
    print(f"[+] Test (Pass Level 6) for [{user}].")
    r = requests.post(url = base_url+route, json=aa)
    print(f"[+] response : {r.text}")
    print("[+] Test (Pass Level 6) done.")

def read_winners(base_url):
    print("[+] Test (read winners) start.")
    route = "/winners"
    r = requests.get(url =base_url+route)
    print(f"[+] response : {r.text}")
    print("[+] Test (read winners) done.")

if __name__ == "__main__":
    ok(base_url)
    create_user(base_url,user,nft_hash)
    read_users(base_url)
    Send_message(base_url,user)
    read_user_messages(base_url,user)
    read_all_messages(base_url)
    pass_level1(base_url,user)
    pass_level2(base_url,user)
    pass_level3(base_url,user)
    pass_level4(base_url,user)
    pass_level5(base_url,user)
    pass_level6(base_url,user)
    read_user_messages(base_url,user)
    read_winners(base_url)
    print("[+] Test done.")
    os.system('python MYSQL_DB.py execute')