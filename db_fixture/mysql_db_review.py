# coding=utf-8
import os
import configparser as config
from pymysql import cursors, connect
from pymysql import OperationalError

# =========获取文件的路径，读取db_config.ini配置文件============
base_dir = os.path.dirname(os.path.dirname(__file__))
base_dir = base_dir.replace('\\', '/')
sql_conf = base_dir + "/db_congig.ini"
cf = config.ConfigParser()
cf.read(sql_conf)
host = cf.get('mysqlconf', 'host')
port = cf.get('mysqlconf', 'port')
user = cf.get('mysqlconf', 'user')
password = cf.get('mysqlconf', 'password')
db = cf.get('mysqlconf', 'db_name')


# ==========封装MySql数据库============
class DB(object):
    def __init__(self):
        # =====链接数据库=====
        try:
            self.conn = connect(host=host,
                                user=user,
                                password=password,
                                db=db,
                                charset='utf8mb4',
                                cursorclass=cursors.DictCursor
                                )
        except OperationalError as e:
            print("MySql Error is %d:%s" % (e.args[1], e.args[2]))

    def clear(self, tablename):
        sql_command = 'delete from ' + tablename + ';'
        with self.conn.cursor() as cursor:
            cursor.execute("SET FOREIGN_KEY_CHECKS=0;")
            cursor.execute(sql_command)
        self.conn.commit()

    def insert(self, tablename, tabledata):
        for key in tabledata:
            tabledata[key] = "'" + str(tabledata[key]) + "'"
        key = "'".join(tabledata.keys())
        value = "'".join(tabledata.values())
        sql_command = 'insert into ' + tablename + "(" + key + ")" \
                      + "values" + "(" + value + ")"
        with self.conn.cursor()as cursor:
            cursor.execute(sql_command)
        self.conn.commit()

    def close(self):
        self.conn.close()


if __name__ == '__main__':
    db = DB()
    tablename = 'sign_event'
    data = {}
    db.clear(tablename)
    db.insert(tablename, data)
    db.close()
