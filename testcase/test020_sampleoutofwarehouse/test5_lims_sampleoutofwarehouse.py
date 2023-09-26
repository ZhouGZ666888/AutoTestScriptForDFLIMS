# -*- coding: utf-8 -*-
# @Time    : 2022/09/09
# @Author  : guanzhou.zhou
# QPCR样本出库的一系列操作测试用例

import re
import unittest
import ddt
from common.xlsx_excel import get_lims_for_excel_by_rows
from conf.all_path import wkgj_file_path, wkfj_file_path, hstq_file_path_mNGS
from pageobj.sampleOutOfWarehouse import GetSampleCK
from conf.enter_tab import EnterTab
from common.logs import log
from common.setup_teardown import MyTest


@ddt.ddt
class SampleCK(MyTest):

    Testdata = [
        {"lims_nub": "", "info": "请录入相关内容"},
        {"lims_nub": "error", "info": "以下样本未找到或不是库内的样本，无法进行出库操作，请检查"}
    ]

    def setUp(self) -> None:
        """
        初始化浏览器驱动
        """
        self.ybck = GetSampleCK(self.driver)

    def test01_addQpcrSampleOut(self):
        """
        出库模块选择qpcr出库
        """
        self.initialize()
        EnterTab.enter_storage_center(self.basepage)
        EnterTab.enter_withdraw(self.basepage)

        self.ybck.add_qpcrSample_ck()

    @ddt.data(*Testdata)
    def test02_inputWrongNumber(self, testData):
        """
        测试录入错误的QPCR样本号，系统提示
        """
        log.info('分别录入错误的和不录入样本号，进行检索')
        self.ybck.search_sample(testData['lims_nub'])
        result = re.search(testData['lims_nub'], self.ybck.get_source)
        self.assertIsNotNone(result)

    def test03_inputCorrectNumber(self):
        """
        测试录入正确的QPCR样本号并正常出库流程
        """
        log.info('录入正确的出库样本号')
        # sample_lims = get_lims_for_excel_by_rows(wkgj_file_path, 0, -5, 'lims号')
        otherNub = get_lims_for_excel_by_rows(wkfj_file_path, 0, 1, 'lims号')  # 其他类型样本号
        self.ybck.process_error_sample()
        self.ybck.add_qpcrSample_ck()
        self.ybck.search_sample(otherNub)
        log.info('选择QPCR菌种')
        self.ybck.qpcr_check_bacteria()
        self.ybck.qpcr_sample_ck_reason()  # 填写出库理由并提交出库

    def test04_checkSampleOut(self):
        """
        测试qpcr出库在流转表配置了正确的建库类型
        """
        log.info('出库成功页面跳转到流转表样本出库节点')
        self.ybck.switch_to_window_handle()
        result = re.search(r"请确认本次出库的建库节点的样本配置了正确的建库类型", self.ybck.get_source)
        self.ybck.close_page_info()
        EnterTab.enter_storage_center(self.basepage)
        EnterTab.enter_withdraw(self.basepage)

        self.assertIsNotNone(result)


if __name__ == '__main__':
    unittest.main()
