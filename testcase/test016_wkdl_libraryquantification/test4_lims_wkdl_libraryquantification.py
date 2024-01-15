# -*- coding: utf-8 -*-
# @Time    : 2024/01/12
# @Author  : guanzhong.zhou
# @File    : 文库定量模块测试用例

import unittest,re
from datetime import datetime
from pageobj.libraryquantificationPage import libraryquantificationPage
from conf.enter_tab import EnterTab
from common.logs import log
from common.setup_teardown import MyTest
str_time = datetime.now().strftime('%Y%m%d')  # 获取当前时间

class libraryquantification(MyTest):
    """文库定量模块测试用例"""

    def setUp(self) -> None:
        """初始化浏览器驱动"""
        self.wkdl = libraryquantificationPage(self.driver)

    def test01_enter_testPage(self):
        """测试进入文库定量任务列表"""
        self.initialize()
        log.info('登录系统，进入文库定量页面')
        EnterTab.enter_test_center(self.basepage)
        EnterTab.enter_libraryquantification(self.basepage)  # 点击文库定量导航树

    def test02_add_wkdl_task(self):
        """测试新建文库定量任务单，在待选表选择sop,检索lims号，添加样本、保存任务单"""
        info = self.wkdl.add_task()  # 新建任务单，选择任务类型、sop
        if info:
            self.assertEqual(info, "任务单保存成功", "保存样本到明细表失败！！")

    def test03_wkdl_enter_result_list(self):
        """测试待选表进入文库定量明细表"""
        log.info("待选表进入文库定量明细表")
        self.wkdl.enter_result_list()  # 保存任务单，进入明细表()
        self.assertIsNotNone(re.search(r'返回待选表', self.wkdl.get_source))

    def test04_wkdl_edit_quantifying_mix_product_name(self):
        """测试文库定量明细表编辑定量混合产物名称"""
        log.info("库定量明细表编辑定量混合产物名称")
        self.wkdl.edit_quantifying_mix_product_name()

    def test05_create_reselt(self):
        """定量明细表生成结果"""
        log.info("定量明细表生成结果")
        info=self.wkdl.create_reselt()
        self.assertEqual('结果生成成功', info, "结果生成成功！")

    def test06_wkdl_enter_result(self):
        """测试文库定量进入结果表"""
        log.info("文库定量进入结果表")
        self.wkdl.enter_result()
        self.assertIsNotNone(re.search(r'返回明细表', self.wkdl.get_source))

    def test07_result_product_type(self):
        """文库定量结果表录入产物体积、产物浓度、总量"""
        log.info("文库定量结果表录入产物体积、产物浓度、总量")
        self.wkdl.result_edit_form_data()

    def test08_wkdl_result_save_result(self):
        """测试文库定量结果表保存页面数据操作"""
        log.info("文库定量结果表保存页面数据操作")
        self.wkdl.save_result()

    def test09_wkdl_result_submit_sample(self):
        """测试文库定量结果表提交"""
        log.info("文库定量结果表提交")
        info=self.wkdl.result_submit_sample()
        self.assertEqual('是', info, "结果表提交失败！")

    def test10_wkdl_result_enter_detail(self):
        """测试文库定量结果表返回明细表"""
        log.info("wkdl结果表，自动计算")
        self.wkdl.write_data_to_excel()
        self.wkdl.enter_detail()
        self.assertIsNotNone(re.search(r'返回待选表', self.wkdl.get_source))

    def test11_detail_submit(self):
        """测试文库定量明细表提交操作"""
        self.wkdl.detail_submit()  # 明细表提交操作

    def test12_detail_into_storage(self):
        """测试文库定量明细表入库操作"""
        self.wkdl.detail_into_storage()  # 明细表样本入库操作

    def test13_complete_task(self):
        """测试文库定量结果表，完成任务单"""
        self.wkdl.enter_result()
        save_info3 = self.wkdl.complete_task()
        self.assertEqual(save_info3.strip(), '完成', '完成任务单失败！')

    def test14_search_task_by_lims(self):
        """测试根据添加到的任务单中的lims样本号搜索对应的任务单"""
        EnterTab.enter_test_center(self.basepage)
        EnterTab.enter_libraryquantification(self.basepage)  # 点击wkdl导航树
        log.info(" 测试根据添加到的任务单中的lims样本号搜索对应的任务单")
        samples = self.wkdl.serach_task()  # 根据lims号搜索任务单号
        self.assertNotEqual(samples, 0, "查询结果错误，查询失败！")


if __name__ == '__main__':
    unittest.main()
