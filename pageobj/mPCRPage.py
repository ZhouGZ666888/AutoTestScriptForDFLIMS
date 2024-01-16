# -*- coding: utf-8 -*-
# @Time    : 2023/05/22
# @Author  : guanzhong.zhou
# @File    : MPCR模块页面功能封装
import pyperclip, xlrd, re
from selenium.webdriver.common.keys import Keys
from common.screenshot import Screenshot
from common.DataBaseConnection import executeSql
from common.xlsx_excel import get_lims_for_excel_by_col, pandas_write_excel, read_excel_col, openpyxl_edit_data
from conf.all_path import position_in_box_path, mpcr_file_path, mpcr_result_consistence_amt_import_path
from conf.config import exp_mpcr_result_t
from PageElements.mpcr_ele import *
from conf.execute_sql_action import mpcr_96_well_plate, mpcr_detail_lims_sql, next_step_sql, mpcr_result_lims_sql
from uitestframework.basepageTools import BasePage
from common.logs import log


class mPCRTest(BasePage):
    """MPCR，待选表、明细表、结果表页面功能封装"""

    # 新增任务单
    def add_task(self):
        """新建MPCR任务单"""
        log.info("MPCR首页，点击新建按钮，进入样本待选表，新增MPCR任务")
        self.clicks('css', add_sample_MPCR_task)
        self.wait_loading()

        log.info("选择任务类型:结核耐药mPCR")
        self.click_by_js('css', task_type)
        self.clicks('xpath', task_type_choice)
        self.wait_loading()

        log.info("选择sop")
        self.clicks('css', task_sop)
        self.sleep(0.5)
        self.clicks('css', task_sop_choice)
        self.wait_loading()

        log.info("操作方式")
        self.clicks('css', action_type)
        self.sleep(0.5)
        self.clicks('xpath', operationType_choice)
        self.sleep(0.5)

    def enter_function_page(self, url):
        """进入指定url页面"""
        js = 'window.open("{}");'
        self.executeJscript(js.format(url))
        self.wait_loading()


    # 待选表校验lims号
    def check_lims_num(self):
        """核对lims号功能，并保存任务单号"""
        # excel中获取待选样本
        sample_nub = get_lims_for_excel_by_col(mpcr_file_path)
        log.info('获取接样流程中的lims样本号,核对lims号是否存在')
        try:
            self.clicks('css', check_lims_sample_num)
            self.sleep(0.5)
            self.input('xpath', check_lims_sample_number_textarea, sample_nub)
            self.sleep(0.5)
            self.clicks('css', check_lims_sample_number_confirm)
            self.wait_loading()
        except Exception as error:
            log.error('mpcr核对样本号信息有误:%s' % error)
        self.sleep(0.5)

        log.info('选中核对后的样本，点击【加入选中样本&保存】')
        self.click_by_js('css', all_choice)
        self.sleep(0.5)
        self.clicks('css', addSelect_or_save_btn)

        # 调用自定义截图方法
        Screenshot(self.driver).get_img("MPCR待选表点击核对lims号，录入样本号进行查询，勾选查询结果，并保存任务单号","保存任务单成功")

        pageinfo = self.get_pageinfo()
        self.wait_loading()
        if pageinfo:
            return pageinfo

    # 待选表进入明细表
    def enter_result_list(self):
        """待选表进入明细表"""
        self.clicks('css', enter_detail_list_btn)
        self.wait_loading()

    # 明细表自动计算
    def detail_auto_complete(self):
        """明细表自动计算"""
        self.clicks('css', detail_all_choice)
        self.sleep(0.5)
        self.clicks('css', detail_auto_complete)
        self.wait_loading()

    # 数据库写入样本的96孔板位置,之后保存
    def position_of_96_well_plate(self):
        """数据库写入样本的96孔板位置,之后保存"""
        mpcrLims = read_excel_col(mpcr_file_path, 'lims号')
        taskId = self.get_text('css', detail_task_id)
        for i in range(len(mpcrLims)):
            executeSql.test_updateByParam(
                mpcr_96_well_plate.format(i + 1, re.findall(r'[a-zA-Z0-9]+', taskId)[0], mpcrLims[i]))
        self.refresh()
        self.clicks('css', detail_save_btn)
        self.wait_loading()

    # 进入结果表
    def enter_result(self):
        """进入结果表"""
        self.clicks('css', go_result)
        self.wait_loading()

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
        log.info('MPCR明细表，点击提交')
        self.clicks('css', detail_all_choice)  # 全选样本
        self.sleep(0.5)
        self.click_by_js('css', sumbit_btn)  # 提交按钮
        self.sleep(0.5)
        # 调用自定义截图方法
        Screenshot(self.driver).get_img("MPCR明细表点击提交按钮","弹出提交确认按钮")
        self.clicks('css', submit_comfirm)  # 提交弹框确认按钮
        self.wait_loading()

    # 明细表入库
    def detail_into_storage(self):
        """明细表样本入库操作"""
        log.info('MPCR明细表，样本入库操作')
        self.clicks('css', deposit_into_storage)  # 入库按钮
        self.sleep(0.5)
        self.clicks('css', storage_all_choice)  # 入库弹框全选按钮
        self.sleep(0.5)

        log.info('MPCR明细表，样本入库选择入样本盒')
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

        log.info('MPCR明细表，样本入库批量粘贴盒内位置')

        lims_list = self.position_index(detail_task_id,mpcr_detail_lims_sql)

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
        Screenshot(self.driver).get_img("MPCR明细表点击入库按钮，在弹框中录入库位信息和盒内位置后点击下一步","样本入库成功")

        self.clicks('xpath', storage_next)
        self.wait_loading()

    # 获取样本号，生成对应的盒内位置写入到文件
    def position_index(self, task_id,sql):
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

    # 结果表修改产物类型
    def result_product_type(self):
        """
        MPCR结果表修改产物类型，批量数据录入
        """
        log.info('MPCR结果表，修改样本产物类型')

        self.clicks("css", product_type)  # 修改产物类型
        self.wait_loading()
        self.clicks("xpath", choice_product_type)  # 修改产物类型弹框数据选择，结核耐药mPCR产物
        self.clicks("xpath", choice_product_type_confirm)  # 修改产物类型弹框数据选择，确认
        self.wait_loading()
        if self.isElementExists('css', choice_product_type_tip):
            self.clicks('css', choice_product_type_tip)
            self.sleep(0.5)

    # 结果表修改NTC对照
    def result_edit_ntc(self):
        """结果表修改NTC对照"""
        self.clicks("css", result_all_choice)  # 样本列表数据全选按钮
        self.sleep(0.5)
        self.clicks('css', ntc_choice_btn)
        self.sleep(0.5)
        self.clicks('xpath', ntc_search)
        self.wait_loading()
        self.clicks('xpath', ntc_choice)
        self.clicks('xpath', ntc_choice_confirm_btn)
        self.wait_loading()

    # 结果表批量数据录入
    def result_batch_data(self):
        """结果表批量数据录入"""
        log.info('MPCR结果表，录入批量数据')
        self.clicks("css", result_batch_data)  # 批量数据按钮
        self.sleep(0.5)
        self.input("css", sampl_package_amount, 1)  # 批量数据弹框，mPCR产物包装量
        self.sleep(0.5)
        self.clicks("css", sampl_package_amount_unit)  # 批量数据弹框，包装单位下拉框
        self.sleep(0.5)
        self.clicks("xpath", sampl_package_amount_unit_choice)  # 批量数据弹框，包装单位下拉值（管 ）
        self.sleep(0.5)
        self.input("css", circular_labels_print, 1)  # 批量数据弹框，圆标签打印份数文本框
        self.sleep(0.5)
        self.input("css", long_labels_print, 1)  # 批量数据弹框，长标签打印份数文本框
        self.sleep(0.5)
        self.input('css', number_cycles, 5)  # 批量数据弹框，循环数
        self.clicks("css", volume_mPCR_product)  # 批量数据弹框，mPCR产物体积
        self.sleep(0.5)
        self.input('css',volume_mPCR_product,11)
        self.sleep(0.5)
        self.clicks('css', batch_data_confirm_btn)  # 保存录入批量数据
        self.sleep(0.5)

    # mpcr结果表批量导入产物浓度
    def result_import_mpcr_consistence_amt(self):
        """mpcr结果表批量导入产物浓度"""
        lims_list = self.position_index(result_task_id,mpcr_result_lims_sql)
        print('获取的样本lims号')
        openpyxl_edit_data(mpcr_result_consistence_amt_import_path, lims_list, 1)
        # 从模板中复制出修改后的待导入数据
        data = xlrd.open_workbook(mpcr_result_consistence_amt_import_path)

        num_list = []
        for index in range(0, len(lims_list)):
            tables = data.sheets()[0]
            vals = tables.row_values(index)
            imp_data = '\t'.join(map(str, vals))
            num_list.append(imp_data)
        print("\n".join(map(str, num_list)))
        pyperclip.copy("\n".join(map(str, num_list)))
        log.info("mpcr结果表批量粘贴导入产物浓度")
        self.clicks('css', import_mpcr_consistence_amt)  # 结果表批量粘贴导入按钮
        self.sleep(0.5)
        self.clicks('xpath', import_mpcr_consistence_amt_input)
        self.findelement('xpath', import_mpcr_consistence_amt_input).send_keys(Keys.CONTROL, 'v')
        self.sleep(0.5)
        self.clicks('xpath', import_mpcr_consistence_amt_confirm_btn)  # 结果表批量粘贴导入弹框确认按钮
        self.sleep(0.5)

    # mpcr结果表批量导入盒内位置
    def result_import_batch_paste_position(self):
        """mpcr结果表批量导入盒内位置"""
        # 把要导入的lims样本号写入盒内位置文件，并复制
        lims_list = self.position_index(result_task_id,mpcr_result_lims_sql)
        openpyxl_edit_data(position_in_box_path, lims_list, 1)
        # 从模板中复制出修改后的待导入数据
        data = xlrd.open_workbook(position_in_box_path)
        num_list = []
        for index in range(0, len(lims_list)):
            tables = data.sheets()[0]
            vals = tables.row_values(index)
            imp_data = '\t'.join(map(str, vals))
            num_list.append(imp_data)
        print("\n".join(map(str, num_list)))
        pyperclip.copy("\n".join(map(str, num_list)))
        log.info("mpcr结果表批量粘贴导入产物浓度")
        self.clicks('css', batch_paste_position)  # 结果表批量粘贴导入按钮
        self.sleep(0.5)
        self.clicks('xpath', batch_paste_position_input)
        self.findelement('xpath', batch_paste_position_input).send_keys(Keys.CONTROL, 'v')
        self.sleep(0.5)
        self.clicks('xpath', batch_paste_position_confirm_btn)  # 结果表批量粘贴导入弹框确认按钮
        self.sleep(1)

    # 结果表自动计算
    def result_auto_complete(self):
        """结果表自动计算"""
        self.clicks('css', result_auto_complete_btn)
        self.wait_loading()

    # 结果表保存
    def save_result(self):
        log.info("mpcr结果表保存页面数据操作")
        self.clicks('css', result_save_btn)
        self.wait_loading()

    # 结果表提交
    def result_submit_sample(self):
        """结果表提交"""
        log.info(' MPCR结果表,点击提交')
        self.clicks('css', result_sumbit_btn)  # 提交按钮
        self.wait_loading()
        # 调用自定义截图方法
        Screenshot(self.driver).get_img("MPCR结果表点击提交按钮","弹出提交确认按钮")
        self.clicks('css', result_submit_comfirm)  # 提交确认按钮
        self.wait_loading()

        submit_info = self.get_text('css', result_sample_status)
        print('样本处理结果表提交状态', submit_info)
        return submit_info.strip()

    # 结果表样本流程环节写入Excel
    def write_data_to_excel(self):
        """根据结果表样本下一步流程，把对应的样本lims号、实验室号、下一步流程以追加形式写入该流程的Excel"""
        self.add_excel_xlxs(next_step_sql, exp_mpcr_result_t, result_task_id)
        print('下一步流程写入成功')

    # 完成任务单
    def complete_task(self):
        """完成任务单"""

        log.info('MPCR结果表,点击完成任务单')
        self.click_by_js('css', result_complete_task_btn)
        self.wait_loading()

        # 调用自定义截图方法：任务单已完成
        Screenshot(self.driver).get_img("MPCR结果表点击完成任务单按钮","完成任务单成功，状态改为完成")
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
        lims_id = read_excel_col(mpcr_file_path, 'lims号')
        self.input('css', search_lims_sample_num, lims_id[0])
        self.sleep(1)
        self.clicks('css', search_btn)
        if self.isElementExists('class_name', 'el-icon-loading'):
            self.wait_loading()
        self.sleep(1)
        samples = self.findelements('css', sample_page_list)
        return len(samples)
