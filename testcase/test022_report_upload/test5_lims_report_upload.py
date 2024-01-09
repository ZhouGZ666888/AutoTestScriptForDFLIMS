import unittest
from common.logs import log
from common.setup_teardown import MyTest
from conf.enter_tab import EnterTab
from pageobj.report_uploadPage import ReportUploadPage


class ReportUpload(MyTest):
    def setUp(self) -> None:

        """
        初始化浏览器驱动
        """
        self.repUpload = ReportUploadPage(self.driver)

    def test01_serach_info(self):
        """测试报告上传模块，分别根据订单号、项目号、预计实验日期搜索"""
        log.info('登录系统，进入报告发送页面')
        self.initialize()
        EnterTab.enter_report_center(self.basepage)
        EnterTab.enter_report_upload(self.basepage)  # 点击报告上传导航树

        log.info('根据订单号查询')
        result = self.repUpload.search_by_order()
        log.info('标记QPCR复检任务')
        self.repUpload.tip_report_qpcr_sample()

        if result is not None:
            self.assertNotEqual(result, 0, "按订单号查询无结果！！！")

    def test02_updata_report(self):
        """测试报告文件上传功能"""
        log.info('选择报告形式')
        self.repUpload.reportStyle()
        log.info('上传报告文件')
        report_info = self.repUpload.upload_report_file()
        if report_info:
            self.assertEqual(report_info, '上传成功', "上传报告文件失败！！！")

    def test03_upload_decode_file(self):
        """测试报告解读文件上传功能"""
        decode_info = self.repUpload.upload_decode_file()
        if decode_info:
            self.assertEqual(decode_info, '上传成功', "上传解读文件失败！！！")

    def test04_upload_other_file(self):
        """测试其他文件上传功能"""
        other_info = self.repUpload.upload_other_file()
        if other_info:
            self.assertEqual(other_info, '上传成功', "上传其他文件失败！！！")

    def test05_complete_report_task(self):
        """测试文件上传完成后，完成报告任务功能"""
        log.info('完成任务')
        complete_info = self.repUpload.complete_report_task()
        if complete_info:
            self.assertEqual(complete_info, '修改', "报告任务完成失败！！！")

    # def test06_create_qpcrReinspect_task(self):
    #     """测试新建QPCR复检任务"""
    #     log.info('新建QPCR复检任务')
    #     self.repUpload.create_qpcrReinspect_task()


if __name__ == '__main__':
    unittest.main()
