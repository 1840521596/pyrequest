# coding=utf-8
import os
import sys
import unittest
import requests
# reload(__import__('sys')).setdefaultencoding('utf-8')
# parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# sys.path.insert(0, parent_dir)


class CreditApprove(unittest.TestCase):
    """批准指定账户转移自己的金额"""

    def setUp(self):
        self.base_url = "http://192.168.50.166:9090/credit/approve"

    def tearDown(self):
        pass

    def test_approve_success(self):
        """测试批准指定账户转移自己的金额成功"""
        payload = {
            "operator": "org2",
            "userId": "org3",
            "value": "10000"
        }
        r = requests.post(self.base_url, data=payload)
        result = r.json()
        print(result)
        self.assertEqual(result['code'], "0")
        self.assertEqual(result['message'], "批准成功")

    def test_approve_ope_noExist(self):
        """测试批准人不存在"""
        payload = {
            "operator": "org",
            "userId": "org2",
            "value": "10"
        }
        r = requests.post(self.base_url, data=payload)
        result = r.json()
        print(result)
        self.assertEqual(result['code'], "-1")
        self.assertEqual(result['message'], "用户异常")
        self.assertEqual(result['content'], "org 用户不存在")

    def test_approve_ope_null(self):
        """测试批准人为空"""
        payload = {
            "operator": "",
            "userId": "org2",
            "value": "10"
        }
        r = requests.post(self.base_url, data=payload)
        result = r.json()
        print(result)
        self.assertEqual(result['code'], "-2")
        self.assertEqual(result['message'], "失败")
        self.assertEqual(result['content'], "请检查是否有参数为空")

    def test_approve_user_noExist(self):
        """测试被指定人不存在"""
        payload = {
            "operator": "org1",
            "userId": "org10",
            "value": "10"
        }
        r = requests.post(self.base_url, data=payload)
        result = r.json()
        print(result)
        self.assertEqual(result['code'], "-1")
        self.assertEqual(result['message'], "用户异常")
        self.assertEqual(result['content'], "org10 用户不存在")

    def test_approve_user_null(self):
        """测试被指定人为空"""
        payload = {
            "operator": "",
            "userId": "org10",
            "value": "10"
        }
        r = requests.post(self.base_url, data=payload)
        result = r.json()
        print(result)
        self.assertEqual(result['code'], "-2")
        self.assertEqual(result['message'], "失败")
        self.assertEqual(result['content'], "请检查是否有参数为空")

    def test_approve_value_null(self):
        """测试金额为空"""
        payload = {
            "operator": "org1",
            "userId": "org10",
            "value": ""
        }
        r = requests.post(self.base_url, data=payload)
        result = r.json()
        print(result)
        self.assertEqual(result['status'], 400)
        self.assertIn("Failed to convert value of type", result['message'])


if __name__ == '__main__':
    # test_data.init_data()  # 初始化接口测试数据
    unittest.main()
