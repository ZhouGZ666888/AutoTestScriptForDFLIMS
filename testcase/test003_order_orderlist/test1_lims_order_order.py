from common.logs import log
from common.screenshot import Screenshot
from pageobj.orderPage import OrderPage
from conf.enter_tab import EnterTab
from common.setup_teardown import MyTest
import unittest


class LimsOrder(MyTest):
    """订单模块测试用例"""

    def setUp(self) -> None:
        self.od = OrderPage(self.driver)

    def test01_add_order(self):
        """测试新建订单号"""
        log.info('登录系统，进入订单页面')
        self.initialize()
        EnterTab.enter_crmorder(self.basepage)
        EnterTab.enter_order(self.basepage)

        log.info("调用新增方法")
        self.od.add_order()

    def test02_search_order(self):
        """测试搜索订单号，进入订单详情"""
        log.info("搜索并进入订单编辑页面")
        self.od.enter_edit()

    def test03_edit_order_info(self):
        """测试编辑订单基本信息"""
        log.info("编辑订单信息,病历关联")
        self.od.edit_order()
        self.od.save_add_order()
        result = self.od.findelement('xpath', '//*[text()="保存成功"]')

        self.od.wait_loading()
        self.assertIsNotNone(result)


if __name__ == '__main__':
    unittest.main()
