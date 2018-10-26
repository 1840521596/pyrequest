# coding=utf-8
import os
import sys
import unittest
import requests

# reload(__import__('sys')).setdefaultencoding('utf-8')
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parent_dir)


class DateFileToUnexecutedCache(unittest.TestCase):
    """指定日期的文件放入到未执行的缓存中"""

    def setUp(self):
        self.base_url = "https://tsdciproxy.bqj.cn/insertToRedis"

    def tearDown(self):
        pass

    def test_date_file_to_unexecuted_cache(self):
        """指定日期的文件放入到未执行的缓存中"""
        payload = {
            'dateStr': '2018-10-26'}

        r = requests.post(self.base_url, params=payload)
        result = r.json()
        print(result)

    def test_date_file_empty_verify(self):
        """指定日期的文件为空验证"""
        payload = {
            'dateStr': '2018-10-99'}

        r = requests.post(self.base_url, params=payload)
        result = r.json()
        print(result)
        self.assertIn('数据目录为空！', result['message'])

    def test_date_file_style_verify(self):
        """指定日期的文件格式验证"""
        payload = {
            'dateStr': ''}

        r = requests.post(self.base_url, params=payload)
        result = r.json()
        print(result)
        self.assertEqual(result['message'], '日期格式不正确！')
