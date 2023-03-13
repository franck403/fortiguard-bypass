from flask import Flask, request
import requests


app = Flask('app')

@app.route('/')
def home():
    return 'Hi from flask'

@app.route('/<path:path>')
def fetch(path):
    request.cookies.get('url')
    data = '''<!DOCTYPE html><html><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><style>html, body {margin: 0;padding: 0;height: 100%;overflow: hidden;}iframe {display: block;width: 100%;height: 100%;border: none;}img {position: absolute;top: 0;right: 0;}</style><script src="https://unpkg.com/@ungap/custom-elements-builtin"></script><script src="https://franck403.github.io/x-frame-bypass/iframe.hitsab.js" type="module"></script></head><body><iframe is="x-frame-bypass" src="https://''' + path + '''"></iframe></body></html>'''
    return data

app.run(host='0.0.0.0', port=8080)
