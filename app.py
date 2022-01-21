from flask import json
from flask import Flask
from flask import request

import time

from QueueGitRequist import addData
import redis
from rq import Queue

r= redis.Redis()
q=Queue(connection=r)

app = Flask(__name__)

@app.route('/')
def root():
    return '<h1>Hi</h1>'

@app.route('/githubdata', methods=['POST'])
def apiMessage():
    print(request.headers['Content-Type'])
    if request.headers['Content-Type'] == 'application/json':
        job = q.enqueue(addData, json.dumps(request.json))
        
        print(f"job= {job}")

        return json.dumps(request.json)

    return "error"

if __name__=='__main__':
    app.run(debug=True)

