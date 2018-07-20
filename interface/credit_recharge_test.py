# coding=utf-8
import os
import sys
import unittest
import requests
# reload(__import__('sys')).setdefaultencoding('utf-8')
# parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# sys.path.insert(0, parent_dir)


class RechargeAccount(unittest.TestCase):
    """充值金额"""

    def setUp(self):
        self.base_url = "http://192.168.50.166:9090/credit/recharge"

    def tearDown(self):
        pass

    def test_recharge_success(self):
        """测试充值金额成功"""
        payload = {
            "admin": "admin",
            "userId": "org1",
            "value": "10000"
        }
        r = requests.post(self.base_url, data=payload)
        result = r.json()
        print(result)
        self.assertEqual(result['code'], "0")
        self.assertEqual(result['message'], "充值成功")

    def test_recharge_fail(self):
        """测试充值金额失败"""
        payload = {
            "admin": "",
            "userId": "org1",
            "value": "500"
        }
        r = requests.post(self.base_url, data=payload)
        print(r)
        result = r.json()
        print(result)
        self.assertEqual(result['code'], "-2")
        self.assertEqual(result['message'], "充值失败")
        self.assertEqual(result['content'], "请检查是否有参数为空")

    def test_recharge_admin_noExist(self):
        """测试充值管理员不存在"""
        payload = {
            "admin": "admin1",
            "userId": "org1",
            "value": "500"
        }
        r = requests.post(self.base_url, data=payload)
        print(r)
        result = r.json()
        print(result)
        self.assertEqual(result['code'], "-1")
        self.assertEqual(result['message'], "异常")
        self.assertEqual(result['content'], "管理员不存在或权限不足")

    def test_recharge_userId_noExist(self):
        """测试充值用户不存在"""
        payload = {
            "admin": "admin",
            "userId": "org20",
            "value": "500"
        }
        r = requests.post(self.base_url, data=payload)
        print(r)
        result = r.json()
        print(result)
        self.assertEqual(result['code'], "-1")
        self.assertEqual(result['message'], "用户异常")
        self.assertEqual(result['content'], "org20 用户不存在")


if __name__ == '__main__':
    # test_data.init_data()  # 初始化接口测试数据
    unittest.main()
