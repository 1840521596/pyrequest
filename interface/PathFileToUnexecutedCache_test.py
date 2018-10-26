# coding=utf-8
import os
import sys
import unittest
import requests

# reload(__import__('sys')).setdefaultencoding('utf-8')
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parent_dir)


class PathFileToUnexecutedCacheTest(unittest.TestCase):
    """指定日期的文件放入到未执行的缓存中"""

    def setUp(self):
        self.base_url = "https://tsdciproxy.bqj.cn/insertOneToRedis"

    def tearDown(self):
        pass

    def test_path_file_to_unexecuted_cache(self):
        """指定路径（系统运行环境的路径）的文件放入到未执行的缓存中"""
        payload = {
            'filePath': '/opt/dci_data/2018-10-26/OS201810271111111110_134440.log'}

        r = requests.post(self.base_url, params=payload)
        result = r.json()
        print(result)
