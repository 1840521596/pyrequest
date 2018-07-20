# coding=utf-8
import os
import sys
import unittest
import requests
# reload(__import__('sys')).setdefaultencoding('utf-8')
# parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# sys.path.insert(0, parent_dir)


class SetFee(unittest.TestCase):
    """设置存证费"""

    def setUp(self):
        self.base_url = "http://192.168.50.166:9090/copyright/setFee"

    def tearDown(self):
        pass

    def test_set_fee_success(self):
        """测试设置存证费用成功"""
        payload = {
            "adminId": "admin",
            "fee": "0.01"
        }
        r = requests.post(self.base_url, data=payload)
        result = r.json()
        print(result)
        self.assertEqual(result['code'], "0")
        self.assertEqual(result['message'], "设置存证费用成功")

    def test_set_fee_fail(self):
        """测试设置存证费用失败"""
        payload = {
            "adminId": "admin",
            "fee": ''
        }
        r = requests.post(self.base_url, data=payload)
        result = r.json()
        print(result)
        self.assertEqual(result['status'], 400)
        self.assertEqual(result['error'], 'Bad Request')


if __name__ == '__main__':
    # test_data.init_data()  # 初始化接口测试数据
    unittest.main()
