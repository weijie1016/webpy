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

def edit_group_post(group_id,group_name):
    try:
        result=db.update('groups',where='group_id=$group_id',vars=locals(),group_name=group_name)
    except:
        result=0
    return result

def del_group_post(group_ids):
    try:
        for group_id in group_ids:
            db.delete('groups',where='group_id=$group_id',vars=locals())
        result=1
    except:
        result=0
    return result