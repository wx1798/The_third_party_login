import pymysql
from settings import Config


def connect():
    conn = Config.POOL.connection()
    cursor = conn.curser(pymysql.cursors.DictCursor)
    return conn, cursor


def close(conn, cursor):
    cursor.close()
    conn.close()


def fetch_one(sql, args):
    conn, cursor = connect()
    cursor.execute(sql, args)
    sql_message = cursor.fetchone()
    close(conn, cursor)
    return sql_message


def insert_one(sql, args):
    conn, cursor = connect()
    cursor.execute(sql, args)
    conn.commit()
    close(conn, cursor)


def update_one(sql, args):
    conn, cursor = connect()
    cursor.execute(sql, args)
    conn.commit()
    close(conn, cursor)


