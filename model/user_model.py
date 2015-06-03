import web,datetime
from conf.db_config import db
#db = web.database(dbn='sqlite', db='../sqlite/demo.db')

def get_user():
    return db.select('users')

def new_user(user_name,user_pwd):
    db.insert('users',user_name=user_name,user_pwd=user_pwd)
