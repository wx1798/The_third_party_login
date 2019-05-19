from flask import Blueprint, redirect, request
from utils.login_key import weibo
from utils.sql import insert_one, fetch_one, update_one
import requests
import json
import uuid


redirects = Blueprint('redirects', __name__,)


@redirects.route("/login/")
def redirect_url():
    code = request.args.get('code')
    print(code)
    client_id, redirect_uri, client_secret = weibo()
    # 请求得到access_token
    # redirect_uri = "http://127.0.0.1:8000/login/"
    get_Access_token_url = "https://api.weibo.com/oauth2/access_token?client_id={}&client_secret={}&redirect_uri={}&code={}".format(
        client_id, client_secret, redirect_uri, code)
    response = requests.post(url=get_Access_token_url).text
    response_loads = json.loads(response)
    print(response_loads)
    access_token = response_loads['access_token']
    print(access_token)
    uid = response_loads['uid']
    # 请求得到用户信息
    get_message_url = "https://api.weibo.com/2/users/show.json?access_token={}&uid={}&redirect_uri={}".format(
        access_token, uid, redirect_uri)
    info_message = requests.get(url=get_message_url).text
    info_message_loads = json.loads(info_message)
    # 存入数据库
    is_user = fetch_one("select * from user where username=%s", info_message_loads['id'])
    if is_user:
        token = str(uuid.uuid4())
        update_one("update user set password=%s where username=%s", (token, is_user))
    else:
        token = str(uuid.uuid4())
        insert_one("insert into user (username, password) values(%s, %s)", (info_message_loads['id'], token))
    # 拿到请求路径
    # path = request.get_host()
    # print(is_safe_url("http://127.0.0.1:8080/home", allowed_hosts={"127.0.0.1:8080"}))
    redirect_url = redirect("http://127.0.0.1:8000/home/")

    redirect_url.set_cookie("name", info_message_loads['id'])
    redirect_url.set_cookie("token", token)
    return redirect_url