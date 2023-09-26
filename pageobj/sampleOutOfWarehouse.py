# -*- coding: utf-8 -*-
# @Time    : 2022/09/09
# @Author  : guanzhou.zhou
# QPCR样本出库的一些列操作
from PageElements.QPCR_ck_ele import *
from uitestframework.basepageTools import BasePage
from common.logs import log


class GetSampleCK(BasePage):
    """
    以下是针对QPCR样本出库的一些列操作
    """

    def add_qpcrSample_ck(self):
        """
        QPCR样本出库
        """
        # 点击新建QPCR出库按钮,录入核酸提取节点的入库样本，进行出库

        log.info("点击新建QPCR出库按钮")
        self.clicks('css', add_qpcr)
        log.info("选择出库样本号，录入出库样本lims号")

    def search_sample(self, lims_nub):
        """
        录入出库样本号
        :param lims_nub:QPCR样本号
        :return:
        """
        self.input('css', qpcr_sample_input, lims_nub)
        print('样本号是：', lims_nub)
        self.sleep(0.5)
        self.clicks('css', qpcr_sample_input_confirm)
        self.wait_loading()

    def process_error_sample(self):
        """
        处理错误的样本号
        """
        self.clicks('css', error_sample_confirm)
        self.clicks('css', cannel_btn)

    def qpcr_check_bacteria(self):
        """
        qpcr出库样本选择菌种
        """
        log.info("为QPCR样本选择QPCR检测菌种")
        self.sleep(1)
        self.clicks('css', get_table)
        self.sleep(0.5)
        self.clicks('css', qpcr_all_chioce)
        self.sleep(0.5)
        self.clicks('css', qpcr_check_bacteria_btn)  # QPCR检测菌种选择按钮
        # 选择两个菌种
        for i in range(1, 3):
            self.clicks('css', choice_bacteria.format(i))
            self.sleep(0.5)
        self.clicks('xpath', choice_bacteria_confirm)  # 选择菌种确认
        self.sleep(0.5)
        self.clicks('css', save_and_last)  # 选择菌种后，保存全部，下一步按钮
        self.wait_loading()

    def qpcr_sample_ck_reason(self):
        log.info("为QPCR样本出库填写出库理由")
        self.input('css', qpcr_out_reason, '自动化测试QPCR出库')  # qpcr填写出库理由
        self.clicks('css', qpcr_out_reason_confirm)  # 填写出库理由确认按钮
        self.wait_loading()

    def switch_to_window_handle(self):
        """
        出库后跳转到流转表页面，切换到流转表页面并关闭出库页面
        """
        # 获取当前窗口句柄
        now_handle = self.get_current_window_handle()
        print('获取当前窗口句柄', now_handle)

        # 获取所有窗口句柄
        all_handles = self.get_all_windows()
        for handle in all_handles:
            if handle != now_handle:
                self.close()
                # 切换到旧窗口句柄，回到原页面
                self.switch_to_window(handle)
                self.wait_loading()
        self.sleep(0.5)

    def close_page_info(self):
        """
        关闭流转表出库节点样本配置提示
        """
        self.clicks('css', sample_info_confirm)
