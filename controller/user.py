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
    "/delete","delete",
    "/delete/","delete",
    "/edit/(\d+)","edit",
    "/login","login",
    "/login/","login",
    "/logout","logout",
    "/logout/","logout"
)

class index:
    def GET(self):
        try:
            user_name=web.cookies().user_name
            return render.user()
        except:    
            return render.login()

class view:
    def __init__(self):
        self.user_post=[]
    def GET(self):
        posts=user_model.get_user_posts()
        for post in posts:
            self.user_post.append(post)
        return json.dumps(self.user_post)

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
        return render.login()
    def POST(self):
        i=web.input()
        user_name=i.get('user_name')
        user_pwd=i.get('user_pwd')
        m=hashlib.md5()
        m.update(user_pwd)
        user_pwd=m.hexdigest()
        result=user_model.is_login(user_name,user_pwd)
        if result:
            for r in result:
                user_level=r.user_level
            web.setcookie('user_name', user_name,expires='',domain=None,secure=False,httponly=False,path='/')
            web.setcookie('user_level', user_level,expires='',domain=None,secure=False,httponly=False,path='/')
            d={'success':1}
        else:
            d={'msg':'Some errors occured.'}
        return json.dumps(d)
        
class logout:
    def GET(self):
        web.setcookie('user_name','',expires=-1,domain=None,secure=False,httponly=False,path='/')
        web.setcookie('user_level','',expires=-1,domain=None,secure=False,httponly=False,path='/')
        raise web.SeeOther('/')

app_user=web.application(urls,locals())
