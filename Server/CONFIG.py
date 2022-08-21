#!/usr/bin/env

# Flask

SECRET_KEY = "secret!"
SOURCE = '0x0000000000000000000000000000000000000000'

# MySQL config

MYSQL_HOST = "127.0.0.1"
MYSQL_USER = "NFTUSER"
MYSQL_PASS = "NFTPASS"
MYSQL_DATABAS = "NFT_GAME"

# Game levels

LEVEL1 = 15
LEVEL2 = 30
LEVEL3 = 45
LEVEL4 = 60
LEVEL5 = 80
LEVEL6 = 100
LEVEL1_CODE = "de96871ca5ea490075a009ebd50177a6210cc91186f145db7ec20093f881bee3"
LEVEL2_CODE = "5e472b3f5aa7f44438b3d83fd72ee3fbf4411e88ced3e045d748176fb3e4403f"
LEVEL3_CODE = "6e30d713bb138b798061ce581b23ecbc23eda84b7676820b5729cbe2035c9fdb"
LEVEL4_CODE = "f25d0521e7fa4ef8cbd04ff2c6fe674c5d30c3ce194565a18002280fa51b5e67"
LEVEL5_CODE = "d9c9ec77c2377df2be249eabc9413905ca5960608ade94d667497102b12942ba"
LEVEL6_CODE = "b5f9c2da0c206aee28ab92cfc00cdb1e97d01c8987f1bb7c9f4735ddf4d13a8b"

# Web3

W3_PROVIDER = ""
CONTRACT_ADDRESS = ""
CONTRACT_ABI = """[
    {
        constant: true,
        inputs: [{name: "_owner", type: "address"}],
        name: "balanceOf",
        outputs: [{name: "balance", type: "uint256"}],
        type: "function",
    },
]"""