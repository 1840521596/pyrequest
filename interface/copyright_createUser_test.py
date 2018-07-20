# coding=utf-8
import os
import sys
import unittest
import requests

# reload(__import__('sys')).setdefaultencoding('utf-8')
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parent_dir)


class CreateUserTest(unittest.TestCase):
    """创建管理员用户"""

    def setUp(self):
        self.base_url = "http://192.168.50.166:9090/copyright/createUser"

    def tearDown(self):
        pass

    def test_create_user_all_repeat(self):
        """测试创建用户重复"""
        payload = {
            "userId": "org5",
            "iDCard": "14263588888888"
        }
        r = requests.post(self.base_url, data=payload)
        result = r.json()
        print(result)
        self.assertEqual(result['code'], "50")
        self.assertEqual(result['message'], "用户已经创建过")

    def test_create_user_all_null(self):
        """测试创建用户为空"""
        payload = {
                "userId": "",
                "iDCard": ""
            }
        r = requests.post(self.base_url, data=payload)
        result = r.json()
        print(result)
        self.assertEqual(result['code'], "-2")
        self.assertEqual(result['message'], "参数错误")

    def test_create_user_success(self):
        """测试创建用户成功"""
        payload = {
                "userId": "userPan",
                "iDCard": "14263522345678"
            }
        r = requests.post(self.base_url, data=payload)
        result = r.json()
        print(result)
        self.assertEqual(result['code'], "0")
        self.assertEqual(result['message'], "创建成功")


if __name__ == '__main__':
    # test_data.init_data()  # 初始化接口测试数据
    unittest.main()
