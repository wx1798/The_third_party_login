from flask import Blueprint, redirect, request
from utils.login_key import weibo_key, qq_key, weixin_key
from utils.sql import insert_one, fetch_one, update_one
import uuid
from AgentLogin import AgentLogin
redirect_url = Blueprint('redirect_url', __name__,)


@redirect_url.route("/login/weibo/")
def redirect_weibo():
    code = request.args.get('code')
    client_id, redirect_uri, client_secret = weibo_key()
    user = AgentLogin.qq(client_id, client_secret, redirect_uri, code)
    # 存入数据库
    is_user = fetch_one("select * from user where username=%s", user)
    if is_user:
        token = str(uuid.uuid4())
        update_one("update user set password=%s where username=%s", (token, user))
    else:
        token = str(uuid.uuid4())
        insert_one("insert into user (username, password) values(%s, %s)", (user, token))
    redirect_url = redirect("/home")
    redirect_url.set_cookie("name", user)
    redirect_url.set_cookie("token", token)
    return redirect_url


@redirect_url.route("/login/qq")
def redirect_qq():
    code = request.args.get('code')
    print(code)
    client_id, redirect_uri, client_secret = qq_key()
    # redirect_uri = "http://127.0.0.1:8000/login/"
    user = AgentLogin.qq(client_id, client_secret, redirect_uri, code)
    # 存入数据库
    is_user = fetch_one("select * from user where username=%s", user)
    if is_user:
        token = str(uuid.uuid4())
        update_one("update user set password=%s where username=%s", (token, user))
    else:
        token = str(uuid.uuid4())
        insert_one("insert into user (username, password) values(%s, %s)", (user, token))
    redirect_url = redirect("/home")

    redirect_url.set_cookie("name", user)
    redirect_url.set_cookie("token", token)

    return redirect_url


@redirect_url.route("/login/weixin/")
def redirect_weixin():
    code = request.args.get('code')
    client_id, redirect_uri, client_secret = weixin_key()

    user = AgentLogin.weixin(client_id, client_secret, code)

    is_user = fetch_one("select * from user where username=%s", user)
    if is_user:
        token = str(uuid.uuid4())
        update_one("update user set password=%s where username=%s", (token, user))
    else:
        token = str(uuid.uuid4())
        insert_one("insert into user (username, password) values(%s, %s)", (user, token))
    redirect_url = redirect("/home")

    redirect_url.set_cookie("name", user)
    redirect_url.set_cookie("token", token)
    return redirect_url
