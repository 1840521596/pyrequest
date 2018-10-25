# coding=utf-8
import os
import sys
import time
import unittest
import requests
# reload(__import__('sys')).setdefaultencoding('utf-8')
# parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# sys.path.insert(0, parent_dir)


class CreditTransfer(unittest.TestCase):
    """转账"""

    def setUp(self):
        self.base_url = "http://192.168.50.166:9090/credit/transfer"

    def tearDown(self):
        pass

    def test_transfer_operator_noExist(self):
        """测试转账操作员不存在"""
        payload = {
            "operator": "org",
            "userId": "org1",
            "value": "0.00"
        }
        r = requests.post(self.base_url, data=payload)
        result = r.json()
        self.assertEqual(result['code'], "-1")
        self.assertEqual(result['message'], "用户异常")
        self.assertEqual(result['content'], "org 用户不存在")
        print(result)

    def test_transfer_success(self):
        """测试转账成功"""
        payload = {
            "operator": "org1",
            "userId": "org1",
            "value": "100"
        }
        r = requests.post(self.base_url, data=payload)
        result = r.json()
        print(result)

    def test_transfer_user_noExist(self):
        """测试收款用户不存在"""
        payload = {
            "operator": "org1",
            "userId": "org",
            "value": "0.00"
        }
        r = requests.post(self.base_url, data=payload)
        result = r.json()
        print(result)
        self.assertEqual(result['code'], "-1")
        self.assertEqual(result['message'], "用户异常")
        self.assertEqual(result['content'], "org 用户不存在")


if __name__ == '__main__':
    # test_data.init_data()  # 初始化接口测试数据
    unittest.main()
