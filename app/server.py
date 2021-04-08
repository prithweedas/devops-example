from flask import Flask
import os

from functions import add

app = Flask(__name__)

@app.route("/")
def add_two_numbers():
    page = '<html><body><h1>'
    page += 'Hey!'
    page += f' {add(1,2)}'
    page += '</h1></body></html>'
    return page

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.getenv('PORT', 5000)))