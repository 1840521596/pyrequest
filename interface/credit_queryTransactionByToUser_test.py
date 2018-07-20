# coding=utf-8
import os
import sys
import unittest
import requests
# reload(__import__('sys')).setdefaultencoding('utf-8')
# parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# sys.path.insert(0, parent_dir)


class QueryTransactionByToUser(unittest.TestCase):
    """查询作为接受者的交易记录"""

    def setUp(self):
        self.base_url = "http://192.168.50.166:9090/credit/queryTransactionByToUser"

    def tearDown(self):
        pass

    def test_queryTransactionByToUser_success(self):
        """测试查询接受者交易记录成功"""
        payload = {
            "userId": "org2"
        }
        r = requests.get(self.base_url, params=payload)
        result = r.json()
        print(result)
        self.assertEqual(result['code'], "0")
        self.assertEqual(result['message'], "查询成功")

    def test_queryTransactionByToUser_noExist(self):
        """测试查询接受者不存在"""
        payload = {
            "userId": "org10"
        }
        r = requests.get(self.base_url, params=payload)
        result = r.json()
        print(result)
        self.assertEqual(result['code'], "53")
        self.assertEqual(result['message'], "用户尚未创建")

    def test_queryTransactionByToUser_null(self):
        """测试查询接受者为空"""
        payload = {
            "userId": ""
        }
        r = requests.get(self.base_url, params=payload)
        result = r.json()
        print(result)
        self.assertEqual(result['code'], "-2")
        self.assertEqual(result['message'], "参数错误")


if __name__ == '__main__':
    # test_data.init_data()  # 初始化接口测试数据
    unittest.main()
