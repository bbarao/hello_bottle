#!/usr/bin/env python3

from gevent import monkey; monkey.patch_all()

import bottle
from bottle import request, template
app = bottle.Bottle()

@app.get('/')
def callback():
    response = bottle.static_file("index.html", "./static")
    response.set_header("Cache-Control", "public, max-age=1")
    return response


@app.get('/<path:path>')
def callback(path):
    response = bottle.static_file(path, "./static")
    response.set_header("Cache-Control", "public, max-age=1")
    return response


@app.post('/')
def callback():
    "Displays User"

    name = request.forms.get('name', '')
    return template("./static/hello.html", name=name)


if __name__ == '__main__':
    app.run(
        host='localhost',
        port=8080,
        debug=True,
        reloader=True
    )
else:
    application = app
