# coding=utf-8
import os
import sys
import unittest
import requests

# reload(__import__('sys')).setdefaultencoding('utf-8')
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parent_dir)


class DeleteAllRedis(unittest.TestCase):
    """批准授权存证次数"""

    def setUp(self):
        self.base_url = "https://tsdciproxy.bqj.cn/deleteAllRedis"

    def tearDown(self):
        pass

    def test_Delete_All_Redis(self):
        """删除所有Redis"""
        payload = {
            '': ''}

        r = requests.post(self.base_url, params=payload)
        result = r.json()
        print(result)
        if result['message'] == '删除成功！':
            self.assertEqual(result['message'], '删除成功！')
        else:
            return False

