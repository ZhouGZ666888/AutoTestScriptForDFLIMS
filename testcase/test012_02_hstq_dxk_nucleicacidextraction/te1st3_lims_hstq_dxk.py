import unittest
from PageElements.hstq_ele import *
from conf.all_path import hstq_file_path_dxk
from pageobj.nucleicAcidExtractionPage import NucleicAcidExtractionPage
from conf.enter_tab import EnterTab
from common.logs import log
from common.setup_teardown import MyTest


class NucleicAcidExtractionDxk(MyTest):
    """核酸提取模块迪讯康样本测试用例"""

    def setUp(self) -> None:
        """初始化浏览器驱动"""
        self.hstq = NucleicAcidExtractionPage(self.driver)

    def test01_add_extraction_task(self):
        """测试新建核酸提取任务单，在待选表选择任务类型、sop,检索lims号，添加、保存任务单"""
        log.info('登录系统，进入核酸提取页面')
        self.initialize()
        EnterTab.enter_test_center(self.basepage)
        EnterTab.enter_extraction(self.basepage)  # 点击核酸提取导航树

        self.hstq.add_task()  # 新建任务单，选择任务类型、sop
        info = self.hstq.check_lims_num(hstq_file_path_dxk)  # 核对lims，添加至任务单
        self.hstq.enter_result_list(enter_detail_list_btn, '核酸提取明细表')  # 保存任务单，进入明细表
        if info is not None:
            self.assertEqual(info, "任务单保存成功", "保存样本到明细表失败！！")
        else:
            print('页面提示没获取到')

    def test02_extraction_detail(self):
        """测试核酸提取明细表样本批量数据录入、自动计算、提交、入库功能"""
        self.hstq.add_NTC_type(ntc_dxk)  # 添加迪讯康对照
        self.hstq.extraction_detail()  # 核酸提取明细表数据录入、自动计算操作
        self.hstq.enter_result_list(goResult, '核酸提取结果表')  # 进入核酸提取结果表

    def test03_extraction_result(self):
        """测试核酸提取结果表修改产物类型、批量数据录入、表单数据录入，提交"""
        self.hstq.extraction_result_data_input()  # 结果表产物类型、批量数录入
        self.hstq.extraction_result_formdata_input()  # 结果表表单数据录入
        pageinfo1 = self.hstq.result_submit_sample()  # 结果表提交
        self.hstq.write_data_to_excel()  # 结果表下一步数据写入对应Excel
        self.assertEqual(pageinfo1, '是', '提交失败!')

    def test04_detail_submit(self):
        """返回明细表提交、入库,完成任务单"""
        self.hstq.detail_submit()  # 明细表提交操作
        pageinfo = self.hstq.detail_into_storage()  # 明细表样本入库操作
        pageinfo3 = self.hstq.complete_task()
        if pageinfo is not None:
            self.assertEqual(pageinfo, "完成", '入库失败')
        else:
            print('页面提示没获取到')
        self.assertEqual(pageinfo, '完成', "入库失败，请检查数据！！！")
        self.assertEqual(pageinfo3[6:].strip(), '完成', '完成任务单失败！')

    def test05_search_task_by_lims(self):
        """测试根据添加到的任务单中的lims样本号搜索对应的任务单"""
        EnterTab.enter_test_center(self.basepage)
        EnterTab.enter_extraction(self.basepage)
        samples = self.hstq.serach_task(hstq_file_path_dxk)  # 根据lims号搜索任务单号
        self.assertNotEqual(samples, 0, "查询结果错误，查询失败！")


if __name__ == '__main__':
    unittest.main()
