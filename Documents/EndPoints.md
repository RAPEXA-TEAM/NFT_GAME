## only user - Called once - order is important

1.   create_user(user,TokenID) # create user
2.   de96871ca5ea490075a009ebd50177a6210cc91186f145db7ec20093f881bee3(user,TokenID) # pass_level1
3.   5e472b3f5aa7f44438b3d83fd72ee3fbf4411e88ced3e045d748176fb3e4403f(user,TokenID) # pass_level2
4.   6e30d713bb138b798061ce581b23ecbc23eda84b7676820b5729cbe2035c9fdb(user,TokenID) # pass_level3
5.   f25d0521e7fa4ef8cbd04ff2c6fe674c5d30c3ce194565a18002280fa51b5e67(user,TokenID) # pass_level4
6.   b5f9c2da0c206aee28ab92cfc00cdb1e97d01c8987f1bb7c9f4735ddf4d13a8b(user,TokenID) # pass_level5

## only user - called every time refreshing app

-   my_messages(TokenID)
- 	book(TokenID)

## only admin

-   ok(password)                                #first call
-   Send_message(TokenID)
-   all_messages()
-   users()
-   winners()

```
-	book: {
		Method: POST
		Parameters: {
			TokenID,
			Device,
		}
        Outputs: {
			{'status':'failed','error':'requests not valid'},
			{'status':'failed','error':'connect to database failed'},
			{'Code':"200" , 'level1': "[LEVEL1_LINK]"},
			{'Code':"200" , 'level1': "[LEVEL1_LINK]" , 'level2': "[LEVEL2_LINK]"},
			{'Code':"200" , 'level1': "[LEVEL1_LINK]" , 'level2': "[LEVEL2_LINK]" , 'level3': "[LEVEL3_LINK]"},
			{'Code':"200" , 'level1': "[LEVEL1_LINK]" , 'level2': "[LEVEL2_LINK]" , 'level3': "[LEVEL3_LINK]" , 'level4': "[LEVEL4_LINK]"},
			{'Code':"200" , 'level1': "[LEVEL1_LINK]" , 'level2': "[LEVEL2_LINK]" , 'level3': "[LEVEL3_LINK]" , 'level4': "[LEVEL4_LINK]" , 'level5': "[LEVEL5_LINK]"},
        }
		Description: {
            This EndPoint send each user book according to their level in game.
		}
	}
}

-	ok: {
		Method: POST
		Parameters:{
			pass,
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
            {'Code':'200', 'users': { [id] : {'user' : [user] , 'TokenID' : [TokenID] , 'percentage' : [percentage] }}},
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
            {'Code':'200', 'users': { [id] = {'TokenID' : [TokenID] , 'user' : [user] }}},
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
            {'Code':"200" , 'Messages': { [id] = {'TokenID' : [TokenID] , 'Message' : [message]}}},
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
			TokenID,
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
			TokenID,
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
			user,
            TokenID,
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
			user,
			TokenID,
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
			user,
			TokenID,
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
			user,
			TokenID,
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
			user,
			TokenID,
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
			user,
			TokenID,
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
			user,
			TokenID,
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