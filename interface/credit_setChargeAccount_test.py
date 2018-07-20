# coding=utf-8
import os
import sys
import unittest
import requests
# reload(__import__('sys')).setdefaultencoding('utf-8')
# parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# sys.path.insert(0, parent_dir)


class SetCreditChargeAccount(unittest.TestCase):
    """设置转账收费账户地址"""

    def setUp(self):
        self.base_url = "http://192.168.50.166:9090/credit/setChargeAccount"

    def tearDown(self):
        pass

    def test_set_charge_account_success(self):
        """测试设置转账收费账户成功"""
        payload = {
            "adminId": "admin",
            "tollerAccount": "0x23ebd90bafe2c344ba920c69470d238ada07a37f"
        }
        r = requests.post(self.base_url, data=payload)
        result = r.json()
        print(result)
        self.assertEqual(result['code'], "0")
        self.assertEqual(result['message'], "设置转账收费账户地址成功")

    def test_set_credit_contract_fail(self):
        """测试设置收费账户失败"""
        payload = {
            "adminId": "",
            "tollerAccount": ""
        }
        r = requests.post(self.base_url, data=payload)
        print(r)
        result = r.json()
        print(result)
        self.assertEqual(result['code'], "-2")
        self.assertEqual(result['message'], "设置失败")


if __name__ == '__main__':
    # test_data.init_data()  # 初始化接口测试数据
    unittest.main()
