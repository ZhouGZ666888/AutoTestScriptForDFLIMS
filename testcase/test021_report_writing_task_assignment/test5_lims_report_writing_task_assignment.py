import unittest
from pageobj.report_bgbxrwfpPage import ReportWritingTaskAssignmentPage
from conf.enter_tab import EnterTab
from common.logs import log
from common.setup_teardown import MyTest


class ReportWritingTaskAssignment(MyTest):
    def setUp(self) -> None:
        """
        初始化浏览器驱动
        """
        self.rwfb = ReportWritingTaskAssignmentPage(self.driver)

    def test01_serach_info(self):
        """
        测试报告编写任务分配模块，分别根据订单号、项目号、预计实验日期搜索待处理任务
        """
        log.info('登录系统，进入报告编写任务分配页面')
        self.initialize()
        # 传入驱动
        EnterTab.enter_report_center(self.basepage)
        EnterTab.report_writing_task_assignment(self.basepage)  # 点击报告上传导航树
        log.info('按项目号搜索')
        result1 = self.rwfb.search_by_project()
        log.info('按预计实验日期查询')
        result2 = self.rwfb.search_by_date()
        log.info('按订单号搜索')
        result3 = self.rwfb.search_by_order()
        self.assertNotEqual(result1, 0, "按项目号查询无结果！！！")
        self.assertNotEqual(result2, 0, "按预计实验日期查询无结果！！！")
        self.assertNotEqual(result3, 0, "按订单号查询无结果！！！")

    def test02_edit_sample_info(self):
        """
        测试对筛选出的报告任务批量选择编写人、审核人
        """
        self.rwfb.search_by_order()
        log.info('选择编写人')
        pageinfo1 = self.rwfb.select_writer_bulk()
        log.info('选择审核人')
        pageinfo2 = self.rwfb.batch_selection_examiner()
        self.assertEqual(pageinfo1, '选择编写人成功', "选择编写人功能失败！！！")
        self.assertEqual(pageinfo2, '选择审核人成功', "选择编写人功能失败！！！")


if __name__ == '__main__':
    unittest.main()
