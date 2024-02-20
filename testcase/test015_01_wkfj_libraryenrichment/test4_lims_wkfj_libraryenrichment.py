# -*- coding: utf-8 -*-
# @Time    : 2022/08/25
# @Author  : guanzhou.zhou
# @File    : 无探针类型文库富集测试用例
import unittest
from PageElements.wkfj_ele import *
from conf.all_path import wkfj_file_path
from pageobj.libraryEnrichmentPage import LibraryenrichmentPage
from conf.enter_tab import EnterTab
from common.logs import log
from common.setup_teardown import MyTest


class LibraryenrichMent(MyTest):

    def setUp(self) -> None:
        """初始化浏览器驱动"""
        self.wkfj = LibraryenrichmentPage(self.driver)

    def test01_add_libraryenrichment_task(self):
        """测试无探针Pooling任务类型任务单，在待选表录入任务描述，选择任务sop,检索lims号，添加、保存任务单"""
        log.info('登录系统，进入文库富集页面')
        self.initialize()
        EnterTab.enter_test_center(self.basepage)
        EnterTab.enter_pooling(self.basepage)  # 点击文库富集导航树

        self.wkfj.add_task('无探针Pooling')  # 新建任务单，选择任务类型、操作类型、sop
        log.info('核对lims，添加至任务单')
        info = self.wkfj.get_non_probe_sample()  # 核对lims，添加至任务单
        log.info('保存任务单，进入明细表')
        self.wkfj.enter_result_list(enter_detail_list_btn, '文库富集明细表')  # 保存任务单，进入明细表
        self.assertEqual(info, "任务单保存成功", "保存样本到明细表失败！！")

    def test02_libraryenrichment_detail(self):
        """测试无探针Pooling任务类型任务单明细表批量批量粘贴导入实验数据、生成结果"""
        log.info("文库富集明细表批量粘贴导入实验数据")
        self.wkfj.detail_libraryenrichment('XX')
        log.info("批量数据后生成结果")
        res_info = self.wkfj.detail_create_result(14)
        log.info('进入文库富集结果表')
        self.wkfj.enter_result_list(enter_result_list_btn, '文库富集结果表')  # 进入文库富集结果表

        self.assertEqual(res_info, '是', '生成结果失败!')

    def test03_libraryenrichment_result(self):
        """测试无探针Pooling任务类型任务单结果表批量粘贴导入实验数据、生成上机分组号，提交，完成任务单"""
        log.info("文库富集结果表，批量数据录入")
        self.wkfj.ultrasonic_result_data_input()
        log.info(' 文库富集结果表提交操作')
        pageinfo1 = self.wkfj.result_submit_sample()
        log.info(' 文库富集结果表样本下一步流程写入Excel')
        self.wkfj.write_data_to_excel()
        log.info('返回富集明细表，提交并入库')
        self.wkfj.goback_detail()
        self.assertEqual(pageinfo1, '是', '提交失败!')

    def test04_detail_submit(self):
        """无探针Pooling任务类型任务单，明细表提交、入库,完成任务单"""
        log.info("文库富集明细表提交")
        self.wkfj.detail_submit()  # 明细表提交操作
        log.info("文库富集明细表入库")
        pageinfo = self.wkfj.detail_into_storage(15)  # 明细表样本入库操作
        log.info('返回富集结果表，完成任务单')
        save_info3 = self.wkfj.complete_task()
        self.assertEqual(pageinfo, '完成', "入库失败，请检查数据！！！")
        self.assertEqual(save_info3[6:].strip(), '完成', '完成任务单失败！')

    def test05_search_task_by_lims(self):
        """测试无探针Pooling任务类型任务单，根据添加到的任务单中的lims样本号搜索对应的任务单"""
        EnterTab.enter_test_center(self.basepage)
        EnterTab.enter_pooling(self.basepage)  # 点击文库富集导航树

        log.info(" 测试根据添加到的任务单中的lims样本号搜索对应的任务单")
        samples = self.wkfj.serach_task(wkfj_file_path)  # 根据lims号搜索任务单号
        self.assertNotEqual(samples, 0, "查询结果错误，查询失败！")


if __name__ == '__main__':
    unittest.main()
