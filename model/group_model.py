import web,datetime
from conf.db_config import db

def get_group_posts():
    return db.select('groups')
def new_group_post(group_name):
    try:
        result=db.insert('groups',group_name=group_name)
    except:
        result=0
    return result