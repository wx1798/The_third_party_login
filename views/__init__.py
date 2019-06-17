from flask import Flask
from views.login import logins
from views.home import homes
from views.redirect_url import redirect_url


def create_app():
    app = Flask(__name__, template_folder="../templates", static_folder="../static")
    app.config.from_pyfile('../settings.py')  # 导入配置文件
    app.register_blueprint(logins)  # 注册蓝图
    app.register_blueprint(homes)
    app.register_blueprint(redirect_url)  # 第三方登录蓝图

    return app