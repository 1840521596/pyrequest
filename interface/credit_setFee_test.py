# coding=utf-8
import os
import sys
import unittest
import requests
# reload(__import__('sys')).setdefaultencoding('utf-8')
# parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# sys.path.insert(0, parent_dir)


class SetFee(unittest.TestCase):
    """设置转账费率"""

    def setUp(self):
        self.base_url = "http://192.168.50.166:9090/credit/setFee"

    def tearDown(self):
        pass

    def test_set_fee_success(self):
        """测试设置转账费率成功"""
        payload = {
            "adminId": "admin",
            "maxFee": "100",
            "minFee": "0.01",
            "feeRate": "0.01"
        }
        r = requests.post(self.base_url, data=payload)
        result = r.json()
        print(result)
        self.assertEqual(result['code'], "0")
        self.assertEqual(result['message'], "设置转账费率成功")

    def test_set_fee_fail(self):
        """测试设置转账费率失败"""
        payload = {
            "adminId": "",
            "maxFee": "100",
            "minFee": "0.01",
            "feeRate": "0.01"
        }
        r = requests.post(self.base_url, data=payload)
        result = r.json()
        print(result)
        self.assertEqual(result['code'], "-2")
        self.assertEqual(result['message'], "设置失败")
        self.assertEqual(result['content'], "请检查是否有参数为空")

    def test_set_fee_null(self):
        """测试设置转账费率为空"""
        payload = {
            "adminId": "",
            "maxFee": "",
            "minFee": "",
            "feeRate": ""
        }
        r = requests.post(self.base_url, data=payload)
        result = r.json()
        print(result)
        self.assertEqual(result['status'], 400)
        self.assertEqual(result['error'], "Bad Request")


if __name__ == '__main__':
    # test_data.init_data()  # 初始化接口测试数据
    unittest.main()
