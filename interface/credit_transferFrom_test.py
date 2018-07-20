# coding=utf-8
import os
import sys
import time
import unittest
import requests
# reload(__import__('sys')).setdefaultencoding('utf-8')
# parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# sys.path.insert(0, parent_dir)


class CreditTransferFrom(unittest.TestCase):
    """转移指定用户金额"""

    def setUp(self):
        self.base_url = "http://192.168.50.166:9090/credit/transferFrom"

    def tearDown(self):
        pass

    def test_transferFrom_fail(self):
        """测试转移失败"""
        payload = {
            "operator": "org2",
            "formUserId": "org1",
            "toUserId": "org3",
            "value": "9909"
        }
        r = requests.post(self.base_url, data=payload)
        result = r.json()
        self.assertEqual(result['code'], "-1")
        self.assertEqual(result['message'], '授权转账失败')
        self.assertEqual(result['content'], 'BCOS获取结果失败')
        print(result)

    def test_transferFrom_success(self):
        """测试授权转账成功"""
        payload = {
            "operator": "org1",
            "formUserId": "org2",
            "toUserId": "org3",
            "value": "10.00"
        }
        r = requests.post(self.base_url, data=payload)
        result = r.json()
        print(result)
        # self.assertEqual(result['code'], "0")
        # self.assertEqual(result['message'], '授权转账成功')

    def test_transfer_toUserId_noExist(self):
        """测试转给用户不存在"""
        payload = {
            "operator": "org2",
            "formUserId": "org1",
            "toUserId": "org10",
            "value": "9909"
        }
        r = requests.post(self.base_url, data=payload)
        result = r.json()
        self.assertEqual(result['code'], "-1")
        self.assertEqual(result['message'], '用户异常')
        self.assertEqual(result['content'], 'org10 用户不存在')
        print(result)


if __name__ == '__main__':
    # test_data.init_data()  # 初始化接口测试数据
    unittest.main()
