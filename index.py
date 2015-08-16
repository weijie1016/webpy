import web
import sqlite3
from controller import group
from controller import user

from conf.render_config import render
urls = (
    "/", "index",
    "/group",group.app_group,
    "/user",user.app_user
)

class index:
    def GET(self):
        return render.hello()

app = web.application(urls,locals())

if __name__ == "__main__":
    app.run()