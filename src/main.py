# API
# A api for my projects and other things
# Github: https://www.github.com/lewisevans2007/api
# Licence: GNU General Public License v3.0
# By: Lewis Evans

from flask import Flask, request, jsonify
from flask_cors import CORS

import json
import datetime
import random
import os
import subprocess
import datetime

VERSION = "1.1.0"
START_TIME = datetime.datetime.now()

app = Flask(__name__)
CORS(app)

homepage = (
    """
<style>
    body {
        font-family: sans-serif;
    }

    .content {
        margin: 0 auto;
        width: 80%;
        box-shadow: 0px 0px 10px 0px rgba(0,0,0,0.10);
        padding: 20px;
        border-radius: 10px;
        background-color: #fff;
    }
</style>
<br>
<div class="content">
    <h1>lewisevans2007 API v"""
    + VERSION
    + """</h1>
    <hr>
    <p>An API for my projects and other things</p>
    <p>Github: <a href="https://www.github.com/lewisevans2007/api">https://www.github.com/lewisevans2007/api</a></p>
    <p>For usage please go to <a href="/api/help">/api/help</a></p>
</div>
"""
)


@app.route("/")
def index():
    return homepage


@app.route("/api/version")
def version():
    ver = {"version": VERSION}
    return json.dumps(ver, indent=4)


@app.route("/api/help")
def help():
    f = open("src/help.json", "r")
    return f.read()


@app.route("/api/time/date")
def api_time_date():
    date = {"date": datetime.datetime.now().strftime("%d/%m/%Y")}
    return json.dumps(date, indent=4)


@app.route("/api/time/time")
def api_time_time():
    time = {"time": datetime.datetime.now().strftime("%H:%M:%S")}
    return json.dumps(time, indent=4)


@app.route("/api/random")
def api_random():
    num = {"random": random.random()}
    return json.dumps(num, indent=4)


@app.route("/api/ip")
def api_ip():
    ip = {"ip": request.remote_addr}
    return json.dumps(ip, indent=4)


@app.route("/api/useragent")
def api_useragent():
    useragent = {"useragent": request.headers.get("User-Agent")}
    return json.dumps(useragent, indent=4)


@app.route("/api/headers")
def api_headers():
    headers = {"headers": request.headers}
    return json.dumps(headers, indent=4)


@app.route("/api/nodejs/version")
def api_nodejs_version():
    nodejs = {
        "nodejs": subprocess.check_output(["node", "--version"])
        .decode("utf-8")
        .replace("\n", "")
    }
    return json.dumps(nodejs, indent=4)


@app.route("/api/repos")
def api_repos():
    result = subprocess.check_output(["node", "src/modules/get_repos.js"]).decode(
        "utf-8"
    )
    return result


@app.route("/api/uptime")
def api_uptime():
    uptime = {"uptime": str(datetime.datetime.now() - START_TIME)}
    return json.dumps(uptime, indent=4)


if __name__ == "__main__":
    app.run(debug=False, port=80)
