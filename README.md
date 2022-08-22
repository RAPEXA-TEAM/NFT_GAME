# NFT_GAME

[![LICENSE](https://img.shields.io/badge/LICENSE-MIT-green)](https://github.com/RAPEXA-TEAM/NFT_GAME/blob/main/LICENSE) 
[![Requirements](https://img.shields.io/badge/Requirements-See%20Here-orange)](https://github.com/RAPEXA-TEAM/NFT_GAME/blob/main/requirements.txt)
[![Todo](https://img.shields.io/badge/Todo-See%20Here-success)](https://github.com/RAPEXA-TEAM/NFT_GAME/blob/main/TODO.md)

The mysterious and obscure game of NFTs, participate in the game, just buy one of the NFTs!

## Technologies

- Solidity
- Truffle
- Flutter
- Flask
- Python
- Mysql
- Rest api

## How to run

- For WebServer follow [Server/RUN.md](https://github.com/RAPEXA-TEAM/NFT_GAME/blob/main/Server/RUN.md)
- For Client follow [Clients/RUN.md](https://github.com/RAPEXA-TEAM/NFT_GAME/blob/main/Clients/RUN.md)
- For Contract follow [Contract/RUN.md](https://github.com/RAPEXA-TEAM/NFT_GAME/blob/main/Contract/RUN.md)

## API

1.  route("/ok",methods=["GET"])                                                                - NULL         - {'code':'200', 'status':'ok'}
2.  route('/users',methods=["GET"])                                                             - NULL         - {'Code':'200', 'users': {"{id}" : {'user' : "{user_db}",'nft' : "{nft_hash}",'percentage' : "{percentage}"}}}
3.  route('/winners',methods=["GET"])                                                           - NULL         - {'Code':'200', 'users': {'{id}' = {'winner' : '{winner_wallet}'}}}
4.  route('/all_messages',methods=["GET"])                                                      - NULL         - {'Code':'200', 'Messages': {"{id}" = {'Message' : "{message_db}"}}}
5.  route('/my_messages',methods=["POST"])                                                      - user         - {'Code':'200', 'Messages': {"{id}" = {'Message' : "{message_db}"}}}
6.  route('/Send_message',methods=["POST"])                                                     - user,msg     - {'code':'200', 'status':'ok'}
7.  route('/create_user',methods=["POST"])                                                      - user,nfthash - {'code':'200', 'status':'ok'}
8.  route('/de96871ca5ea490075a009ebd50177a6210cc91186f145db7ec20093f881bee3',methods=["POST"]) - user         - {'code':'200', 'status':'ok'}
9.  route('/5e472b3f5aa7f44438b3d83fd72ee3fbf4411e88ced3e045d748176fb3e4403f',methods=["POST"]) - user         - {'code':'200', 'status':'ok'}
10. route('/6e30d713bb138b798061ce581b23ecbc23eda84b7676820b5729cbe2035c9fdb',methods=["POST"]) - user         - {'code':'200', 'status':'ok'} 
11. route('/f25d0521e7fa4ef8cbd04ff2c6fe674c5d30c3ce194565a18002280fa51b5e67',methods=["POST"]) - user         - {'code':'200', 'status':'ok'}
12. route('/d9c9ec77c2377df2be249eabc9413905ca5960608ade94d667497102b12942ba',methods=["POST"]) - user         - {'code':'200', 'status':'ok'}
13. route('/b5f9c2da0c206aee28ab92cfc00cdb1e97d01c8987f1bb7c9f4735ddf4d13a8b',methods=["POST"]) - user         - {'code':'200', 'status':'ok'}