# coding=utf-8
import os
import sys
import unittest
import requests

# reload(__import__('sys')).setdefaultencoding('utf-8')
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parent_dir)


class AllFileDetailInfoTest(unittest.TestCase):
    """批准授权存证次数"""

    def setUp(self):
        self.base_url = "https://tsdciproxy.bqj.cn/getAllFile"

    def tearDown(self):
        pass

    def test_all_file_detail_info(self):
        """查询所有文件处理详情"""
        payload = {
            '': ''}

        r = requests.post(self.base_url, params=payload)
        result = r.json()
        print(result)
        if result['message'] == '获取所有的文件记录，请求成功':
            self.assertEqual(result['message'], '获取所有的文件记录，请求成功')
        else:
            return False
