# encoding=utf-8
import sys
import time
import unittest
from HTMLTestRunner import HTMLTestRunner
# from db_fixture import test_data


# reload(__import__('sys')).setdefaultencoding('utf-8')
from common import send_mail

sys.path.append('./interface')
sys.path.append('./db_fixture')


# 指定测试用例为当前文件夹下的interface 目录
test_dir = './interface'
discover = unittest.defaultTestLoader.discover(test_dir, pattern='*_test.py')

if __name__ == '__main__':
    # test_data.init_data()  # 初始化接口测试数据
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    file_name = './report/' + now + '_result.html'
    fp = open(file_name, 'wb')
    runner = HTMLTestRunner(stream=fp,
                            title='积分存证接口测试报告',
                            description='实施结果如下：')
    runner.run(discover)
    fp.close()
    time.sleep(3)
    send_mail.send_report()
