# coding=utf-8
import os
import sys
import unittest
import requests

# reload(__import__('sys')).setdefaultencoding('utf-8')
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parent_dir)


class QueryUserTest(unittest.TestCase):
    """查询用户"""

    def setUp(self):
        self.base_url = "http://192.168.50.166:9090/copyright/queryUser"

    def tearDown(self):
        pass

    def test_search_user_null(self):
        """ 查询用户为空 """
        r = requests.get(self.base_url, params={"userId": ""})
        result = r.json()
        print(result)
        self.assertEqual(result['code'], "-2")
        self.assertEqual(result['message'], "参数错误")

    def test_search_user_error(self):
        """ 查询用户错误 """
        r = requests.get(self.base_url, params={"userId": "org10"})
        result = r.json()
        print(result)
        self.assertEqual(result['code'], "53")
        self.assertEqual(result['message'], "用户尚未创建")

    def test_search_user_success(self):
        """查询用户成功"""
        r = requests.get(self.base_url, params={"userId": "org3"})
        result = r.json()
        print(result)
        self.assertEqual(result['code'], "0")
        self.assertEqual(result['message'], "查询成功")


if __name__ == '__main__':
    # test_data.init_data()  # 初始化接口测试数据
    unittest.main()
