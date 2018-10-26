# coding=utf-8
import os
import sys
import unittest
import requests

# reload(__import__('sys')).setdefaultencoding('utf-8')
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parent_dir)


class CallbackContentToLocal(unittest.TestCase):
    """批准授权存证次数"""

    def setUp(self):
        self.base_url = "https://tsdciproxy.bqj.cn/CPCC/callBackServlet"

    def tearDown(self):
        pass

    def test_callback_content_to_local(self):
        """将回调内容写入本地"""
        payload = {
            'callbackMessage': '{"auditDesc":"不通过，登记类型错误，应该为美术作品。","dciCode":"","flag":false,'
                               '"registerId":"OS201810271111111111","content":""}'}

        r = requests.post(self.base_url, data=payload)
        result = r.json()
        print(result)
        self.assertEqual(result['message'], '回调成功')
