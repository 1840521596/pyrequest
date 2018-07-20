# coding=utf-8
import os
import sys
import unittest
import requests
# reload(__import__('sys')).setdefaultencoding('utf-8')
# parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# sys.path.insert(0, parent_dir)


class CreditRevert(unittest.TestCase):
    """撤销转账"""

    def setUp(self):
        self.base_url = "http://192.168.50.166:9090/credit/revert"

    def tearDown(self):
        pass

    def test_revert_success(self):
        """测试撤销转账成功"""
        payload = {
            "admin": "admin",
            "transHash": "0x97910f700c270fd1b0ef83d0d85cf3d55c15d963c761dbc620dbac1c2878b553"
        }
        r = requests.post(self.base_url, data=payload)
        result = r.json()
        print(result)
        self.assertEqual(result['code'], "0")
        self.assertEqual(result['message'], "撤销成功")

    def test_revert_fail(self):
        """测试撤销转账失败"""
        payload = {
            "admin": "org1",
            "transHash": "0x97910f700c270fd1b0ef83d0d85cf3d55c15d963c761dbc620dbac1c2878b553"
        }
        r = requests.post(self.base_url, data=payload)
        result = r.json()
        print(result)
        self.assertEqual(result['code'], "-1")
        self.assertEqual(result['message'], "异常")
        self.assertEqual(result['content'], "管理员不存在或权限不足")

    def test_transfer_admin_null(self):
        """测试撤销转账参数为空"""
        payload = {
            "admin": "",
            "transHash": "0x97910f700c270fd1b0ef83d0d85cf3d55c15d963c761dbc620dbac1c2878b553"
        }
        r = requests.post(self.base_url, data=payload)
        result = r.json()
        print(result)
        self.assertEqual(result['code'], "-2")
        self.assertEqual(result['message'], "撤销失败")
        self.assertEqual(result['content'], "请检查是否有参数为空")


if __name__ == '__main__':
    # test_data.init_data()  # 初始化接口测试数据
    unittest.main()
