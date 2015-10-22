import web,datetime
from conf.db_config import db

def get_user_posts():
    return db.select('user_group_view')

def is_login(user_name,user_pwd):
    return db.where('users',user_name=user_name,user_pwd=user_pwd)

def new_user_post(user_name,user_pwd,user_level,user_group_id):
    try:
        result=db.insert('users',user_name=user_name,user_pwd=user_pwd,user_level=user_level,user_group_id=user_group_id)
    except:
        result=0
    return result

def edit_user_post(user_id,user_name):
    try:
        result=db.update('users',where='user_id=$user_id',vars=locals(),user_name=user_name)
    except:
        result=0
    return result

def del_user_post(user_ids):
    try:
        for user_id in user_ids:
            db.delete('users',where='user_id=$user_id',vars=locals())
        result=1
    except:
        result=0
    return result