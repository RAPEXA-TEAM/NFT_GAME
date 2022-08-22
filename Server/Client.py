# run this first :
# ---- python MYSQL_DB.py execute

#!/usr/bin/env
import requests

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
    print("[+] Test (read a user Messages) start.")
    route = "/my_messages"
    aa = {'user':user}
    print(f"[+] Test (read a user Messages) for [{user}].")
    r = requests.post(url = base_url+route, json=aa)
    print(f"[+] response : {r.text}")
    print("[+] Test (read a user Messages) done.")

def read_winners(base_url):
    print("[+] Test (read winners) start.")
    route = "/winners"
    r = requests.get(url =base_url+route)
    print(f"[+] response : {r.text}")
    print("[+] Test (read winners) start.")

if __name__ == "__main__":
    #ok(base_url)
    #create_user(base_url,user,nft_hash)
    #read_users(base_url)
    #Send_message(base_url,user)
    #read_user_messages(base_url,user)
    #read_all_messages(base_url)

    #read_winners(base_url)
    pass