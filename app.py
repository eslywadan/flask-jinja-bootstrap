#!/usr/bin/env python

from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route("/")
def hello():
    a = [1, 2, 3]
    return render_template('index.html', b = a)

if __name__ == '__main__':
    app.run(debug=True)