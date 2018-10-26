# coding:utf-8
import os
import sys
import unittest
from common import send_mail
from HtmlTestRunner.HTMLTestReportCN import HTMLTestRunner
import time
# sys.path.append("./testcase")
sys.path.append("./driver")
sys.path.append("./interface")


def get_log_name():
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    filename = './report/' + now + '_TestReport.html'
    return filename


def out_put_report(arg):
    # version = get_version()
    log_name = get_log_name()
    # startup()
    fp = open(log_name, 'wb')
    runner = HTMLTestRunner(
        stream=fp,
        title='DCI发送与回调测试报告',
        description='详细测试用例结果')
    runner.run(arg)
    fp.close()


if __name__ == '__main__':
    # 指定测试用例为当前文件夹下的testcase目录
    # os.startfile("startup.bat")
    time.sleep(2)
    # os.system("ntsd -c q -pn cmd.exe")
    test_dir = './interface'
    discover = unittest.defaultTestLoader.discover(test_dir, pattern='*_test.py')
    time.sleep(2)
    # 输出报告
    out_put_report(discover)
    time.sleep(2)
    # send_mail.send_report()
    # os.system("taskkill /f /t /im cmd.exe")