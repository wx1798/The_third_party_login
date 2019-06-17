from flask import Blueprint, render_template, request, session, redirect
from utils.login_key import weibo_key, qq_key, weixin_key
from AgentLogin import AgentLogin

logins = Blueprint('logins', __name__,)  #  static_folder='', static_url_path=''


@logins.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "GET":
        weibo_client_id, weibo_redirect_url, weibo_client_secret = weibo_key()
        qq_client_id, qq_redirect_url, qq_client_secret = qq_key()
        weibo_url = AgentLogin.weibo_url(weibo_client_id, weibo_redirect_url)
        qq_url = AgentLogin.qq_url(qq_client_id, qq_redirect_url)
        return render_template("login.html", weibo_url=weibo_url, qq_url=qq_url)
    username = request.form.get("username")
    password = request.form.get('password')
    print(username, password)
    return redirect("/home")