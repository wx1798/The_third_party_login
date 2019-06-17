def weibo_key():
    client_weibo_id = 3214515364
    redirect_uri = "http://127.0.0.1:8000/login/weibo/"
    client_weibo_secret = "1b9b415350019674abfda80d0ef24cca"
    return client_weibo_id, redirect_uri, client_weibo_secret


def qq_key():
    client_qq_id = 101576925
    client_qq_secret = '95bfd07354fcd7188507b8bea4ff679a'
    redirect_uri = "http://127.0.0.1:8000/login/qq"
    return client_qq_id, redirect_uri, client_qq_secret


def weixin_key():
    pass