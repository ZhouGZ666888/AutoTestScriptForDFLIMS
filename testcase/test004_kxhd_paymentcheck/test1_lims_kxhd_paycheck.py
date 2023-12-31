import unittest
from common.logs import log
from pageobj.paycheckPage import PaycheckPage
from conf.enter_tab import EnterTab
from common.setup_teardown import MyTest


class PaymentCheck(MyTest):
    """
      款项核对模块测试用例
      """

    def setUp(self) -> None:
        self.pc = PaycheckPage(self.driver)

    def test01_setpayment(self):
        """设置订款项状态：搜索订单并设置是否确认收款"""
        log.info('登录系统，进入款项核对页面')
        self.initialize()
        EnterTab.enter_crmorder(self.basepage)
        EnterTab.enter_payment(self.basepage)

        # 开始主程序，搜索订单，设置确认状态，保存
        self.pc.search_order()
        # 获取保存提示信息，做断言
        result = self.pc.findelement('xpath', '//*[text()="保存成功"]')
        self.assertIsNotNone(result)


if __name__ == '__main__':
    unittest.main()
