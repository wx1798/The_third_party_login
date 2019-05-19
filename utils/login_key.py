def weibo():
    client_weibo_id = 3214515364
    redirect_uri = "http://127.0.0.1:8000/login/weibo/"
    client_weibo_secret = "1b9b415350019674abfda80d0ef24cca"
    return client_weibo_id, redirect_uri, client_weibo_secret


def qq():
    client_qq_id = '1108968848'
    client_qq_secret = 'gp4zQO13YP3oHEae'
    redirect_uri = "http://127.0.0.1:8000/login/qq/"
    return client_qq_id, redirect_uri, client_qq_secret