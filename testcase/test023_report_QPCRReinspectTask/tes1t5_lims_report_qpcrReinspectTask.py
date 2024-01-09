# -*- coding: utf-8 -*-
# @Time    : 2022/09/20
# @Author  : guanzhong.zhou
# @File    : 报告-qpcr复检任务模块测试用例
import unittest
from pageobj.report_qpcrReinspectTaskPage import QPCRReinspectTask
from conf.enter_tab import EnterTab
from common.logs import log
from common.setup_teardown import MyTest


class ReportBasicInfoTaskAssignment(MyTest):

    def setUp(self) -> None:
        """
        初始化浏览器驱动
        """
        self.qrt = QPCRReinspectTask(self.driver)

    def test01_serach_sample_by_seqSampleId(self):
        """
        测试QPCR复检任务模块，查询复检任务信息
        """
        log.info('QPCR复检任务模块，查询复检任务信息')
        self.initialize()

        EnterTab.enter_report_center(self.basepage)
        EnterTab.enter_qpcr_reinspectionTask(self.basepage)  # 点击报告上传导航树

        samples = self.qrt.serach_sample_by_seqSampleId()
        self.assertIsNot(samples, 0, "未查出复检任务样本！")

    def test02_qpcr_multiple_out(self):
        """
        测试复检任务出库功能
        """
        log.info('QPCR复检任务模块，样本出库')

        info = self.qrt.qpcr_multiple_out()
        self.assertIsNotNone(info, "未查出复检任务样本！")


if __name__ == '__main__':
    unittest.main()
