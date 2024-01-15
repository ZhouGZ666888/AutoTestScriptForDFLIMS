# -*- coding: utf-8 -*-
# @Time    : 2024/01/11
# @Author  : guanzhong.zhou
# @File    : 文库定量模块页面功能封装
import re
from datetime import datetime
import pyperclip
import xlrd
from selenium.webdriver.common.keys import Keys
from common.screenshot import Screenshot
from common.DataBaseConnection import executeSql
from conf.all_path import position_in_box_path, wkdl_file_path
from conf.config import libquant_result
from common.xlsx_excel import read_excel_col, get_lims_for_excel_by_col, pandas_write_excel
from PageElements.wkdl_ele import *
from conf.execute_sql_action import wkdl_detail_update, dl_next_step, dl_detail_lims_sql
from uitestframework.basepageTools import BasePage
from common.logs import log


class libraryquantificationPage(BasePage):
    """文库定量页面方法封装"""

    # 新增任务单
    def add_task(self):
        """新建文库定量任务单"""
        log.info("文库定量首页，点击新建按钮，进入样本待选表，新增文库定量任务")
        self.clicks('css', add_sample_task)
        self.wait_loading()

        log.info("选择sop")
        self.clicks('css', task_sop)
        self.sleep(0.5)
        self.clicks('css', task_sop_choice)
        self.wait_loading()
        return self.check_lims_num()

    # 待选表校验lims号
    def check_lims_num(self):
        """核对lims号功能，并保存任务单号"""
        # excel中获取待选样本
        sample_nub = get_lims_for_excel_by_col(wkdl_file_path)
        log.info('获取接样流程中的lims样本号,核对lims号是否存在')
        try:
            self.clicks('css', check_lims_sample_num)
            self.sleep(0.5)
            self.input('xpath', check_lims_sample_number_textarea, sample_nub)
            self.sleep(0.5)
            self.clicks('css', check_lims_sample_number_confirm)
            self.wait_loading()
        except Exception as error:
            log.error('文库定量核对样本号信息有误:%s' % error)
        self.sleep(0.5)

        log.info('选中核对后的样本，点击【加入选中样本&保存】')
        self.click_by_js('css', all_choice)
        self.sleep(0.5)
        self.clicks('css', addSelect_or_save_btn)

        # 调用自定义截图方法
        Screenshot(self.driver).get_img("文库定量待选表点击核对lims号，录入样本号进行查询，勾选查询结果，并保存任务单号", "保存任务单成功")

        pageinfo = self.get_pageinfo()
        self.wait_loading()
        if pageinfo:
            return pageinfo

    # 待选表进入明细表
    def enter_result_list(self):
        """待选表进入明细表"""
        log.info('从定量待选表进入文库定量明细表')
        self.clicks('css', enter_detail_list_btn)
        self.wait_loading()
        Screenshot(self.driver).get_img("进入定量明细表界面", "明细表页面展示正常")

    def set_form_data(self):
        """通过数据库写入表单数据"""
        taskstatus = self.get_text('css', detail_task_id)  # 获取任务单号
        print('富集任务单号', taskstatus)
        executeSql.test_updateByParam(wkdl_detail_update.format(taskstatus[5:].strip()))
        self.sleep(0.5)
        self.refresh()

    # 明细表编辑定量混合产物名称
    def edit_quantifying_mix_product_name(self):
        """明细表编辑定量混合产物名称"""
        self.set_form_data()  # 数据库写入表单数据
        str_time = datetime.now().strftime('%Y%m%d')  # 获取当前时间
        fjwkmc = 'NJ-' + str_time + '-101-A-1@1'  # 编辑定量混合产物名称
        log.info('定量明细表录入定量混合产物名称')
        totalSample = self.findelements('css', detail_all_samples)
        for i in range(1, len(totalSample) + 1):
            self.clicks('css', quantifying_mix_product_name.format(i))
            self.sleep(0.2)
            self.input('css', quantifying_mix_product_name_input.format(i), fjwkmc)
            self.sleep(0.5)
        self.sleep(0.5)

    def create_reselt(self):
        """定量明细表生成结果"""
        log.info('定量明细表生成结果')
        self.clicks('xpath', create_result)
        self.wait_loading()
        self.clicks('css', create_result_tips)
        info = self.get_pageinfo()
        self.wait_loading()
        Screenshot(self.driver).get_img("定量明细表生成结果", "明细表生成结果成功")
        return info

    # 进入结果表
    def enter_result(self):
        """进入结果表"""
        self.clicks('css', go_result)
        self.wait_loading()
        Screenshot(self.driver).get_img("进入定量结果表", "进入定量结果表，数据展示正常")

    # 返回明细表
    def enter_detail(self):
        """返回明细表"""
        self.clicks('css', go_back)
        self.sleep(0.5)
        self.clicks('css', go_back_confirm)
        self.wait_loading()

    # 明细表提交
    def detail_submit(self):
        """明细表样本提交操作"""
        log.info('文库定量明细表，点击提交')
        self.clicks('css', detail_all_choice)  # 全选样本
        self.sleep(0.5)
        self.click_by_js('css', sumbit_btn)  # 提交按钮
        self.sleep(0.5)
        # 调用自定义截图方法
        Screenshot(self.driver).get_img("文库定量明细表点击提交按钮", "弹出提交确认按钮")
        self.clicks('css', submit_comfirm)  # 提交弹框确认按钮
        self.wait_loading()

    # 明细表入库
    def detail_into_storage(self):
        """明细表样本入库操作"""
        log.info('文库定量明细表，样本入库操作')
        self.clicks('css', deposit_into_storage)  # 入库按钮
        self.sleep(0.5)
        self.clicks('css', storage_all_choice)  # 入库弹框全选按钮
        self.sleep(0.5)

        log.info('文库定量明细表，样本入库选择入样本盒')
        self.clicks('css', batch_paste_sample_box)  # 入库弹框选择样本盒按钮
        self.wait_loading()
        self.input('css', target_storage, '自动化测试用(勿删)')
        self.sleep(0.5)
        self.clicks('css', select_sample_box_search)
        self.wait_loading()
        self.clicks('css', select_sample_box_choice)  # 入库弹框选选择样本盒值，默认选择列表第一条数据
        self.sleep(0.5)
        self.clicks('xpath', select_sample_box_comfirm)  # 入库弹框选选择样本盒弹框，确认按钮
        self.sleep(0.5)

        log.info('文库定量明细表，样本入库批量粘贴盒内位置')
        lims_list = self.position_index(detail_task_id, dl_detail_lims_sql)
        data = xlrd.open_workbook(position_in_box_path)
        num_list = []
        for B in range(0, len(lims_list)):
            tables = data.sheets()[0]
            vals = tables.row_values(B)
            imp_data = '\t'.join(map(str, vals))
            num_list.append(imp_data)
        print("\n".join(map(str, num_list)))
        pyperclip.copy("\n".join(map(str, num_list)))

        # 粘贴到【批量粘贴盒内位置】文本框
        self.click_by_js('css', batch_copy_BoxPosition)
        self.findelement('xpath', batch_copy_BoxPosition_input).send_keys(Keys.CONTROL, 'v')
        self.sleep(1)
        self.clicks('xpath', batch_copy_BoxPosition_comfirm)
        self.sleep(0.5)

        # 调用自定义截图方法
        Screenshot(self.driver).get_img("文库定量明细表点击入库按钮，在弹框中录入库位信息和盒内位置后点击下一步", "样本入库成功")

        self.clicks('xpath', storage_next)
        self.wait_loading()

    # 获取样本号，生成对应的盒内位置写入到文件
    def position_index(self, task_id, sql):
        """获取样本号，生成对应的盒内位置写入到文件"""
        taskid = self.get_text('css', task_id)  # 获取任务单号
        lims_id = executeSql.test_select_limsdb(sql.format(re.findall(r'[a-zA-Z0-9]+', taskid)[0]))  #
        # 从数据库获取当前任务单号下样本lims号
        lims_list = [item[key] for item in lims_id for key in item]  # 把获取的lims号转换为一维列表
        nub_list = [str(i) for i in range(1, len(lims_list) + 1)]  # 根据lims样本数量，生成数字列表，作为盒内位置编号用
        res = [list(i) for i in zip(lims_list, nub_list)]  # 将lims号和数字编号转换为二维列表格式，写入Excel
        print(res)
        pandas_write_excel(res, position_in_box_path)
        return lims_list

    # 结果表录入表单数值
    def result_edit_form_data(self):
        """文库定量结果表录入产物体积、产物浓度、总量"""
        log.info('文库定量结果表，录入产物体积、产物浓度、总量')
        # 根据总样本数，循环录入产物体积、浓度、总量
        result_total_samples = self.findelements('css', result_all_samples)
        for i in range(1, len(result_total_samples) + 1):
            # 录入产物体积
            self.clicks('css', quantifying_mix_product_vol.format(i))
            self.input('css', quantifying_mix_product_vol_input.format(i), 5)
            self.sleep(0.4)
            # 录入产物浓度
            self.clicks('css', quantifying_mix_product_consistenceAmt.format(i))
            self.input('css', quantifying_mix_product_consistenceAmt_input.format(i), 5)
            self.sleep(0.4)
            # 录入产物总量
            self.clicks('css', quantifying_mix_product_total.format(i))
            self.input('css', quantifying_mix_product_total_input.format(i), 25)
            self.sleep(0.4)

    # 结果表保存
    def save_result(self):
        log.info("文库定量结果表保存页面数据操作")
        self.clicks('css', result_save_btn)
        self.wait_loading()

    # 结果表提交
    def result_submit_sample(self):
        """结果表提交"""
        log.info(' 文库定量结果表,点击提交')
        self.clicks('css', result_sumbit_btn)  # 提交按钮
        self.wait_loading()
        # 调用自定义截图方法
        Screenshot(self.driver).get_img("文库定量结果表点击提交按钮", "弹出提交确认按钮")
        self.clicks('css', result_submit_comfirm)  # 提交确认按钮
        self.wait_loading()

        submit_info = self.get_text('css', result_sample_status)
        print('样本处理结果表提交状态', submit_info)  #
        return submit_info.strip()

    # 结果表样本流程环节写入Excel
    def write_data_to_excel(self):
        """根据结果表样本下一步流程，把对应的样本lims号、实验室号、下一步流程以追加形式写入该流程的Excel"""
        self.add_excel_xlxs(dl_next_step, libquant_result, result_task_id)
        print('下一步流程写入成功')

    # 完成任务单
    def complete_task(self):
        """完成任务单"""

        log.info('文库定量结果表,点击完成任务单')
        self.click_by_js('css', result_complete_task_btn)
        self.wait_loading()

        # 调用自定义截图方法：任务单已完成
        Screenshot(self.driver).get_img("文库定量结果表点击完成任务单按钮", "完成任务单成功，状态改为完成")
        taskstatus = self.get_text('css', result_task_status)
        return taskstatus

    # 获取页面提示信息
    def get_pageinfo(self):
        """
        获取页面操作提示信息
        Task list saved successfully---保存样本到任务单成功
        Submit successfully---提交成功
        sample in storage successfully---入库成功
        """
        if self.isElementExists('xpath', page_success_info):
            return self.get_text('xpath', page_success_info)
        else:
            return None

    # 任务列表查询样本所在任务单
    def serach_task(self):
        """
        首页面查询已完成的样本任务单
        """
        lims_id = read_excel_col(wkdl_file_path, 'lims号')
        self.input('css', search_lims_sample_num, lims_id[0])
        self.sleep(1)
        self.clicks('css', search_btn)
        if self.isElementExists('class_name', 'el-icon-loading'):
            self.wait_loading()
        self.sleep(1)
        samples = self.findelements('css', sample_page_list)
        return len(samples)
