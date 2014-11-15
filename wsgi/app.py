# -*- coding: utf-8 -*-

"""
Flask Quick-Start for OpenShift
FYI - this probably isn't up to date with the Spring 2014 release, but it works.

2014 - Neal Shyam - @nealrs
"""

from flask import request, Flask, render_template
import requests

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run()
