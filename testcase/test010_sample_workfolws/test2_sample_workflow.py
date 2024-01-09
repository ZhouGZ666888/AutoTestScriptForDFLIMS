import unittest
import datetime
from conf.enter_tab import EnterTab
from pageobj.sample_workflowPage import SampleWorkflowPage
from conf.execute_sql_action import *
from common.setup_teardown import MyTest


class SampleWorkflow(MyTest):

    def setUp(self) -> None:
        self.swf = SampleWorkflowPage(self.driver)

    def user_enter_order(self):
        """调用进入模块功能"""
        # 调用登录(单独调试case用，批量跑用例则需要注释)
        self.initialize()
        EnterTab.enter_workflow(self.basepage)  # 点击流转表的tab按钮
        EnterTab.enter_single_workflow(self.basepage)  # 点击单样本流转表按钮

    def test01_search_order(self):
        """测试在流转表搜索指定订单"""
        self.user_enter_order()  # 进入单样本流转表页面
        self.swf.workflow_search_order()

    def test02_search_sample(self):
        """测试在流转表搜索指定LIMS样本号(以提取待选表样本为例)"""
        self.swf.workflow_search_samplelimsid(lzb_get_sql1.format('extraction'))

    def test03_search_samplelab(self):
        """测试在流转表根据指定实验室第一部分号搜索"""
        self.swf.workflow_search_samplelab(lzb_get_sql1.format('extraction'))

    def test04_sample_fromdata(self):
        """测试在流转表搜索指定样本，分管操作，以在样本处理节点分管为例"""
        self.swf.workflow_fg(lzb_get_sql7.format('preparation'))

    def test05_sample_withdraw(self):
        """测试在流转表搜索指定数据，出库操作，以在样本接收节点为例"""
        self.swf.workflow_ck(lzb_get_sql3)

    def test06_update_pooling_data(self):
        """在流转表对数据，做修改【建库+富集】信息的操作"""
        self.swf.workflow_update_wkgj_wkfj( 'DNA建库', (datetime.datetime.now() + datetime.timedelta(days=2)).strftime('%Y.%m.%d'))


if __name__ == '__main__':
    unittest.main()
