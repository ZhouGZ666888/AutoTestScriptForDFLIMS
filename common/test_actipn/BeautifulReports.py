import sys
from io import StringIO as StringIO
import json
import unittest
import platform
import base64
from distutils.sysconfig import get_python_lib
import traceback
from functools import wraps
from conf.all_path import *
import logging

__all__ = ['BeautifulReports.py']

HTML_IMG_TEMPLATE = """
    <a href="data:image/png;base64, {}">
    <img src="data:image/png;base64, {}" width="800px" height="500px"/>
    </a>
    <br></br>
"""


class OutputRedirector(object):
    """ Wrapper to redirect stdout or stderr """

    def __init__(self, fp):
        self.fp = fp

    def write(self, s):
        self.fp.write(s)

    def writelines(self, lines):
        self.fp.writelines(lines)

    def flush(self):
        self.fp.flush()


stdout_redirector = OutputRedirector(sys.stdout)
stderr_redirector = OutputRedirector(sys.stderr)

SYSSTR = platform.system()
SITE_PAKAGE_PATH = get_python_lib()

FIELDS = {
    "testPass": 0,
    "testResult": [
    ],
    "testName": "",
    "testAll": 0,
    "testFail": 0,
    "beginTime": "",
    "totalTime": "",
    "testSkip": 0
}


class PATH:
    """ all file PATH meta """
    config_tmp_path = SITE_PAKAGE_PATH + '/BeautifulReport/template/template'


class MakeResultJson:
    """ make html table tags """

    def __init__(self, datas: tuple):
        """
        init self object
        :param datas: 拿到所有返回数据结构
        """
        self.datas = datas
        self.result_schema = {}

    def __setitem__(self, key, value):
        """

        :param key: self[key]
        :param value: value
        :return:
        """
        self[key] = value

    def __repr__(self) -> str:
        """
            返回对象的html结构体
        :rtype: dict
        :return: self的repr对象, 返回一个构造完成的tr表单
        """
        keys = (
            'className',
            'methodName',
            'description',
            'spendTime',
            'status',
            'log',
        )
        for key, data in zip(keys, self.datas):
            self.result_schema.setdefault(key, data)
        return json.dumps(self.result_schema)


class ReportTestResult(unittest.TestResult):
    """override"""

    def __init__(self, suite, stream=sys.stdout):
        """pass"""
        super(ReportTestResult, self).__init__()

        self.begin_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

        self.start_time = 0

        self.stream = stream

        self.end_time = 0

        self.failure_count = 0

        self.error_count = 0

        self.loggor = logging.getLogger('kkb')

    def startTest(self, test) -> None:
        """当测试用例测试即将运行时调用
    
        :return:"""
        unittest.TestResult.startTest(self, test)

        stdout_redirector.fp = self.outputBuffer

        stderr_redirector.fp = self.outputBuffer

        self.sys_stdout = sys.stdout

        self.sys_stderr = sys.stderr  # self.sys_stdout = sys.stderr

        sys.stdout = stdout_redirector

        sys.stderr = stderr_redirector

        self.start_time = time.time()  # ----add logging output-----fancc

        self.log_cap = StringIO()

        self.ch = logging.StreamHandler(self.log_cap)

        self.ch.setLevel(logging.DEBUG)

        myfmt = logging.Formatter(
            '%(asctime)s - %(name)s - "%(filename)s: %(lineno)d" - %(funcName)s - %(levelname)s - %(message)s')

        self.ch.setFormatter(myfmt)

        self.loggor.addHandler(self.ch)

    def complete_output(self):
        """Disconnect output redirection and return buffer.

        Safe to call multiple times."""

        if self.sys_stdout:
            sys.stdout = self.sys_stdout

            sys.stderr = self.sys_stdout

            self.sys_stdout = None

            self.sys_stdout = None  # add log out put ---------fancc

        return self.outputBuffer.getvalue() + '\n' + self.log_cap.getvalue()

    def stopTest(self, test) -> None:
        """当测试用力执行完成后进行调用
    
        :return:"""
        self.end_time = '{0:.3} s'.format((time.time() - self.start_time))

        self.result_list.append(self.get_all_result_info_tuple(test))  # 清除log的handle----fancc

        self.complete_output()

        self.loggor.removeHandler(self.ch)
