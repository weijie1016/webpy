import web
import json
from model import group_model
from conf.render_config import render
urls = (
    "","index",
    "/","index",
    "/view","view",
    "/view/","view",
    "/new","new",
    "/wjtest","wjtest",
    "/delete","delete",
    "/delete/","delete"
)

class index:
    def GET(self):
        return render.group()

class view:
    def __init__(self):
        self.group_post=[]
    def GET(self):
        posts=group_model.get_group_posts()
        for post in posts:
            self.group_post.append(post)
        return json.dumps(self.group_post)
class wjtest:
    def GET(self):
        dict={'success':1}
        return json.dumps(dict)
        
  
class new:
    def POST(self):
        i=web.input()
        group_name=i.group_name
        result=group_model.new_group_post(group_name)
        if result:
            d={'success':1}
        else:
            d={'msg':'Some errors occured.'}
        return json.dumps(d)
        
class delete:
    def POST(self):
        i=web.input()
        group_idstr=i.get('group_idstr')
        group_ids=group_idstr.split(",")
        result=group_model.del_group_post(group_ids)
        if result:
            d={'success':1}
        else:
            d={'msg':'Some errors occured.'}
        return json.dumps(d)
        

app_group=web.application(urls,locals())
