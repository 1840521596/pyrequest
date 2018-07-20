# coding=utf-8
import sys
import time
from db_fixture.mysql_db import DB
sys.path.append("../db_fixture")


# 创建测试数据
now = time.strftime("%Y-%m-%d %H_%M_%S")
datas = {
    # 发布会表数据
    'sign_event': [
        {'id': 1, 'name': '红米Pro发布会', '`limit`': 2000, 'status': 1, 'address':
            '北京会展中心', 'start_time': '2017-09-10 00:25:42', 'create_time': now},
        {'id': 2, 'name': '可参加人数为0', '`limit`': 0, 'status': 1, 'address':
            '北京会展中心', 'start_time': '2017-09-10 00:25:42', 'create_time': now},
        {'id': 3, 'name': '当前状态为0关闭', '`limit`': 2000, 'status': 0, 'address':
            '北京会展中心', 'start_time': '2016-08-20 00:25:42', 'create_time': now},
        {'id': 4, 'name': '发布会已经结束', '`limit`': 2000, 'status': 1, 'address':
            '北京会展中心', 'start_time': '2016-08-20 00:25:42', 'create_time': now},
        {'id': 5, 'name': '小米5发布会', '`limit`': 2000, 'status': 1, 'address':
            '北京会展中心', 'start_time': '2016-08-20 00:25:42', 'create_time': now},
        {'id': 6, 'name': '小米6发布会', '`limit`': 2000, 'status': 1, 'address':
            '北京会展中心', 'start_time': '2016-08-20 00:25:42', 'create_time': now},
        {'id': 7, 'name': '小米7发布会', '`limit`': 2000, 'status': 1, 'address':
            '北京会展中心', 'start_time': '2016-08-20 00:25:42', 'create_time': now},
        {'id': 8, 'name': '小米8发布会', '`limit`': 2000, 'status': 1, 'address':
            '北京会展中心', 'start_time': '2016-08-20 00:25:42', 'create_time': now},
        {'id': 9, 'name': '小米9发布会', '`limit`': 2000, 'status': 1, 'address':
            '北京会展中心', 'start_time': '2016-08-20 00:25:42', 'create_time': now},
        {'id': 10, 'name': '小米10发布会', '`limit`': 2000, 'status': 1, 'address':
            '北京会展中心', 'start_time': '2016-08-20 00:25:42', 'create_time': now}
    ],
    # 发布会表数据
    'sign_guest': [
        {'id': 1, 'realname': 'alen', 'phone': 13511001100, 'email': 'alen@mail.com',
         'sign': 0, 'event_id': 1, 'create_time': now},
        {'id': 2, 'realname': 'has sign', 'phone': 13511001101, 'email': 'sign@mail.com',
         'sign': 1, 'event_id': 1, 'create_time': now},
        {'id': 3, 'realname': 'tom', 'phone': 13511001102, 'email': 'tom@mail.com',
         'sign': 0, 'event_id': 5, 'create_time': now},
    ]
}


# 将测试数据插入表
def init_data():
    db = DB()
    for table, data in datas.items():
        db.clear(table)
        for d in data:
            db.insert(table, d)
    db.close()


if __name__ == '__main__':
    init_data()