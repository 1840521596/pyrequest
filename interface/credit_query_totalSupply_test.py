# coding=utf-8
import os
import sys
import unittest
import requests
# reload(__import__('sys')).setdefaultencoding('utf-8')
# parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# sys.path.insert(0, parent_dir)


class TotalSupply(unittest.TestCase):
    """查询发币总额"""

    def setUp(self):
        self.base_url = "http://192.168.50.166:9090/credit/totalSupply"

    def tearDown(self):
        pass

    def test_totalSupply_success(self):
        """测试查询发币总额成功"""
        payload = {
            "": ""
        }
        r = requests.get(self.base_url, params=payload)
        result = r.json()
        print(result)
        self.assertEqual(result['code'], "0")
        self.assertEqual(result['message'], "查询成功")


if __name__ == '__main__':
    # test_data.init_data()  # 初始化接口测试数据
    unittest.main()
