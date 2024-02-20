import unittest
from common.setup_teardown import MyTest
from conf.enter_tab import EnterTab
from common.logs import log
from pageobj.sampleRecPage import SampleReceivePage


class SampleReceive(MyTest):
    """
    样本处理模块测试用例
    """

    def setUp(self) -> None:
        self.src = SampleReceivePage(self.driver)

    def test01_set_order_receive_info(self):
        """
        测试新增接样样本设置接样-订单信息，选择所属项目、检测产品
        """
        self.initialize()
        log.info('登录系统，进入样本接收页面')
        EnterTab.enter_samplereceive(self.basepage)
        log.info("搜索订单号")
        self.src.search_order()
        log.info("添加样本的项目信息类型")
        self.src.add_order_project()

    def test02_add_samples(self):
        """测试添加样本、设置样本的报告类型"""
        log.info("添加样本")
        self.src.sampleRec_addSample()
        log.info("样本选择样本报告类型和样本类型")
        self.src.add_sampleReportType()

    def test03_set_sample_type(self):
        """测试选择样本类型"""
        log.info('选择样本类型')
        self.src.set_sampleType()

    def test04_set_laboratory_process(self):
        """测试按照报告类型的不同，设置样本实验流程"""
        log.info("为样本选择实验流程")
        self.src.generate_laboratory_process()

    def test05_inputsampleinfo(self):
        """
        测试录入样本包装量和样本计量等填充信息
        """
        log.info("录入样本计量、选择质检结果、接样备注")
        self.src.input_sampleamt()
        log.info("把接样样本信息存入对应的Excel文件中")
        self.src.save_all_samples_excel()

    def test06_submission_for_review(self):
        """测试批量提交审核，切换审核用户"""
        log.info("批量提交审核")
        self.src.submit_sample_for_review()
        log.info("页面退出登录按钮，切换登录用户")
        self.src.batch_submit_for_review()

    def test07_batchreview(self):
        """
        对样本进行批量提交审核，切换用户进行完成审核功能测试
        """
        self.login_action('guanzhong.zhou')
        EnterTab.enter_samplereceive(self.basepage)
        self.src.search_order()
        self.src.batch_review()


if __name__ == '__main__':
    unittest.main()
