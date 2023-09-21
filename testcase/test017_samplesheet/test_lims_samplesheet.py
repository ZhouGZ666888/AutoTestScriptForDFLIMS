import unittest
from pageobj.samplesheet import SampleSheetPage
from conf.enter_tab import EnterTab
from common.logs import log
from common.setup_teardown import MyTest


class SampleSheet(MyTest):

    def setUp(self) -> None:
        """初始化浏览器驱动"""
        self.ss = SampleSheetPage(self.driver)

    def enterPage(self):
        self.initialize()
        EnterTab.enter_test_center(self.basepage)
        EnterTab.enter_samplesheet(self.basepage)  # 点击samplesheet导航树

    def test01_search_by_taskid(self):
        """测试通过上机任务单号搜索samplesheet"""
        log.info('登录系统，进入上机页面')
        self.enterPage()

        log.info('新建任务单，录入定量类型、任务描述、sop')
        self.ss.search_by_taskid()

    def test02_samplesheet_detail_download(self):
        """测试导出samplesheet文件"""
        self.ss.samplesheet_detail_download()

    def test03_samplesheet_detail_import(self):
        """测试导入samplesheet文件"""
        info = self.ss.samplesheet_detail_import()
        self.assertEqual('上传成功', info, '导入samplesheet文件失败')

    def test04_detail_save_generate_new_version(self):
        """测试samplesheet保存&生成新版本"""
        info = self.ss.detail_save_generate_new_version()
        self.assertEqual('已生成新版本，请重新确认可用', info, '生成新版本失败')

    def test05_detail_modify_record(self):
        """查看修改记录"""
        info = self.ss.detail_modify_record()
        self.assertNotEqual(info, 0, "修改记录无数据")


if __name__ == '__main__':
    unittest.main()
