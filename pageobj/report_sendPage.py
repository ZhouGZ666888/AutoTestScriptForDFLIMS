# -*- coding: utf-8 -*-
# @Time    : 2022/09/27
# @Author  : guanzhong.zhou
# @File    : 报告发送模块页面方法封装

from datetime import datetime
from common.editYaml import get_order
from common.screenshot import Screenshot
from PageElements.report_send_ele import *
from uitestframework.basepageTools import BasePage
from common.logs import log


class ReportSendPage(BasePage):
    """报告-基本信息任务分配模块页面基础方法封装"""

    def search_by_date(self):
        """
        根据预计实验日期查询
        :return: 返回查询结果数量
        """
        log.info("根据预计实验日期查询")
        self.input('css', reportSend_form_completeDate, datetime.now().strftime('%Y.%m.%d'))
        self.sleep(0.5)
        self.click_by_js('css', search_btn)  # 点击查询
        self.wait_loading()

        res = self.isElementExists('xpath', search_result)
        if res:
            allorder = self.findelements('xpath', search_result)  # 获取查询结果数量
            allorder_len = len(allorder)
        else:
            allorder_len = 0
        self.clicks('css', reset_btn)  # 重置查询条件
        return allorder_len

    def search_by_order(self):
        """
        按订单号搜索
        :return:返回查询出的订单信息数量
        """
        order = get_order()  # 订单Excel获取订单号
        log.info("按订单号搜索{}".format(order))
        self.clicks('css', order_num)
        self.sleep(0.5)
        self.input('css', order_num_input, order)
        self.clicks('css', order_num_input_confirm)
        self.click_by_js('css', search_btn)  # 点击查询
        self.wait_loading()
        res = self.isElementExists('xpath', search_result)
        if res:
            allorder = self.findelements('xpath', search_result)  # 获取查询结果数量
            allorder_len = len(allorder)
        else:
            allorder_len = 0
        return allorder_len

    def edit_report_status(self):
        """
        修改报告审核状态
        """
        log.info("修改报告审核状态")
        self.search_by_order()
        self.click_by_js('xpath', audit_status)  # 点击表单审核状态表单
        self.sleep(0.5)
        self.click_by_js('xpath', audit_status_select)  # 点击表单审核状态下拉
        # 这里调用自定义截图方法
        Screenshot(self.driver).get_img("报告发送模块，选中报告，点击状态下拉框，选择已发送","修改报告状态成功")

        self.clicks('xpath', audit_status_choice)  # 表单审核状态选择---已审核

    def save(self):
        """
        保存信息
        :return:返回页面提示信息
        """
        log.info("保存信息")
        self.clicks('css', save_btn)
        pageinfo = self.get_save_info()
        log.info("获取保存信息的页面提示：{}".format(pageinfo))
        return pageinfo

    def get_save_info(self):
        """
        获取数据操作后，页面给出的提示信息语
        Submit successfully
        review successfully
        """
        log.info('获取页面提示信息')
        return self.get_text('xpath', page_info)
