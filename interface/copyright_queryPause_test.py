# coding=utf-8
import os
import sys
import unittest
import requests

# reload(__import__('sys')).setdefaultencoding('utf-8')
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parent_dir)


class QueryPauseTest(unittest.TestCase):
    """查询合约状态"""

    def setUp(self):
        self.base_url = "http://192.168.50.166:9090/copyright/queryPause"

    def tearDown(self):
        pass

    def test_queryPause_success(self):
        """测试查询合约状态成功"""
        payload = {
            "": ""
        }
        r = requests.get(self.base_url, params=payload)
        result = r.json()
        print(result)
        self.assertEqual(result['code'], "0")
        self.assertEqual(result['message'], "查询合约状态成功")
        self.assertEqual(result['content'], True)


if __name__ == '__main__':
    # test_data.init_data()  # 初始化接口测试数据
    unittest.main()
