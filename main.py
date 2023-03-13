from flask import Flask, request, make_response
import requests


app = Flask('app')

@app.route('/')
def home():
    return 'Hi from flask'

@app.route('/cookie/<path:path>')
def home(path):
    resp = make_response(render_template('readcookie.html'))
    resp.set_cookie('userID', user)
    return 'cookie set to : ' + path


@app.route('/<path:path>',methods = ['POST', 'GET'])
def fetch(path):
    if request.method == 'GET':
        url = request.cookies.get('url')
        requests.get(url)
        data = '''<!DOCTYPE html><html><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><style>html, body {margin: 0;padding: 0;height: 100%;overflow: hidden;}iframe {display: block;width: 100%;height: 100%;border: none;}img {position: absolute;top: 0;right: 0;}</style><script src="https://unpkg.com/@ungap/custom-elements-builtin"></script><script src="https://franck403.github.io/x-frame-bypass/iframe.hitsab.js" type="module"></script></head><body><iframe is="x-frame-bypass" src="https://''' + path + '''"></iframe></body></html>'''
    else:
        data = "not supported for now"
    return data

app.run()
