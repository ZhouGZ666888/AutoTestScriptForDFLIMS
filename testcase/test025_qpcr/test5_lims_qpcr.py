# -*- coding: utf-8 -*-
# @Time    : 2022/09/14
# @Author  : guanzhong.zhou
# @File    : QPCR复检测试用例

import unittest
from common.logs import log
from common.setup_teardown import MyTest
from conf.all_path import qpcr_dxk_file_path
from conf.enter_tab import EnterTab
from pageobj.qpcrPage import QpcrPage, enter_detail_list_btn, go_result


class QpcrReinspect(MyTest):

    def setUp(self) -> None:
        """
        初始化浏览器驱动
        """
        self.qpcr = QpcrPage(self.driver)

    def test01_add_dxk_task(self):
        """
        新建qpcr迪讯康复检任务
        """
        self.initialize()
        log.info('进入QPCR复检页面')
        EnterTab.enter_test_center(self.basepage)
        EnterTab.enter_qpcr_recheck(self.basepage)

        log.info('新建qpcr迪讯康复检任务')
        self.qpcr.add_qpcr_task()
        log.info('待选表选择迪讯康任务类型')
        self.qpcr.to_be_select('迪迅康')

        log.info('选中样本进入明细表')
        self.qpcr.add_sample_to_detail()
        self.qpcr.enter_result_list(enter_detail_list_btn, '迪讯康复检任务明细表')

    def test02_qpcr_detail(self):
        """
        测试qpcr明细表自动计算、提交入库
        """
        log.info('qpcr明细表添加NC/PC')
        self.qpcr.qpcr_detail_addncpc()
        log.info(' qpcr明细表自动计算')
        self.qpcr.qpcr_detail()
        log.info('qpcr明细表提交')
        self.qpcr.detail_sumbit()
        log.info('qpcr明细表入库')
        page_info = self.qpcr.detail_into_storage()
        self.qpcr.enter_result_list(go_result, ' qpcr结果表')  # 保存任务单，进入结果表
        self.assertEqual(page_info, '完成', "入库失败，请检查数据！！！")

    def test03_qpcr_result(self):
        """
        qpcr结果表导出复检信息、导入复检信息、自动判读测试
        """
        log.info('QPCR结果表，导出复孔信息')
        self.qpcr.qpcr_result_export_out_btn()
        log.info('QPCR结果表，导入复孔信息')
        self.qpcr.qpcr_result_export_in_btn()
        log.info('QPCR结果表，自动判读')
        self.qpcr.result_auto_Complete()
        log.info('qpcr结果表提交')
        samples_status = self.qpcr.result_submit(14)
        self.assertEqual(samples_status, '完成', "提交失败！！！")

    def test04_qpcr_complete_detail(self):
        """
        qpcr结果表完成任务单
        """
        # log.info('qpcr返回明细表完成nc/pc 样本提交')
        # self.qpcr.go_back_detail()
        log.info('qpcr结果表完成任务单')
        task_status = self.qpcr.complete_task()
        self.assertEqual(task_status.strip(), '完成', '完成任务单失败！')

    def test05_add_mNGS_task(self):
        """
        新建qpcr-mNGS复检任务
        """

        log.info('进入QPCR复检页面')
        EnterTab.enter_qpcr_recheck(self.basepage)

        log.info('新建qpcrmNGS复检任务')
        self.qpcr.add_qpcr_task()
        log.info('待选表选择mNGS复检任务类型')
        self.qpcr.to_be_select('mNGS')

        log.info('选中样本进入明细表')
        self.qpcr.add_sample_to_detail()
        self.qpcr.enter_result_list(enter_detail_list_btn, 'mNGS复检任务明细表')

    def test06_qpcr_mNGS_detail(self):
        """
        测试qpcr明细表添加NC/PC，自动计算、提交入库
        """
        log.info('qpcr明细表添加NC/PC')
        self.qpcr.qpcr_detail_addncpc()
        log.info(' qpcr明细表自动计算')
        self.qpcr.qpcr_detail()
        log.info('qpcr明细表提交')
        self.qpcr.detail_sumbit()
        log.info('qpcr明细表入库')
        page_info = self.qpcr.detail_into_storage()
        self.qpcr.enter_result_list(go_result, ' qpcr结果表')  # 保存任务单，进入结果表
        self.assertEqual(page_info, '完成', "入库失败，请检查数据！！！")

    def test07_qpcr_mNGS_result(self):
        """
        qpcr结果表导出复检信息、导入复检信息、自动判读测试
        """
        log.info('QPCR结果表，导出复孔信息')
        self.qpcr.qpcr_result_export_out_btn()

        log.info('QPCR结果表，导入复孔信息')
        self.qpcr.qpcr_result_export_in_btn()

        log.info('QPCR结果表，自动判读')
        self.qpcr.result_auto_Complete()

        log.info('qpcr结果表提交')
        samples_status = self.qpcr.result_submit(13)
        self.assertEqual(samples_status, '完成', "提交失败！！！")

    def test08_qpcr_mNGS_complete_detail(self):
        """
        qpcr结果表完成任务单
        """
        # log.info('qpcr返回明细表完成nc/pc 样本提交')
        # self.qpcr.go_back_detail()
        log.info('qpcr结果表完成任务单')
        task_status = self.qpcr.complete_task()
        self.assertEqual(task_status.strip(), '完成', '完成任务单失败！')

    def test09_add_other_task(self):
        """
        新建qpcr-其他类型复检任务
        """

        log.info('进入QPCR复检页面')
        EnterTab.enter_qpcr_recheck(self.basepage)

        log.info('新建qpcr其他类型任务')
        self.qpcr.add_qpcr_task()
        log.info('待选表选择其他类型')
        self.qpcr.to_be_select('其他')

        log.info('选中样本进入明细表')
        self.qpcr.add_sample_to_detail()
        self.qpcr.enter_result_list(enter_detail_list_btn, '其他复检任务明细表')

    def test10_qpcr_other_detail(self):
        """
        测试qpcr明细表自动计算、提交入库
        """
        log.info('qpcr明细表添加NC/PC')
        self.qpcr.qpcr_detail_addncpc()
        log.info(' qpcr明细表自动计算')
        self.qpcr.qpcr_detail()
        log.info('qpcr明细表提交')
        self.qpcr.detail_sumbit()
        log.info('qpcr明细表入库')
        page_info = self.qpcr.detail_into_storage()
        self.qpcr.enter_result_list(go_result, ' qpcr结果表')  # 保存任务单，进入结果表
        self.assertEqual(page_info, '完成', "入库失败，请检查数据！！！")

    def test11_qpcr_other_result(self):
        """
        qpcr结果表添加NC/PC，导出复检信息、导入复检信息、自动判读测试
        """
        log.info('QPCR结果表，导出复孔信息')
        self.qpcr.qpcr_result_export_out_btn()

        log.info('QPCR结果表，导入复孔信息')
        self.qpcr.qpcr_result_export_in_btn()

        log.info('QPCR结果表，自动判读')
        self.qpcr.result_auto_Complete()

        log.info('qpcr结果表提交')
        samples_status = self.qpcr.result_submit(13)
        self.assertEqual(samples_status, '完成', "提交失败！！！")

    def test12_qpcr_other_complete_detail(self):
        """
        qpcr明细表完成NC/PC任务，结果表完成任务单
        """
        # log.info('qpcr返回明细表完成nc/pc 样本提交')
        # self.qpcr.go_back_detail()
        log.info('qpcr结果表完成任务单')
        task_status = self.qpcr.complete_task()
        self.assertEqual(task_status.strip(), '完成', '完成任务单失败！')

    def test13_search_task_by_lims(self):
        """
        测试根据添加到的任务单中的lims样本号搜索对应的任务单
        """

        log.info('进入QPCR复检任务单页面')
        EnterTab.enter_qpcr_recheck(self.basepage)

        samples = self.qpcr.serach_task(qpcr_dxk_file_path)  # 根据lims号搜索任务单号
        self.assertNotEqual(samples, 0, "查询结果错误，查询失败！")


if __name__ == '__main__':
    unittest.main()
