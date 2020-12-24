
from typing import Dict
from pydantic import BaseModel

class UserInDB(BaseModel):
    username: str
    password: str
    balance: int

database_users = Dict[str, UserInDB]

database_users = {
"camilo24": UserInDB(**{"username":"camilo24",
                        "password":"root",
                        "balance":12000}),
"carlos24": UserInDB(**{"username":"carlos24",
                        "password":"root",
                        "balance":13000}),
"andres24": UserInDB(**{"username":"andres24",
                        "password":"root",
                        "balance":14000}),
}

def get_user(username: str):
    if username in database_users.keys():
        return database_users[username]
    else:
        return None

def update_user(user_in_db: UserInDB):
    database_users[user_in_db.username] = user_in_db
    return user_in_db