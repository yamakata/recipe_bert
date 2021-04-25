# -*- coding: utf-8 -*-

import json
import os

from flask import Flask
from flask_httpauth import HTTPDigestAuth
from flask import request
from mybert import sent_emb

app = Flask(__name__)
'''
app.config['SECRET_KEY'] = os.environ['SECRET_KEY']
auth = HTTPDigestAuth()

users = {
    'yamakata': 'test_yamakata',
    'guest': 'Uq8VcRS4'
}
@auth.get_password
def get_pw(username):
    if username in users:
        return users.get(username)
    return None
'''

@app.route("/sent")
#@auth.login_required
def sent():
    dic = {}
    if request.args.get("sent", "") is not None:
        print('query:', request.args.get("text", ""))
        dic['input_text'] = request.args.get("text", "")
        dic['morphemes'] = sent_emb(dic['input_text'])
    else:
        dic['input_text'] = 'No query submitted.'
        
    return json.dumps(dic, indent=2, ensure_ascii=False)

if __name__ == '__main__':
    app.run()

