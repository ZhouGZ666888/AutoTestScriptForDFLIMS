# -*- coding: utf-8 -*-
# @Time    : 2023/05/24
# @Author  : guanzhong.zhou
# @File    : mPCR模块测试用例

import unittest
from pageobj.mPCRPage import mPCRTest
from conf.enter_tab import EnterTab
from common.logs import log
from common.setup_teardown import MyTest


class mPCRTestCase(MyTest):
    """mPCR模块测试用例"""

    def setUp(self) -> None:
        """初始化浏览器驱动"""
        self.mpcr = mPCRTest(self.driver)

    def test01_add_mPCR_task(self):
        """测试新建mPCR任务单，在待选表选择任务类型、sop,检索lims号，添加、保存任务单"""
        self.initialize()
        log.info('登录系统，进入mPCR页面')
        EnterTab.enter_test_center(self.basepage)
        EnterTab.enter_mPCR(self.basepage)  # 点击mPCR导航树

        self.mpcr.add_task()  # 新建任务单，选择任务类型、操作类型、sop

    def test02_item_check_lims_num(self):
        """待选表核对lims号，进入明细表"""
        log.info('核对lims，添加至任务单')
        info = self.mpcr.check_lims_num()  # 核对lims，添加至任务单
        log.info('保存任务单，mPCR明细表')
        self.mpcr.enter_result_list()  # 保存任务单，进入明细表
        if info:
            self.assertEqual(info, "任务单保存成功", "保存样本到明细表失败！！")

    def test03_mPCR_detail_auto_complete(self):
        """测试mPCR明细表自动计算"""
        log.info("mPCR明细表自动计算")
        self.mpcr.detail_auto_complete()

    def test04_mPCR_detail_position_of_96_well_plate(self):
        """测试mPCR明细表录入96孔版位置"""
        log.info("mPCR明细表选，录入96孔版位置")
        self.mpcr.position_of_96_well_plate()
        log.info('进入mPCR结果表')
        self.mpcr.enter_result()  # 进入mPCR结果表

    def test05_mPCR_result_edit_ntc(self):
        """测试mPCR结果表修改NTC对照"""
        log.info("mPCR结果表，修改NTC对照")
        self.mpcr.result_edit_ntc()

    def test06_mPCR_result_edit_product_type(self):
        """测试mPCR结果表修改产物类型"""
        log.info("mPCR结果表，修改产物类型")
        self.mpcr.result_product_type()

    def test07_mPCR_result_batch_data(self):
        """测试mPCR结果表批量数量录入"""
        log.info("mPCR结果表，批量数量录入")
        self.mpcr.result_batch_data()

    def test08_mPCR_result_import_mpcr_consistence_amt(self):
        """测试mPCR结果表批量导入产物浓度"""
        log.info("mPCR结果表，批量导入产物浓度")
        self.mpcr.result_import_mpcr_consistence_amt()

    def test09_mPCR_result_import_batch_paste_position(self):
        """测试mPCR结果表批量导入盒内位置"""
        log.info("mPCR结果表，批量导入盒内位置")
        self.mpcr.result_import_batch_paste_position()

    def test10_mPCR_result_auto_complete(self):
        """测试mPCR结果表自动计算"""
        log.info("mPCR结果表，自动计算")
        self.mpcr.result_auto_complete()

    def test11_mPCR_result_submit_sample(self):
        """测试mPCR结果表提交表单"""
        log.info("mPCR结果表，提交")
        info = self.mpcr.result_submit_sample()

        log.info("mPCR结果表，结果表下一步数据写入对应Excel")
        self.mpcr.write_data_to_excel()
        self.assertEqual('已提交', info, "结果表提交样本失败！")

    def test12_mPCR_result_enter_detail(self):
        """测试mPCR结果表返回明细表完成提交入库操作"""
        log.info("mPCR结果表，返回明细表完成提交入库操作")
        self.mpcr.enter_detail()

    def test13_detail_submit(self):
        """测试明细表提交操作"""
        self.mpcr.detail_submit()  # 明细表提交操作

    def test14_detail_into_storage(self):
        """测试明细表入库操作"""
        self.mpcr.detail_into_storage()  # 明细表样本入库操作

    def test15_complete_task(self):
        """测试返回结果表，完成任务单"""
        self.mpcr.enter_result()
        save_info3 = self.mpcr.complete_task()
        self.assertEqual(save_info3.strip(), '完成', '完成任务单失败！')

    def test16_search_task_by_lims(self):
        """测试根据添加到的任务单中的lims样本号搜索对应的任务单"""
        EnterTab.enter_test_center(self.basepage)
        EnterTab.enter_mPCR(self.basepage)  # 点击mPCR导航树
        log.info(" 测试根据添加到的任务单中的lims样本号搜索对应的任务单")
        samples = self.mpcr.serach_task()  # 根据lims号搜索任务单号
        self.assertNotEqual(samples, 0, "查询结果错误，查询失败！")


if __name__ == '__main__':
    unittest.main()
