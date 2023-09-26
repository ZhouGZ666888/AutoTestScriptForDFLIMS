# -*- coding: utf-8 -*-
# @Time    : 2022/04/14
# @Author  : guanzhong.zhou
import unittest
from pageobj.sample_outsendPage import *
from conf.enter_tab import EnterTab
from common.setup_teardown import MyTest


class SampleOutSend(MyTest):

    def setUp(self) -> None:
        self.sos = SampleOutSendPage(self.driver)

    def test01_add_outsend_task(self):
        """测试新建外送任务，添加外送样本并提交审核"""
        self.initialize()
        EnterTab.enter_storage_center(self.basepage)  # 点击样本库位管理的tab按钮
        EnterTab.enter_send_back(self.basepage)  # 点击样本外送的tab按钮

        log.info('新建样本外送任务')
        self.sos.add_sample_outsend_task()
        log.info('待选样本表选择样本至明细表')
        self.sos.add_sample_to_task()
        log.info('样本外送明细表处理、提交审核')
        task_statue = self.sos.outsend_detail_edit()

        self.assertEqual(task_statue, '待部门审核', "提交审核失败")

    def test02_task_for_review(self):
        """测试审核外送任务"""
        log.info('切换用户进行数据修改审批')
        self.sos.batch_submit_for_review()
        self.login_action('guanzhong.zhou')
        # EnterTab.enter_unresolve_job(self.basepage)

        log.info(' 部门审核人角色审核任务单')
        task_statue1, task_statue2 = self.sos.task_for_review()
        self.assertEqual(task_statue1, '取样中', "部门审核人审核审核失败")
        self.assertEqual(task_statue2, '待寄送', "部门审核人审核审核失败")

    def test03_sample_check(self):
        """测试审核和取样、寄送以及完成任务单"""
        log.info('切换用户进行数据修改审批')
        self.sos.batch_submit_for_review()
        self.login_action('guoqi.dong')
        EnterTab.enter_unresolve_job(self.basepage)

        log.info(' 在审核完成后，有权限用户进行取样确认操作')
        application_status = self.sos.sample_check()
        self.assertEqual(application_status, '完成', "完成任务单失败")

    def test04_search_task(self):
        """测试根据任务单检索任务"""
        EnterTab.enter_storage_center(self.basepage)  # 点击样本库位管理的tab按钮
        EnterTab.enter_send_back(self.basepage)  # 点击样本外送的tab按钮
        log.info('测试根据任务单检索任务')
        eles = self.sos.search_task()
        self.assertNotEqual(len(eles), 0, "查询任务单失败")

    def test05_testend(self):
        """结束测试，关闭系统"""
        log.info('结束测试，退出系统，关闭页面')

        self.sos.close()
        self.sos.quit()


if __name__ == '__main__':
    unittest.main()
