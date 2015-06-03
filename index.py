import web
import sqlite3
from controller import group

from conf.render_config import render
urls = (
    "/", "index",
    "/group",group.app_group
)

class index:
    def GET(self):
        return render.hello()

app = web.application(urls,locals())

if __name__ == "__main__":
    app.run()