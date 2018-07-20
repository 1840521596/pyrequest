# coding=utf-8
import os
import sys
import unittest
import requests

# reload(__import__('sys')).setdefaultencoding('utf-8')
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parent_dir)


class CreateTest(unittest.TestCase):
    """创建存证"""

    def setUp(self):
        self.base_url = "http://192.168.50.166:9090/copyright/create"

    def tearDown(self):
        pass

    def test_create_success(self):
        """测试创建存证成功"""
        payload = {
            "userId": "org1",
            "hash": "tester1engineer",
            "value": "work hard for better life!"
        }
        r = requests.post(self.base_url, data=payload)
        result = r.json()
        print(result)
        self.assertEqual(result['code'], "0")
        self.assertEqual(result['message'], "存证成功")

    def test_create_fail(self):
        """测试参数为空创建失败"""
        payload = {
            "userId": "",
            "hash": "tester1engineer",
            "value": "work hard for better life!"
            }
        r = requests.post(self.base_url, data=payload)
        result = r.json()
        print(result)
        self.assertEqual(result['code'], "-2")
        self.assertEqual(result['message'], "存证失败")
        self.assertEqual(result['content'], "请检查是否有参数为空")

    def test_create_noExist(self):
        """测试创建用户ID不存在"""
        payload = {
            "userId": "org20",
            "hash": "tester1engineer",
            "value": "work hard for better life!"
            }
        r = requests.post(self.base_url, data=payload)
        result = r.json()
        print(result)
        self.assertEqual(result['code'], "-1")
        self.assertEqual(result['message'], "用户异常")
        self.assertEqual(result['content'], "org20 用户不存在")


if __name__ == '__main__':
    # test_data.init_data()  # 初始化接口测试数据
    unittest.main()
