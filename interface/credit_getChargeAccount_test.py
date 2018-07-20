# coding=utf-8
import os
import sys
import unittest
import requests
# reload(__import__('sys')).setdefaultencoding('utf-8')
# parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# sys.path.insert(0, parent_dir)


class GetChargeAccount(unittest.TestCase):
    """查询转账收费账户地址"""

    def setUp(self):
        self.base_url = "http://192.168.50.166:9090/credit/getChargeAccount"

    def tearDown(self):
        pass

    def test_get_chargeAccount_success(self):
        """测试查询收费账户地址成功"""
        r = requests.get(self.base_url, params={'': ''})
        result = r.json()
        print(result)
        self.assertEqual(result['code'], "0")
        self.assertEqual(result['message'], "查询转账收费账户地址成功")


if __name__ == '__main__':
    # test_data.init_data()  # 初始化接口测试数据
    unittest.main()
