import web
import json
from model import group_model
from conf.render_config import render
urls = (
    "","index",
    "/","index",
    "/view","view",
    "/new","new"
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

# class new:
    # def __init__(self):
        # pass
    # def POST(self):
        

app_group=web.application(urls,locals())