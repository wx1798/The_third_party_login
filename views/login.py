from flask import Blueprint, render_template, request, session, redirect
from utils.login_key import weibo

logins = Blueprint('logins', __name__,)  #  static_folder='', static_url_path=''


@logins.route('/', methods=['GET', 'POST'])
def login():
    if request.method == "GET":
        client_id, redirect_weibo_url, client_secret = weibo()
        weibo_url = "https://api.weibo.com/oauth2/authorize?client_id={client_id}&redirect_uri={redirect_uri}".format(
            client_id=client_id, redirect_uri=redirect_weibo_url)
        return render_template("login.html", weibo_url=weibo_url)
    username = request.form.get("username")
    password = request.form.get('password')
    print(username, password)
    return redirect("/home")