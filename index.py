import web
import sqlite3
from controller import group
from controller import user
from controller import worklog
from conf.render_config import render
from controller.base import base
urls = (
    "/", "index",
    "/group", group.app_group,
    "/user", user.app_user,
    "/worklog", worklog.app_worklog
)



class index(base):
    def GET(self):
        if base.is_login(self):
            return render.hello(self.user_name,self.user_level)
        else:
            return render.login()
    
app = web.application(urls, locals())

if __name__ == "__main__":
    app.run()
