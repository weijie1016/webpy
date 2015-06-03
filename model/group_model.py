import web,datetime
from conf.db_config import db

def get_group_posts():
    return db.select('groups')
def new_group_post(group_name):
    db.insert('groupss',group_name=group_name)