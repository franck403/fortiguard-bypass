from flask import Flask, request, make_response
import requests
import re

app = Flask(__name__)

# Regex to detect http(s) or domain-only URLs
URL_REGEX = re.compile(
    r'\b(?:(?:https?:\/\/)?(?:www\.)?)?(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}'
    r'(?::\d+)?(?:\/[^\s]*)?\b'
)

# Base URL of your Flask app (adjust if hosted elsewhere)
FLASK_BASE_URL = 'http://localhost:5000/'

@app.route('/')
def home():
    return 'Hi from Flask'

@app.route('/cookie/<path:path>')
def set_cookie(path):
    resp = make_response(f'Cookie set to: {path}')
    resp.set_cookie('url', path)
    return resp

@app.route('/<path:path>', methods=['GET', 'POST'])
def fetch(path):
    if request.method == 'GET':
        # Get the cookie named 'url'
        url = request.cookies.get('url')
        if url:
            # Apply regex to find all matching URLs
            matches = URL_REGEX.findall(url)

            # Replace each match with Flask-proxied URL
            def replace_with_flask_proxy(match):
                return FLASK_BASE_URL + match

            rewritten = URL_REGEX.sub(lambda m: replace_with_flask_proxy(m.group(0)), url)
            return f"Original: {url}\nRewritten: {rewritten}"
        else:
            return "No URL found in cookie"
    else:
        return "POST method not supported"

if __name__ == '__main__':
    app.run(debug=True)
