# coding=utf-8
import os
import sys
import unittest
import requests
# reload(__import__('sys')).setdefaultencoding('utf-8')
# parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# sys.path.insert(0, parent_dir)


class CreditGetAllowance(unittest.TestCase):
    """返回能提取金额数量"""

    def setUp(self):
        self.base_url = "http://192.168.50.166:9090/credit/allowance"

    def tearDown(self):
        pass

    def test_getAllowance_success(self):
        """测试返回能提取金额数量成功"""
        payload = {
            "owner": "org1",
            "spender": "org2"
        }
        r = requests.get(self.base_url, params=payload)
        result = r.json()
        print(result)
        self.assertEqual(result['code'], "0")
        self.assertEqual(result['message'], "查询成功")

    def test_getAllowance_noExist(self):
        """测试被授权人不存在"""
        payload = {
            "owner": "org1",
            "spender": "org10"
        }
        r = requests.get(self.base_url, params=payload)
        result = r.json()
        print(result)
        self.assertEqual(result['code'], "-1")
        self.assertEqual(result['message'], "用户异常")
        self.assertEqual(result['content'], "org10 用户不存在")

    def test_getAllowance_null(self):
        """测试被授权人为空"""
        payload = {
            "owner": "org1",
            "spender": ""
        }
        r = requests.get(self.base_url, params=payload)
        result = r.json()
        print(result)
        self.assertEqual(result['code'], "-2")
        self.assertEqual(result['message'], "充值失败")
        self.assertEqual(result['content'], "请检查是否有参数为空")

    def test_getAllowance_owner_noExist(self):
        """测试授权人不存在"""
        payload = {
            "owner": "org10",
            "spender": "org1"
        }
        r = requests.get(self.base_url, params=payload)
        result = r.json()
        print(result)
        self.assertEqual(result['code'], "-1")
        self.assertEqual(result['message'], "用户异常")
        self.assertEqual(result['content'], "org10 用户不存在")

    def test_getAllowance_owner_null(self):
        """测试授权人为空"""
        payload = {
            "owner": "",
            "spender": "org1"
        }
        r = requests.get(self.base_url, params=payload)
        result = r.json()
        print(result)
        self.assertEqual(result['code'], "-2")
        self.assertEqual(result['message'], "充值失败")
        self.assertEqual(result['content'], "请检查是否有参数为空")


if __name__ == '__main__':
    # test_data.init_data()  # 初始化接口测试数据
    unittest.main()
