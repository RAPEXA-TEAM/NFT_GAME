## only user - Called once - order is important

1.   create_user(UserWalletAddress,nft_hash)
2.   pass_level1(UserWalletAddress)
3.   pass_level2(UserWalletAddress)
4.   pass_level3(UserWalletAddress)
5.   pass_level4(UserWalletAddress)
6.   pass_level5(UserWalletAddress)
7.   pass_level6(UserWalletAddress)

## only user - called every time refreshing app

-   read_user_messages(UserWalletAddress)

## only admin

-   ok()                                #first call
-   Send_message(UserWalletAddress)
-   read_all_messages()
-   read_users()
-   read_winners()

######

```

-	ok: {
		Method: POST
		Parameters:{
			password,
		}
        Outputs: {
            {'code':'200', 'status':'ok'},
			{'status':'failed','error':'password incorrect!'},
			{'status':'failed','error':'requests not valid'},
            }
		Description: {
            This EndPoint check password for login admin.
         }
	}

-	users: {
		Method: GET
		Parameters:{}
        Outputs: {
            {'Code':'200', 'users': { [id] : {'user' : [user] , 'nft' : [nft hash] , 'percentage' : [percentage] }}},
            {'status':'failed','error':'connect to database failed'},
            }
		Description: {
            This EndPoint return all users.
		}
	}


-	winners: {
		Method: GET
		Parameters: {}
        Outputs: {
            {'Code':'200', 'users': { [id] = {'winner' : [winner_wallet] }}},
            {'status':'failed','error':'connect to database failed'},
        }
		Description: {
            This EndPoint return all winners.
		}
	}
}

-	all_messages: {
		Method: GET
		Parameters: {}
        Outputs: {
            {'Code':'200', 'Messages': { [id] = {'Message' : [message] }}},
            {'status':'failed','error':'connect to database failed'},
        }
		Description: {
            This EndPoint return all messages.
		}
	}
}

-	my_messages: {
		Method: POST
		Parameters: {
			UserWalletAddress,
		}
        Outputs: {
            {'Code':'200', 'Messages': { [id] = {'Message' : [message_db] }}},
            {'status':'failed','error':'requests not valid'},
        }
		Description: {
            This EndPoint return one user messages.
		}
	}
}

-	Send_message: {
		Method: POST
		Parameters: {
			UserWalletAddress,
            Message,
		}
        Outputs: {
            {'code':'200', 'status':'ok'},
            {'status':'failed','error':'requests not valid'},
        }
		Description: {
            This EndPoint send message to one user.
		}
	}
}

-	create_user: {
		Method: POST
		Parameters: {
			UserWalletAddress,
            NFTHash,
		}
        Outputs: {
            {'status':'ok','code':'200'},
            {'status':'failed','error':'writing user to database'},
            {'status':'failed','error':'user not valid'},
            {'status':'failed','error':'requests not valid'},
        }
		Description: {
            This EndPoint check and vaidate payment and then create one user.
		}
	}
}

-	de96871ca5ea490075a009ebd50177a6210cc91186f145db7ec20093f881bee3: {
		Method: POST
		Parameters: {
			UserWalletAddress,
		}
        Outputs: {
            {'code':'200', 'status':'ok'},
            {'status':'failed','error':'user not valid'},
            {'status':'failed','error':'requests not valid'},
        }
		Description: {
            This EndPoint pass one User Level 1.
		}
	}
}

-	5e472b3f5aa7f44438b3d83fd72ee3fbf4411e88ced3e045d748176fb3e4403f: {
		Method: POST
		Parameters: {
			UserWalletAddress,
		}
        Outputs: {
            {'code':'200', 'status':'ok'},
            {'status':'failed','error':'user not valid'},
            {'status':'failed','error':'requests not valid'},
        }
		Description: {
            This EndPoint pass one User Level 2.
		}
	}
}

-	6e30d713bb138b798061ce581b23ecbc23eda84b7676820b5729cbe2035c9fdb: {
		Method: POST
		Parameters: {
			UserWalletAddress,
		}
        Outputs: {
            {'code':'200', 'status':'ok'},
            {'status':'failed','error':'user not valid'},
            {'status':'failed','error':'requests not valid'},
        }
		Description: {
            This EndPoint pass one User Level 3.
		}
	}
}

-	f25d0521e7fa4ef8cbd04ff2c6fe674c5d30c3ce194565a18002280fa51b5e67: {
		Method: POST
		Parameters: {
			UserWalletAddress,
		}
        Outputs: {
            {'code':'200', 'status':'ok'},
            {'status':'failed','error':'user not valid'},
            {'status':'failed','error':'requests not valid'},
        }
		Description: {
            This EndPoint pass one User Level 4.
		}
	}
}

-	d9c9ec77c2377df2be249eabc9413905ca5960608ade94d667497102b12942ba: {
		Method: POST
		Parameters: {
			UserWalletAddress,
		}
        Outputs: {
            {'code':'200', 'status':'ok'},
            {'status':'failed','error':'user not valid'},
            {'status':'failed','error':'requests not valid'},
        }
		Description: {
            This EndPoint pass one User Level 5.
		}
	}
}

-	b5f9c2da0c206aee28ab92cfc00cdb1e97d01c8987f1bb7c9f4735ddf4d13a8b: {
		Method: POST
		Parameters: {
			UserWalletAddress,
		}
        Outputs: {
            {'code':'200', 'status':'ok'},
            {'status':'failed','error':'user not valid'},
            {'status':'failed','error':'connect to database failed'},
            {'status':'failed','error':'user didnt pass level 5'},
            {'status':'failed','error':'requests not valid'},
        }
		Description: {
            This EndPoint pass one User Level 6.
		}
	}
}

```