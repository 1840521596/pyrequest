# coding=utf-8
import os
import sys
import unittest
import requests

# reload(__import__('sys')).setdefaultencoding('utf-8')
# parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# sys.path.insert(0, parent_dir)


class SetCreditContract(unittest.TestCase):
    """设置积分合约地址"""

    def setUp(self):
        self.base_url = "http://192.168.50.166:9090/copyright/setCreditContract"

    def tearDown(self):
        pass

    def test_set_credit_contract_success(self):
        """测试设置积分合约地址成功"""
        payload = {
            "adminId": "admin",
            "solAddress": "0x74132cb7037b0615df8dd258567dfa0fd260beb9"
        }
        r = requests.post(self.base_url, data=payload)
        result = r.json()
        print(result)
        self.assertEqual(result['code'], "0")
        self.assertEqual(result['message'], "设置积分合约地址成功")

    def test_set_credit_contract_fail(self):
        """测试设置积分合约地址失败"""
        payload = {
            "adminId": "",
            "solAddress": "0x74132cb7037b0615df8dd258567dfa0fd260beb9"
        }
        r = requests.post(self.base_url, data=payload)
        result = r.json()
        print(result)
        self.assertEqual(result['code'], "-2")
        self.assertEqual(result['message'], "设置失败")


if __name__ == '__main__':
    # test_data.init_data()  # 初始化接口测试数据
    unittest.main()
