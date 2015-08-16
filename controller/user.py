import web
import json
import hashlib
from model import user_model
from conf.render_config import render
urls = (
    "","index",
    "/","index",
    "/view","view",
    "/view/","view",
    "/new","new",
    "/wjtest","wjtest",
    "/delete","delete",
    "/delete/","delete",
    "/edit/(\d+)","edit",
    "/login","login",
    "/login/","login",
    
)

class index:
    def GET(self):
        return render.user()

class view:
    def __init__(self):
        self.user_post=[]
    def GET(self):
        posts=user_model.get_user_posts()
        for post in posts:
            self.user_post.append(post)
        return json.dumps(self.user_post)
class wjtest:
    def GET(self):
        dict={'success':1}
        return json.dumps(dict)
        
  
class new:
    def POST(self):
        i=web.input()
        user_name=i.user_name
        user_pwd=i.user_pwd
        user_level=i.user_level
        user_group_id=i.user_group_id
        m=hashlib.md5()
        m.update(user_pwd)
        user_pwd=m.hexdigest()
        result=user_model.new_user_post(user_name,user_pwd,user_level,user_group_id)
        if result:
            d={'success':1}
        else:
            d={'msg':'Some errors occured.'}
        return json.dumps(d)
class edit:
    def POST(self,user_id):
        i=web.input()
        user_name=i.user_name
        result=user_model.edit_user_post(user_id,user_name)
        if result:
            d={'success':1}
        else:
            d={'msg':'Some errors occured.'}
        return json.dumps(d)
class delete:
    def POST(self):
        i=web.input()
        user_idstr=i.get('user_idstr')
        user_ids=user_idstr.split(",")
        result=user_model.del_user_post(user_ids)
        if result:
            d={'success':1}
        else:
            d={'msg':'Some errors occured.'}
        return json.dumps(d)
class login:
    def GET(self):
        return "login"
    def POST(self):
        pass
        
        

app_user=web.application(urls,locals())
