# -*- coding: utf-8 -*-
# @Time    : 2021/11/11
# @Author  : guanzhong.zhou
# @File    : 款项核对页面功能封装
from common.editYaml import get_order
from common.screenshot import Screenshot
from PageElements.paymentcheck_ele import *
from uitestframework.basepageTools import BasePage
from common.logs import log


class PaycheckPage(BasePage):
    """款项核对页面基础方法类"""

    def search_order(self):
        """查询方法"""
        log.info('批量修改订单确认状态...')
        log.info('点击搜索框，录入订单号...')
        self.sleep(3)
        self.clicks('css', orderId)
        self.sleep(0.5)

        order = get_order()
        log.info('录入订单号...%s:' % order)
        self.input('css', order_number, order)
        self.sleep(0.5)
        self.clicks('css', order_search_comfirm_btn)
        self.wait_loading()

        # 调用自定义截图方法
        Screenshot(self.driver).get_img("款项核对订单号搜索框录入订单号，点击搜索按钮","检索出正确的订单信息")

        log.info('根据录入的订单号筛选订单')
        self.clicks('css', screen_button)
        self.wait_loading()
        log.info('选中筛选结果，设置确认信息为：已确认')
        self.sleep(1)

        self.clicks('css', body_list)  # 选择第一条
        self.sleep(1)

        self.moved_to_element('css', statue_button)  # 移动鼠标到确认状态选择按钮
        self.sleep(1)
        self.clicks('xpath', chioce_status_button)
        self.sleep(1)
        log.info('保存设置后的结果')
        self.clicks('css', save_button)
        self.sleep(1)

    def get_save_info(self):
        """获取保存提示信息"""
        if self.isElementExists('xpath', save_success_info):
            return self.get_text('xpath', save_success_info)
        else:
            pass
