# -*- coding: utf-8 -*-
# @Time    : 2022/08/25
# @Author  : guanzhong.zhou
# @File    : 文库构建模块测试用例

import unittest
from PageElements.wkgj_ele import *
from pageobj.libconstructionPage import LibconstructionPage
from conf.enter_tab import EnterTab
from common.logs import log
from common.setup_teardown import MyTest


class Libconstruction(MyTest):
    """文库构建模块测试用例"""

    def setUp(self) -> None:
        """初始化浏览器驱动"""
        self.wkgj = LibconstructionPage(self.driver)

    def test01_add_libconstruction_task(self):
        """测试新建文库构建任务单，在待选表选择任务类型、sop,检索lims号，添加、保存任务单"""
        self.initialize()
        log.info('登录系统，进入文库构建页面')
        EnterTab.enter_test_center(self.basepage)
        EnterTab.enter_libconstruction(self.basepage)  # 点击文库构建导航树

        self.wkgj.add_task()  # 新建任务单，选择任务类型、操作类型、sop
        log.info('核对lims，添加至任务单')
        info = self.wkgj.check_lims_num()  # 核对lims，添加至任务单
        log.info('保存任务单，进入明细表')
        self.wkgj.enter_result_list(enter_detail_list_btn, '文库构建明细表')  # 保存任务单，进入明细表
        if info is not None:
            self.assertEqual(info, "任务单保存成功", "保存样本到明细表失败！！")
        else:
            pass

    def test02_libconstruction_detail(self):
        """测试文库构建明细表批量数量录入、入库信息、批量包装余量、录入96孔版位置"""
        log.info(" 文库构建明细表，选择入库信息、批量包装余量、录入96孔版位置")
        self.wkgj.detail_libconstruction()
        log.info("文库构建明细表选，进行自动计算")
        self.wkgj.detail_libconstruction_form_input()
        log.info('进入文库构建结果表')
        self.wkgj.enter_result_list(enter_result_list_btn, '文库构建结果表')  # 进入文库构建结果表

    def test03_libconstruction_result(self):
        """测试文库构建结果表批量数量录入、表单数据录入、修改产物类型、自动计算、录入预计富集时间"""
        log.info("文库构建结果表，修改产物类型、批量数据")
        self.wkgj.ultrasonic_result_data_input()

        log.info("文库构建结果表，修改预计富集时间")
        self.wkgj.edit_estimated_enrichment_time()

        log.info("文库构建结果表，结果表表单录入,生成盒内位置")
        self.wkgj.ultrasonic_result_formdata_input()

        log.info("文库构建结果表，结果表提交")
        self.wkgj.result_submit_sample()

        log.info("文库构建结果表，结果表下一步数据写入对应Excel")
        self.wkgj.write_data_to_excel()
        log.info("文库构建结果表，返回明细表完成提交入库操作")
        self.wkgj.goback_detail()

    def test04_detail_submit(self):
        """返回明细表提交、入库"""
        self.wkgj.detail_sumbit()  # 明细表提交操作
        page_info = self.wkgj.detail_into_storage()  # 明细表样本入库操作
        self.assertEqual(page_info, '完成', "入库失败，请检查数据！！！")

    def test05_complete_task(self):
        """完成任务单"""
        save_info3 = self.wkgj.complete_task()
        self.assertEqual(save_info3[6:].strip(), '完成', '完成任务单失败！')

    def test05_search_task_by_lims(self):
        """测试根据添加到的任务单中的lims样本号搜索对应的任务单"""
        EnterTab.enter_test_center(self.basepage)
        EnterTab.enter_libconstruction(self.basepage)  # 点击文库构建导航树

        log.info(" 测试根据添加到的任务单中的lims样本号搜索对应的任务单")
        samples = self.wkgj.serach_task()  # 根据lims号搜索任务单号
        self.assertNotEqual(samples, 0, "查询结果错误，查询失败！")


if __name__ == '__main__':
    unittest.main()
