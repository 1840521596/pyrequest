# coding=utf-8
import os
import sys
import unittest
import requests
# reload(__import__('sys')).setdefaultencoding('utf-8')
# parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# sys.path.insert(0, parent_dir)


class GetApproveNumber(unittest.TestCase):
    """查询剩余授权存证次数"""

    def setUp(self):
        self.base_url = "http://192.168.50.166:9090/copyright/getApproveNumber"

    def tearDown(self):
        pass

    def test_get_approveNumber_success(self):
        """测试查询剩余授权存证次数成功"""
        r = requests.get(self.base_url, params={'operator': 'org1'})
        result = r.json()
        print(result)
        self.assertEqual(result['code'], "0")
        self.assertEqual(result['message'], "授权存证次数查询成功！")

    def test_get_approveNumber_noExist(self):
        """测试查询剩余授权存证次数失败"""
        r = requests.get(self.base_url, params={'operator': 'org20'})
        result = r.json()
        print(result)
        self.assertEqual(result['code'], "-1")
        self.assertEqual(result['message'], "用户异常")
        self.assertEqual(result['content'], "org20 用户不存在")

    def test_get_approveNumber_null(self):
        """测试查询剩余授权存证人为空"""
        r = requests.get(self.base_url, params={'operator': ''})
        result = r.json()
        print(result)
        self.assertEqual(result['code'], "-2")
        self.assertEqual(result['message'], "失败")
        self.assertEqual(result['content'], "请检查是否有参数为空")


if __name__ == '__main__':
    # test_data.init_data()  # 初始化接口测试数据
    unittest.main()
