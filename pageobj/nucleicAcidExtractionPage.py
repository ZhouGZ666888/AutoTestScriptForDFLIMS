# -*- coding: utf-8 -*-
# @Time    : 2022/11/22
# @Author  : guanzhong.zhou
# @File    : 核酸提取模块页面功能封装
import pyperclip, xlrd
from selenium.webdriver.common.keys import Keys
from common import editYaml
from common.screenshot import Screenshot
from common.DataBaseConnection import executeSql
from common.xlsx_excel import get_lims_for_excel_by_col, pandas_write_excel, read_excel_col
from conf.all_path import  position_in_box_path, dataChangFile
from conf.config import extraction_result
from PageElements.hstq_ele import *
from conf.execute_sql_action import hstq_detail_sql, hstq_detail_sql3, hstq_detail_sql2, hstq_result_sql, next_step_sql, \
    check_sample_set
from uitestframework.basepageTools import BasePage
from uitestframework.exceptionsTools import FileNotFound
from common.logs import log


class NucleicAcidExtractionPage(BasePage):
    """核酸提取，待选表、明细表、结果表页面功能封装"""

    # 新增任务单
    def add_task(self):
        """新建核酸提取任务单"""
        log.info("核酸提取首页，点击新建按钮，进入样本待选表，新增核酸提取任务")
        self.clicks('css', add_sample_process_task)
        self.wait_loading()

        log.info("选择任务类型")
        self.click_by_js('css', task_type)
        self.clicks('css', task_type_choice)
        self.wait_loading()

        log.info("操作方式")
        self.clicks('css', action_type)
        self.clicks('css', operationType_choice)
        self.sleep(0.5)

        log.info("选择sop")
        self.clicks('css', select_sop)
        self.sleep(0.5)
        self.clicks('css', select_sop_choice)
        self.wait_loading()

    # 待选表校验lims号
    def check_lims_num(self, path):
        """核对lims号功能，并保存任务单号"""
        # excel中获取待选样本
        sample_nub = get_lims_for_excel_by_col(path)
        log.info('获取接样流程中的lims样本号,核对lims号是否存在')

        if sample_nub is None:
            raise FileNotFound("没有找到Excel中的流转样本")
        else:
            self.clicks('css', check_lims_sample_num)
            self.sleep(0.5)

            self.input('css', check_lims_sample_number_textarea, sample_nub)
            self.sleep(0.5)
            self.clicks('css', check_lims_sample_number_confirm)
            self.wait_loading()
            if self.isElementExists('xpath', search_err_info):
                raise FileNotFound("样本检索存在未知样本")
        self.sleep(0.5)

        log.info('选中核对后的样本，点击【加入选中样本&保存】')
        self.click_by_js('css', all_choice)
        self.sleep(0.5)
        self.clicks('css', addSelect_or_save_btn)

        # 调用自定义截图方法
        Screenshot(self.driver).get_img("核酸提取待选表点击核对lims号，录入样本号进行查询，勾选查询结果，并保存任务单号","保存任务单成功")

        pageinfo = self.get_pageinfo()
        self.wait_loading()
        return pageinfo

    # 进入明细表或结果表
    def enter_result_list(self, ele, page):
        """
        进入下一节点
        :param ele: 点击进入下一节点元素定位
        :param page: 下一节点页面名称
        """
        self.clicks('css', ele)
        log.info('点击按钮进入{}'.format(page))
        self.wait_loading()

    def save_item_url(self):
        """获取提取结果表URL地址和任务单号，存入临时文件，作为数据修改模块修改数据使用"""
        taskstatus = self.get_text('css', detail_task_id)
        task_id = taskstatus[5:].strip()
        urldata = editYaml.read_yaml(dataChangFile)
        url = self.get_current_url()  # 获取当前页面URL地址
        urldata["datachange_url"] = url
        urldata["datachange_extraction_taskId"] = task_id
        editYaml.save_yaml(dataChangFile, urldata)  # 写入模式获取的URL地址到yaml文件中

        print("写入后的临时文件内容：", urldata)

    def aliquot_sample(self):
        """样本分管操作"""
        log.info('样本分管操作')
        # 选择一条数据进行分管
        self.clicks('css', first_sample)
        self.sleep(0.5)
        self.clicks('css', aliquot_sample)  # 点击分管按钮
        self.sleep(0.5)
        self.clicks('css',aliquot_before_tips)
        self.sleep(1)


        # 调用自定义截图方法
        Screenshot(self.driver).get_img("核酸提取明细表选中一条样本，点击分管按钮","打开分管弹框")

        self.clicks('css', aliquot_sample_all_choice)  # 分管弹框全选按钮
        self.input('xpath', aliquot_number, 1)  # 分管弹框分管数文本录入
        self.clicks('xpath', aliquot_number_batch_edit)  # 分管弹框分管数文本录入后批量填入按钮
        self.clicks('xpath', aliquot_sample_next)  # 分管弹框下一步按钮
        self.sleep(1)

        log.info('样本分管批量录入操作')
        self.clicks('css', aliquot_sample_last_step_all_choice)  # 分管批量录入弹框全选
        self.clicks('css', aliquot_sample_batch_data)  # 分管弹框批量录入按钮
        self.sleep(0.5)

        log.info('分管批量录入操作,“是否做mPCR”选择否')
        self.click_by_js('css', aliquot_sample_ismPCR)  # 批量录入是否做mPCR
        self.sleep(0.5)
        self.click_by_js('css', aliquot_sample_ismPCR_input)
        self.sleep(0.5)
        self.click_by_js('css', aliquot_sample_ismPCR_chioce)
        self.sleep(0.5)

        log.info('样本分管批量录入操作,“最后步骤”选择上机')
        self.click_by_js('css', aliquot_sample_lastStep)  # 分管弹框最后步骤下拉值选择
        self.sleep(0.5)
        self.click_by_js('css', aliquot_sample_lastStep_input)
        self.sleep(0.5)
        self.click_by_js('css', aliquot_sample_lastStep_chioce)
        self.sleep(0.5)

        log.info('样本分管批量录入操作,“建库类型”选择DNA建库')
        self.click_by_js('css', aliquot_sample_libType)  # 分管弹框建库类型下拉值选择
        self.sleep(0.5)
        self.click_by_js('css', aliquot_sample_libType_input)
        self.sleep(0.5)
        self.click_by_js('css', aliquot_sample_libType_chioce)
        self.sleep(0.5)


        self.click_by_js('css', aliquot_sample_confirm_btn)  # 批量弹框录入后确认
        self.click_by_js('css', aliquot_sample_last_step_comfirm)  # 明细表分管弹框分管后确认按钮
        self.wait_loading()

    # 添加NTC对照
    def add_NTC_type(self, ele):
        """添加NTC对照"""

        self.clicks('css', add_ntc)  # 添加ntc对照按钮
        self.wait_loading()
        self.clicks('css', ntc_choice)  # 对照大类选择框
        self.clicks('css', choice_ntc_type)  # 选择NTC对照类型
        self.sleep(0.5)
        self.clicks('css', choice_ntc_sample_type)  # 选择对照样本类型
        self.sleep(0.5)
        self.clicks('css', ele)  # 选择对照样本类型
        self.clicks('css', add_ntc_confirm)
        self.clicks('css', add_duizhao_confirm)
        self.wait_loading()

    # 明细表数据录入操作
    def extraction_detail(self):
        """
        核酸提取明细表数据录入、自动计算操作
        """
        log.info('核酸提取明细表点击生成排序号')

        self.clicks('css', create_sort_number)  # 生成排序号按钮
        self.sleep(0.5)
        self.clicks('css', detail_all_choice)  # 全选样本
        self.sleep(0.5)

        log.info('核酸提取明细表，进行批量数据录入')
        self.clicks('css', detail_batch_data)  # 明细表批量数据按钮
        self.sleep(0.5)
        self.input('css', detail_used_sample_amount, 1)  # 明细表批量数据，样本进入量
        self.sleep(0.5)
        self.input('css', detail_remaining_sample_package_amount, 1)  # 明细表批量数据，包装余量

        self.clicks('css', detail_sample_package_amount_unit)  # 明细表批量数据，包装单位下拉框
        self.sleep(0.5)
        self.clicks('xpath', detail_sample_package_amount_unit_value)  # 明细表批量数据，包装单位下拉值
        self.sleep(0.5)
        self.clicks('css', detail_remaining_sample_package_amount_unit)  # 明细表批量数据，包装余量单位下拉框
        self.sleep(0.5)
        self.clicks('xpath', detail_remaining_sample_package_amount_unit_value)  # 明细表批量数据，包装余量单位下拉值
        self.sleep(0.5)
        self.clicks('css', detail_batch_data_comfirm)  # 明细表批量数据弹框，确认按钮
        self.sleep(1)
        self.clicks('css', detail_save_result)  # 保存
        self.wait_loading()
        # 设置余样计量
        taskstatus = self.get_text('css', detail_task_id)
        sqls = hstq_detail_sql.format(taskstatus[5:].strip())
        self.updata_sql(sqls)
        # 刷新页面
        self.refresh()
        self.wait_loading()

        self.clicks('css', detail_all_choice)  # 全选样本
        self.sleep(0.5)
        log.info('核酸提取明细表，自动计算')
        self.clicks('css', detail_auto_calculate)  # 自动计算按钮
        self.sleep(1)

    # 明细表提交
    def detail_submit(self):
        """
        明细表样本提交操作
        """
        log.info('核酸提取明细表，点击提交')
        # 设置余样计量
        taskstatus = self.get_text('css', detail_task_id)
        sqls = hstq_detail_sql3.format(taskstatus[5:].strip())
        self.updata_sql(sqls)
        # 刷新页面
        self.refresh()
        self.wait_loading()

        self.clicks('css', detail_all_choice)  # 全选样本
        self.sleep(0.5)
        self.click_by_js('css', submit_btn)  # 提交按钮
        self.sleep(0.5)
        self.clicks('css', submit_comfirm)  # 提交弹框确认按钮

        # 调用自定义截图方法
        Screenshot(self.driver).get_img("核酸提取明细表点击提交按钮","弹出提交确认按钮")
        self.wait_loading()

    # 明细表入库
    def detail_into_storage(self):
        """明细表样本入库操作"""
        log.info('核酸提取明细表，样本入库操作')
        self.clicks('css', deposit_into_storage)  # 入库按钮
        self.sleep(0.5)
        self.clicks('css', storage_all_choice)  # 入库弹框全选按钮
        self.sleep(0.5)

        log.info('核酸提取明细表，样本入库选择入样本盒')
        self.clicks('xpath', batch_paste_sample_box)  # 入库弹框选择样本盒按钮
        self.wait_loading()
        self.input('css', target_storage, '自动化测试用(勿删)')
        self.sleep(0.5)
        self.clicks('css', select_sample_box_search)
        self.wait_loading()
        self.clicks('css', select_sample_box_choice)  # 入库弹框选选择样本盒值，默认选择列表第一条数据
        self.sleep(0.5)
        self.clicks('css', select_sample_box_comfirm)  # 入库弹框选选择样本盒弹框，确认按钮
        self.sleep(0.5)

        log.info('核酸提取明细表，样本入库批量粘贴盒内位置')

        taskstatus = self.get_text('css', detail_task_id)  # 获取任务单号
        lims_id = executeSql.test_select_limsdb(hstq_detail_sql2.format(taskstatus[5:].strip()))  # 从数据库获取当前任务单号下样本lims号

        lims_list = [item[key] for item in lims_id for key in item]  # 把获取的lims号转换为一维列表
        nub_list = [str(i) for i in range(1, len(lims_list) + 1)]  # 根据lims样本数量，生成数字列表，作为盒内位置编号用
        res = [list(i) for i in zip(lims_list, nub_list)]  # 将lims号和数字编号转换为二维列表格式，写入Excel
        print(res)
        pandas_write_excel(res, position_in_box_path)

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
        self.findelement('css', batch_copy_BoxPosition_input).send_keys(Keys.CONTROL, 'v')
        self.sleep(1)
        self.clicks('css', batch_copy_BoxPosition_comfirm)
        self.sleep(0.5)

        # 调用自定义截图方法
        Screenshot(self.driver).get_img("核酸提取明细表点击入库按钮，在弹框中录入库位信息和盒内位置后点击下一步","样本入库成功")

        self.click_by_js('css', storage_next)
        self.wait_loading()

        self.executeJscript('document.getElementsByClassName("vxe-table--body-wrapper")[0].scrollLeft=3080')
        samples_status = self.get_text('css', submit_status)
        self.sleep(1)
        return samples_status

    # 结果表结果表修改产物类型，批量数据录入
    def extraction_result_data_input(self):
        """
        核酸提取结果表修改产物类型，批量数据录入
        """

        log.info('核酸提取结果表，修改样本产物类型')
        self.clicks('css', sortNo)
        self.sleep(0.5)
        self.clicks("css", result_all_choice)  # 样本列表数据全选按钮
        self.sleep(0.5)
        self.clicks("css", result_change_product_type)  # 修改产物类型
        self.wait_loading()
        self.clicks("xpath", result_change_product_type_choice)  # 修改产物类型弹框数据选择，默认选择游离DNA
        self.clicks("xpath", result_change_product_type_comfirm)  # 修改产物类型弹框数据选择，确认
        self.wait_loading()
        ele = self.isElementExists('css', result_change_product_type_continue_comfirm)
        print(ele)
        if ele:
            self.click_by_js('css', result_change_product_type_continue_comfirm)
            self.wait_loading()
        self.sleep(1)

        log.info('核酸提取结果表，录入批量数据')
        self.clicks("css", result_batch_data)  # 批量数据按钮
        self.sleep(0.5)
        self.input("css", result_product_amount, 1)  # 批量数据弹框，产物包装量
        self.sleep(0.5)

        self.clicks("css", result_sample_amount_unit)  # 批量数据弹框，包装单位下拉框
        self.sleep(0.5)
        self.clicks("xpath", result_sample_amount_unit_choice)  # 批量数据弹框，包装单位下拉值（管 ）
        self.sleep(0.5)

        self.input("css", result_sample_package_amount, 1)  # 批量数据弹框，圆标签打印份数文本框
        self.sleep(0.5)

        self.input("css", result_sampl_package_amount_unit, 1)  # 批量数据弹框，长标签打印份数文本框
        self.sleep(0.5)

        self.input('css', result_sampl_package_amount_unit_choice, 5)  # 批量数据弹框，产物体积

        self.clicks("xpath", result_batch_data_comfirm)  # 批量数据弹框，确认按钮
        self.sleep(0.5)

        self.clicks('css', result_save_result)  # 保存录入批量数据
        self.wait_loading()

    # 结果表表单数据录入
    def extraction_result_formdata_input(self):
        """
        核酸提取结果表，通过数据库进行表单数据录入，产物Qubit浓度、值为20
        """
        log.info(' 核酸提取结果表，表单数据录入,并点击自动计算')
        taskstatus = self.get_text('css', result_task_id)
        print("提取任务单号")
        # 产物Qubit浓度、值为20
        executeSql.test_updateByParam(hstq_result_sql.format(taskstatus[5:].strip()))
        self.sleep(0.5)

        # 刷新页面
        self.refresh()

        log.info(' 核酸提取结果表,点击自动计算')
        self.clicks('css', result_all_choice)
        self.sleep(0.5)
        self.clicks('css', result_auto_calculate)
        self.sleep(0.5)
        if self.isElementExists('css', result_auto_calculate_promote):
            self.clicks('css', result_auto_calculate_promote)
        self.sleep(1)

        log.info(' 核酸提取结果表,批量生成盒内位置')
        self.clicks('css', result_postionInBox)
        self.sleep(0.5)
        self.clicks('css', result_postionInBox_confirm)
        self.clicks('css', result_postionInBox_info_confirm)
        self.sleep(0.5)

    # 结果表提交
    def result_submit_sample(self):
        """结果表提交"""
        log.info(' 核酸提取结果表,点击提交')
        self.clicks('css', result_submit)  # 提交按钮
        # 调用自定义截图方法
        Screenshot(self.driver).get_img("核酸提取结果表点击提交按钮","弹出提交确认按钮")
        self.wait_loading()
        if self.isElementExists('css', nextProcessorId):
            self.sleep(1)
            self.clicks('css', nextProcessorId)
            self.sleep(0.5)
            self.input('css', nextProcessorId, 'dgq')
            self.wait_loading()
            self.clicks('css', nextProcessorId_choice)
        self.sleep(0.5)
        self.clicks('css', result_submit_comfirm)  # 提交确认按钮
        self.wait_loading()
        self.executeJscript('document.getElementsByClassName("vxe-table--body-wrapper")[0].scrollLeft=5000')
        self.sleep(0.5)
        submit_info = self.get_text('css', result_sample_status)
        print('样本处理结果表提交状态', submit_info)
        return submit_info

    # 结果表样本流程环节写入Excel
    def write_data_to_excel(self):
        """根据结果表样本下一步流程，把对应的样本lims号、实验室号、下一步流程以追加形式写入该流程的Excel"""
        self.add_excel_xlxs(next_step_sql, extraction_result, result_task_id)
        print('下一步流程写入成功')
        log.info("返回样本处理明细表,进行明细表提交操作")
        self.clicks('css', goback_detail_table)
        self.sleep(0.5)
        self.clicks('css', goback_detail_table_confirm)
        self.wait_loading()

    # 完成任务单
    def complete_task(self):
        """完成任务单"""
        log.info('核酸提取结果表,点击完成任务单')
        self.clicks('css', goResult)
        self.wait_loading()
        self.save_item_url()  # 存储提取模块的URL地址，在数据修改模块使用
        self.click_by_js('css', result_complete_task_btn)
        self.wait_loading()
        # 调用自定义截图方法
        Screenshot(self.driver).get_img("核酸提取结果表点击完成任务单按钮","完成任务单成功，状态改为完成")
        taskstatus = self.get_text('css', task_status)
        print("明细表提交状态",taskstatus)
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
    def serach_task(self, path):
        """
        首页面查询已完成的样本任务单
        """
        lims_id = read_excel_col(path, 'lims号')
        self.clicks('css', search)
        self.sleep(1)
        self.input('css', search_lims_sample_num, lims_id[0])
        self.sleep(1)
        self.clicks('css', search_confirm)
        if self.isElementExists('class_name', 'el-icon-loading'):
            self.wait_loading()
        self.sleep(1)
        samples = self.findelements('xpath', sample_page_list)
        return len(samples)

    def enter_function_page(self, url):
        """进入指定url页面"""
        js = 'window.open("{}");'
        self.executeJscript(js.format(url))
        self.wait_loading()
