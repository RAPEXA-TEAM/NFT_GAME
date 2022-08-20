# How to run

1. Update mirrors `apt update`
2. Install GIT `apt install git`
3. Install MySQL `apt install mysql-server`
4. Clone the project `git clone https://github.com/RAPEXA-TEAM/NFT_GAME && cd NFT_GAME`
5. Go to Server directory `cd Server`
6. Make virtualenv `python -m virtualenv .venv`
7. Start virtualenv `source .venv/Scripts/activate`
8. Install Server requirements `pip install -r ../requirements.txt`
9. Open Terminal and start MySQl `mysql -u root -p`
10. Open mysql on Terminal and execute commands below :

- `CREATE DATABASE NFT_GAME;`
- `CREATE USER 'NFTUSER'@'localhost' IDENTIFIED BY 'NFTPASS';`
- `GRANT ALL PRIVILEGES ON NFT_GAME.* TO 'NFTUSER'@'localhost';`
- `exit;`

11. Config MySQL server `python MYSQL_DB.py execute`
12. Start Server `python Server.py`
13. Test Server `python TEST.py`