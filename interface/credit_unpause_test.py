# coding=utf-8
import os
import sys
import unittest
import requests
# reload(__import__('sys')).setdefaultencoding('utf-8')
# parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# sys.path.insert(0, parent_dir)


class UnpauseTest(unittest.TestCase):
    """解冻合约"""

    def setUp(self):
        self.base_url = "http://192.168.50.166:9090/credit/unpause"

    def tearDown(self):
        pass

    def test_unpause_success(self):
        """测试解冻合约成功"""
        payload = {
            "adminId": "admin"
        }
        r = requests.post(self.base_url, data=payload)
        result = r.json()
        print(result)
        self.assertEqual(result['code'], "0")
        self.assertEqual(result['message'], "解冻合约成功")

    def test_unpause_noExist(self):
        """测试解冻合约不存在"""
        payload = {
            "adminId": ""
        }
        r = requests.post(self.base_url, data=payload)
        result = r.json()
        print(result)
        self.assertEqual(result['code'], "-1")
        self.assertEqual(result['message'], "异常")
        self.assertEqual(result['content'], "管理员不存在或权限不足")


if __name__ == '__main__':
    # test_data.init_data()  # 初始化接口测试数据
    unittest.main()
