# coding=utf-8
import os
import sys
import unittest
import requests
# reload(__import__('sys')).setdefaultencoding('utf-8')
# parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# sys.path.insert(0, parent_dir)


class GetCreditContract(unittest.TestCase):
    """查询查询金额合约地址"""

    def setUp(self):
        self.base_url = "http://192.168.50.166:9090/copyright/getCreditContract"

    def tearDown(self):
        pass

    def test_get_creditContract_success(self):
        """测试查询金额合约地址成功"""
        r = requests.get(self.base_url, params={'': ''})
        result = r.json()
        print(result)
        self.assertEqual(result['code'], "0")
        self.assertEqual(result['message'], "查询成功")


if __name__ == '__main__':
    # test_data.init_data()  # 初始化接口测试数据
    unittest.main()
