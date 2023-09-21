# -*- coding: utf-8 -*-
# @Time    : 2022/09/27
# @Author  : guanzhong.zhou
# @File    : 报告发送模块页面方法封装
import unittest
from pageobj.report_sendPage import ReportSendPage
from conf.enter_tab import EnterTab
from common.logs import log
from common.setup_teardown import MyTest


class ReportSend(MyTest):
    def setUp(self) -> None:
        """
        初始化浏览器驱动
        """
        self.rs = ReportSendPage(self.driver)

    def test01_serach_by_data(self):

        """测试报告发送模块，根据预计实验日期搜索待处理任务"""
        log.info('登录系统，进入报告发送页面')
        self.initialize()
        EnterTab.enter_report_center(self.basepage)  # 点击报告任务列表
        EnterTab.enter_report_send(self.basepage)  # 点击基本信息任务分配

        log.info('根据报告完成日期查询')
        result = self.rs.search_by_date()
        self.assertNotEqual(result, 0, "查询无结果！！！")

    def test02_serach_by_order(self):
        """ 测试报告发送模块，根据订单号搜索待处理任务"""
        log.info('按订单号搜索')
        result = self.rs.search_by_order()
        self.assertNotEqual(result, 0, "查询无结果！！！")

    def test03_updata_report(self):
        """测试修改报告审核状态,并保存报告信息"""
        log.info('修改报告审核状态')
        self.rs.edit_report_status()


if __name__ == '__main__':
    unittest.main()
