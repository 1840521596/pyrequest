# coding=utf-8
import os
import sys
import unittest
import requests
# reload(__import__('sys')).setdefaultencoding('utf-8')
# parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# sys.path.insert(0, parent_dir)


class BalanceOf(unittest.TestCase):
    """查询账户余额"""

    def setUp(self):
        self.base_url = "http://192.168.50.166:9090/credit/balanceOf"

    def tearDown(self):
        pass

    def test_balanceOf_success(self):
        """测试查询账户余额成功"""
        payload = {
            "userId": "org1"
        }
        r = requests.get(self.base_url, params=payload)
        result = r.json()
        print(result)
        self.assertEqual(result['code'], "0")
        self.assertEqual(result['message'], "查询成功")

    def test_balanceOf_fail(self):
        """测试查询账户余额失败"""
        payload = {
            "userId": ""
        }
        r = requests.get(self.base_url, params=payload)
        result = r.json()
        print(result)
        self.assertEqual(result['code'], "-2")
        self.assertEqual(result['message'], "失败")
        self.assertEqual(result['content'], "参数错误")

    def test_balanceOf_noExist(self):
        """测试查询账户余额不存在"""
        payload = {
            "userId": "org20"
        }
        r = requests.get(self.base_url, params=payload)
        result = r.json()
        print(result)
        self.assertEqual(result['code'], "-1")
        self.assertEqual(result['message'], "用户异常")
        self.assertEqual(result['content'], "org20 用户不存在")


if __name__ == '__main__':
    # test_data.init_data()  # 初始化接口测试数据
    unittest.main()
