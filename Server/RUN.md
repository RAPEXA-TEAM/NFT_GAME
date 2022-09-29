# How to run

1. Update mirrors `apt update`
2. Install GIT `apt install git`
3. Install MySQL `apt install mysql-server`
4. Clone the project `git clone https://github.com/RAPEXA-TEAM/NFT_GAME && cd NFT_GAME`
5. Go to Server directory `cd Server`
6. Make virtualenv `python3 -m virtualenv .venv`
7. Start virtualenv `source .venv\bin\activate`
8. Install Server requirements `pip3 install -r ../requirements.txt`
9. Open Terminal and start MySQl `mysql -u root -p`
10. Open mysql on Terminal and execute commands below :

- `CREATE DATABASE NFT_GAME;`
- `CREATE USER 'NFTUSER'@'localhost' IDENTIFIED BY 'NFTPASS';`
- `GRANT ALL PRIVILEGES ON NFT_GAME.* TO 'NFTUSER'@'localhost';`
- `exit;`

11. Config MySQL server `python3 MYSQL_DB.py execute`
12. Start Server `python3 Server.py`
13. Test Server `python3 Client.py`