# coding=utf-8
import os
import sys
import unittest
import requests

# reload(__import__('sys')).setdefaultencoding('utf-8')
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parent_dir)


class QueryTest(unittest.TestCase):
    """查询存证"""

    def setUp(self):
        self.base_url = "http://192.168.50.166:9090/copyright/query"

    def tearDown(self):
        pass

    def test_query_success(self):
        """测试查询存证成功"""
        payload = {
            "hash": "tester1engineer"
        }
        r = requests.get(self.base_url, params=payload)
        result = r.json()
        print(result)
        self.assertEqual(result['code'], "0")
        self.assertEqual(result['message'], "查询成功")

    def test_query_fail(self):
        """测试查询存证失败"""
        payload = {
            "hash": "",
            }
        r = requests.get(self.base_url, data=payload)
        result = r.json()
        print(result)
        self.assertEqual(result['status'], 400)
        self.assertIn("Required String parameter 'hash' is not present", result['message'])
        self.assertEqual(result['error'], "Bad Request")

    def test_query_hash_noExist(self):
        """测试查询存证不存在"""
        payload = {
            "hash": "11tester1engineer111"
            }
        r = requests.get(self.base_url, params=payload)
        result = r.json()
        print(result)
        self.assertEqual(result['code'], "0")
        self.assertEqual(result['message'], "查询成功")


if __name__ == '__main__':
    # test_data.init_data()  # 初始化接口测试数据
    unittest.main()
