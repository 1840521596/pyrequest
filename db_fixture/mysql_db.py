# coding=utf8
import time
import os
from pymysql import connect, cursors
from pymysql import OperationalError
import configparser as cpaser


# ============读取 db_config.ini文件设置===============
base_dir = str(os.path.dirname(os.path.dirname(__file__)))
base_dir = base_dir.replace('\\', '/')
file_path = base_dir + "/db_config.ini"
cf = cpaser.ConfigParser()
cf.read(file_path)
host = cf.get('mysqlconf', 'host')
port = cf.get('mysqlconf', 'port')
db = cf.get('mysqlconf', 'db_name')
user = cf.get('mysqlconf', 'user')
password = cf.get('mysqlconf', 'password')


# ============封装MySQL基本操作===============
class DB:
    def __init__(self):
        try:
            # 连接数据库
            self.conn = connect(host=host,
                                user=user,
                                password=password,
                                db=db,
                                charset='utf8mb4',
                                cursorclass=cursors.DictCursor
                                )
        except OperationalError as e:
            print("Mysql Error %d:%s" % (e.args[0], e.args[1]))

    # 清除表数据
    def clear(self, tablename):
        real_sql = "delete from " + tablename + ";"
        with self.conn.cursor() as cursor:
            cursor.execute("SET FOREIGN_KEY_CHECKS=0;")
            cursor.execute(real_sql)
        self.conn.commit()

    # 插入表数据
    def insert(self, tablename, tabledata):
        for key in tabledata:
            tabledata[key] = "'" + str(tabledata[key]) + "'"
        key = ",".join(tabledata.keys())
        value = ",".join(tabledata.values())
        real_sql = "INSERT INTO " + tablename + " (" + key + ") VALUES(" + value + ");"
        print(real_sql)

        with self.conn.cursor() as cursor:
            cursor.execute(real_sql)
        self.conn.commit()

    # 关闭数据库连接
    def close(self):
        self.conn.close()


if __name__ == '__main__':
    db = DB()
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    tablename = "test_data"
    data = {'id': 12, 'name': '红米', '`limit`': 2000, 'status': 1, 'address':
            '清大世纪教育集团', 'start_time': '2016-08-20 00:25:42', 'create_time': now}
    db.clear(tablename)
    db.insert(tablename, data)
    db.close()
