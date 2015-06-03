import web
import sqlite3
import user_model

urls = (
    '/', 'index',
    '/group','group',
    '/user','user',
    '/worklog','worklog',
    '/user','user',
    '/blog/(.*)','blog'
)

render = web.template.render('templates')

class index:
    def GET(self):
        names=model.get_logins()

        return render.hello(names)

class new:
    form=web.form.Form(
        web.form.Textbox('username', web.form.notnull, 
            size=30,
            description="Post username:"),
        web.form.Password('password', web.form.notnull, 
            size=30,
            description="Post password:"),
        web.form.Button('Post entry'),
    )
    def GET(self):
        form = self.form()
        return render.new(form)

    def POST(self):
        form = self.form()
        if not form.validates():
            return render.new(form)
        model.new_post(form.d.username,form.d.password)
        raise web.seeother('/')

class blog:
    def GET(self,name):
        return render.hello(name)

if __name__ == "__main__":
    app = web.application(urls, locals())
    app.run()