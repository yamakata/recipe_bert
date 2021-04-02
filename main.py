import json
import os

from flask import Flask
from flask_httpauth import HTTPDigestAuth
from flask import request
from mybert import sent_emb

app = Flask(__name__)

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

@app.route("/sent")
@auth.login_required
def sent():
    dic = {}
    if request.args.get("sent", "") is not None:
        print('query:', request.args.get("text", ""))
        dic['text'] = request.args.get("text", "")
        dic['vec'] = sent_emb(dic['text'])
    else:
        dic['text'] = 'No query submitted.'
        
    return json.dumps(dic, indent=2, ensure_ascii=False)

if __name__ == '__main__':
    app.run()

