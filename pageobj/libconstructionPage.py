# -*- coding: utf-8 -*-
# @Time    : 2022/08/16
# @Author  : guanzhong.zhou
# @File    : 文库构建模块页面功能封装
from datetime import datetime
import pyperclip
import xlrd
from selenium.webdriver.common.keys import Keys
from PageElements.wkgj_ele import *
from common.screenshot import Screenshot
from common.DataBaseConnection import executeSql
from common import editYaml
from common.xlsx_excel import get_lims_for_excel_by_col, pandas_write_excel, read_excel_col, write_data_toexcle
from conf.all_path import wkgj_file_path, functionpageURL_path, position_in_box_path, index_96_import
from conf.config import libconstruction_result
from conf.execute_sql_action import wkgj_detail_sql2, wkgj_result_sql1, wkgj_result_sql2, \
    wkgj_detail_sql3, gj_next_step
from uitestframework.basepageTools import BasePage
from common.logs import log


class LibconstructionPage(BasePage):
    """
    文库构建页面方法封装
    """

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

    # 新增任务单
    def add_task(self):
        """
        新建文库构建任务单
        """
        log.info("文库构建首页，点击新建按钮，进入样本待选表，新增文库构建任务")
        self.clicks('css', add_sample_process_task)
        self.wait_loading()

        log.info("选择样本类型")
        self.click_by_js('css', task_type)
        self.sleep(0.5)
        self.clicks('css', task_type_choice)
        self.wait_loading()

        log.info("选择操作类型")
        self.click_by_js('css', operation_type)
        self.sleep(0.5)
        self.clicks('css', operation_type_choice)
        self.sleep(1)

        log.info("选择sop")
        self.clicks('css', select_sop)
        self.sleep(0.5)
        self.clicks('css', select_sop_choice)
        self.wait_loading()

    # excel中获取待选样本

    # 待选表校验lims号
    def check_lims_num(self):
        """
        待选表核对lims号功能，并保存任务单号
        """
        lims_id_str = get_lims_for_excel_by_col(wkgj_file_path)
        log.info('获取接样流程中的lims样本号,核对lims号是否存在')
        self.clicks('css', check_lims_sample_num)
        self.sleep(1)
        self.input('css', check_lims_sample_number_textarea, lims_id_str)
        self.sleep(0.5)
        self.clicks('css', check_lims_sample_number_confirm)
        self.wait_loading()
        self.sleep(1)

        # 如果有未查到的样本，忽略
        if self.isElementExists('xpath', error_info):
            self.clicks('xpath', error_info)

        log.info('选中核对后的样本，点击【加入选中样本&保存】')
        self.click_by_js('css', all_choice)
        self.sleep(0.5)
        self.clicks('css', addSelect_or_save_btn)
        pageInfo = self.get_pageinfo()
        Screenshot(self.driver).get_img("文库构建待选表点击核对lims号，录入样本号进行查询，勾选查询结果，并保存任务单号", "保存任务单成功")
        self.wait_loading()
        return pageInfo

    # 进入明细表或结果表
    def enter_result_list(self, ele, page):
        """
        待选表或者明细表，在进入下一节点时，获取下一节点URL地址，并写入临时数据文件中
        :param ele: 点击进入下一节点元素定位
        :param page: 下一节点页面名称
        """
        urldata = editYaml.read_yaml(functionpageURL_path)

        self.clicks('css', ele)
        log.info('点击按钮进入{}'.format(page))
        self.wait_loading()
        self.wait_loading()  #
        self.sleep(2)

        url = self.get_current_url()  # 获取当前页面URL地址
        print('获取的URL地址', url)
        urldata["url"] = url
        editYaml.save_yaml(functionpageURL_path, urldata)  # 写入模式获取的URL地址到yaml文件中
        print("写入后的URL地址", urldata)

    # 明细表入库信息、批量包装余量、录入96孔版位置
    def detail_libconstruction(self):
        """文库构建明细表，选择入库信息、批量包装余量"""
        self.clicks('css', detail_all_choice)  # 列表全选按钮
        log.info("文库构建明细表录入批量包装余量")
        self.clicks('css', batch_remaining_sample_package_amount)  # 明细表批量包装余量
        self.sleep(0.5)
        self.clicks('css', batch_remaining_sample_package_amount_comfirm)  # 明细表批量包装余量确认
        self.sleep(1)

    def index_96_import(self):
        """96孔板位置和INDEX导入"""
        log.info("文库构建明细表96孔板位置和INDEX导入")
        taskstatus = self.get_text('css', detail_task_id)  # 获取任务单号
        print('富集任务单号', taskstatus)
        lims_list = executeSql.test_select_limsdb(
            wkgj_detail_sql3.format(taskstatus[5:].strip()))
        values_list = [list(d.values()) for d in lims_list]
        new_list = [[i + 1] + item + [i + 1] for i, item in enumerate(values_list)]  # 从数据库获取当前任务单号下样本lims号和实验室号，转换为二维列表
        print(new_list)
        write_data_toexcle(index_96_import, new_list)  # 将二维列表写入Excel
        log.info("点击文库构建明细表96孔板位置和INDEX导入按钮")
        self.clicks('css', col_96_well_plate_position)  # 点击96孔板位置和INDEX导入按钮
        self.sleep(0.5)
        Screenshot(self.driver).get_img("文库构建明细表点击96孔板位置和INDEX导入按钮", "弹出导入弹框")
        # 执行修改元素属性js
        self.executeJscript(
            "document.querySelector('.el-dialog--center .el-dialog__body .el-upload__input').style.setProperty('display','block','important');")
        self.sleep(0.5)
        log.info("点击文库构建明细表96孔板位置和INDEX上传导入文件")
        self.input('css', col_96_well_plate_position_input, index_96_import)  # 上传导入文件
        self.sleep(1)
        self.clicks('css', col_96_well_plate_position_upload)
        self.wait_loading()

    # 明细表表单自动计算
    def detail_libconstruction_form_input(self):
        """明细表表单自动计算"""
        log.info("点击自动计算")
        self.sleep(0.5)
        self.clicks('css', detail_auto_calculate)
        self.wait_loading()
        self.sleep(0.5)

    # 明细表提交
    def detail_sumbit(self):
        """文库构建明细表，样本提交操作"""
        log.info("文库构建明细表样本提交")
        self.click_by_js('css', detail_all_choice)
        self.sleep(0.5)
        self.clicks('css', submit_btn)  # 提交按钮
        self.sleep(0.5)
        Screenshot(self.driver).get_img("文库构建明细表点击提交按钮", "弹出提交确认按钮")
        self.click_by_js('css', submit_comfirm)  # 提交弹框确认按钮
        self.wait_loading()
        self.sleep(1)

    # 明细表入库
    def detail_into_storage(self):
        """
        文库构建明细表样本入库操作
        """
        try:
            log.info('文库构建明细表，样本入库操作')
            self.clicks('css', deposit_into_storage)  # 入库按钮
            self.sleep(0.5)
            self.clicks('css', storage_all_choice)  # 入库弹框全选按钮
            self.sleep(0.5)

            log.info('文库构建明细表，样本入库选择入样本盒')
            self.clicks('css', batch_paste_sample_box)  # 入库弹框选择样本盒按钮
            self.wait_loading()
            self.input('css', target_storage, '自动化测试用(勿删)')
            self.sleep(0.5)
            self.clicks('css', select_sample_box_search)
            self.wait_loading()
            self.sleep(0.5)
            self.clicks('css', select_sample_box_choice)  # 入库弹框选选择样本盒值，默认选择列表第一条数据
            self.sleep(0.5)
            self.clicks('css', select_sample_box_comfirm)  # 入库弹框选选择样本盒弹框，确认按钮
            self.sleep(0.5)

            log.info('文库构建明细表，样本入库批量粘贴盒内位置')

            taskstatus = self.get_text('css', detail_task_id)  # 获取任务单号
            print(taskstatus)
            lims_id = executeSql.test_select_limsdb(
                wkgj_detail_sql2.format(taskstatus[5:].strip()))  # 从数据库获取当前任务单号下样本lims号

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
            Screenshot(self.driver).get_img("文库构建明细表点击入库按钮，在弹框中录入库位信息和盒内位置后点击下一步", "样本入库成功")

            self.clicks('css', storage_next)
            self.wait_loading()

            # self.executeJscript('document.getElementsByClassName("vxe-table--body-wrapper")[0].scrollLeft=3080')
            samples_status = self.get_text('css', submit_status)
            print('明细表状态', samples_status)
            self.sleep(1)
            return samples_status
        except Exception as info:
            print(info)

    # 结果表批量数据录入
    def ultrasonic_result_data_input(self):
        """
        文库构建结果表修改产物类型、批量数据
        """
        log.info("文库构建结果表，修改产物类型")
        self.clicks('css', result_all_choice)  # 样本列表数据全选按钮
        self.sleep(0.5)
        self.clicks('css', result_change_product_type)  # 修改产物类型
        self.sleep(0.5)
        self.clicks('css', result_change_product_type_choice)  # 修改产物类型弹框数据选择，默认选择第一条
        self.sleep(0.5)
        self.clicks('css', result_change_product_type_comfirm)  # 修改产物类型弹框数据选择，确认
        self.sleep(0.5)
        ele = self.isDisplayed('xpath', error_info_box)
        print(ele)
        if ele:
            self.clicks('css', result_change_product_type_continue_comfirm)
        self.wait_loading()
        self.sleep(1)

        log.info("文库构建结果表，批量数据")
        self.clicks('css', result_batch_data)  # 批量数据按钮
        self.wait_loading()
        self.sleep(0.5)
        self.input('css', result_sample_package_amount, 1)  # 批量数据弹框，产物包装量
        self.sleep(0.5)
        self.clicks('css', result_sample_package_amount_unit)  # 批量数据弹框，包装单位下拉框
        self.sleep(0.5)
        self.clicks('css', result_sample_amount_unit_choice)  # 批量数据弹框，包装单位下拉值（管 ）
        self.sleep(0.5)
        self.input('css', result_number_of_ircular_labels_printed, 1)  # 批量数据弹框，圆打印份数文本框
        self.sleep(0.5)
        self.input('css', result_number_of_rectangular_labels_printed, 1)  # 批量数据弹框，长打印份数文本框
        self.sleep(0.5)
        self.clicks('css', adapter_concentration)
        self.sleep(0.5)
        self.clicks('css', adapter_concentration_choice)
        self.sleep(0.5)
        self.input('xpath', pcr_cycle, 6)  # 批量数据弹框，循环数
        self.sleep(0.5)
        self.input('css', library_volume, 10)  # 批量数据弹框，文库体积
        self.sleep(0.5)

        self.clicks('css', result_batch_data_comfirm)  # 批量数据弹框，确认按钮
        self.sleep(0.5)
        self.clicks('css', result_save_task)
        self.wait_loading()

        # 预计富集时间

    def edit_estimated_enrichment_time(self):
        """
        预计富集时间
        """
        now_time = datetime.now()
        str_time = now_time.strftime('%Y.%m.%d')  # 获取当前时间
        self.clicks('css', edit_estimated_enrichment_time)  # 预计富集时间按钮
        self.wait_loading()
        self.clicks('css', edit_estimated_enrichment_time_all_choice)  # 预计富集时间弹框全选
        self.sleep(0.5)
        self.clicks('css', batch_edit_estimated_enrichment_date)  # 预计富集时间弹框，录入时间弹框按钮
        self.sleep(0.5)
        self.input('css', estimated_enrichment_data, str_time)  # 预计富集时间弹框，时间录入文本
        self.sleep(0.5)
        self.clicks('css', estimated_enrichment_data_comfirm)  # 预计富集时间弹框，时间录入文本确认按钮
        self.sleep(0.5)
        self.clicks('css', edit_estimated_enrichment_time_comfirm)  # 预计富集时间弹框确认按钮
        self.wait_loading()
        self.sleep(0.5)
        self.clicks('css', result_save_task)
        self.wait_loading()
        self.sleep(0.5)

    # 结果表表单录入
    def ultrasonic_result_formdata_input(self):
        """
        文库构建结果表通过数据库进行大小片段分离后浓度、连接后纯化浓度、文库浓度、盒内位置录入
        """
        taskstatus = self.get_text('css', result_task_id)
        ##文库浓度1ng/μL*、文库浓度2ng/μL*、平均文库浓度ng/μL*录入

        self.updata_sql(wkgj_result_sql1.format(taskstatus[5:].strip()))
        # self.updata_sql(wkgj_result_sql1.format(taskstatus[5:].strip()))
        executeSql.test_updateByParam(wkgj_result_sql2.format(taskstatus[5:].strip()))  # 为对照样本设置预期通量
        print("为对照样本设置预期通量")
        # 刷新页面
        self.refresh()
        self.wait_loading()

        self.clicks('css', result_all_choice)
        log.info('文库构建结果表,点击批量计算')
        self.clicks('css', result_auto_calculate)
        self.wait_loading()
        self.sleep(1)
        ele = self.isElementExists('css', result_auto_calculate_promote)
        print(ele)
        if ele:
            self.click_by_js('css', result_auto_calculate_promote)
            self.sleep(1)
        log.info('文库构建结果表,生成盒内位置')
        self.clicks('css', result_postionInBox)
        self.sleep(0.5)
        self.clicks('css', result_postionInBox_confirm)
        self.sleep(0.5)
        self.clicks('css', result_postionInBox_info_confirm)
        self.sleep(1)

    def goback_detail(self):
        """返回明细表"""
        urldata = editYaml.read_yaml(functionpageURL_path)
        log.info('点击按钮返回明细表')
        self.click_by_js('css', goback_detail)

        self.clicks('css', goback_page_info)
        self.wait_loading()
        self.sleep(1)

        url = self.get_current_url()  # 获取当前页面URL地址
        print('获取的URL地址', url)
        urldata["url"] = url
        editYaml.save_yaml(functionpageURL_path, urldata)  # 写入模式获取的URL地址到yaml文件中
        print("写入后的URL地址", urldata)

    # 结果表提交
    def result_submit_sample(self):
        """
        结果表提交
        """
        log.info(' 文库构建结果表,点击提交')
        self.clicks('css', result_submit)  # 提交按钮
        self.wait_loading()
        self.sleep(0.5)

        Screenshot(self.driver).get_img("文库构建结果表点击提交按钮", "弹出提交确认按钮")

        self.clicks('css', result_submit_comfirm)  # 提交确认按钮
        self.wait_loading()
        self.sleep(0.5)

    # 结果表样本流程环节写入Excel
    def write_data_to_excel(self):
        """
         根据结果表样本下一步流程，把对应的样本lims号、实验室号、下一步流程以追加形式写入该流程的Excel
        """
        self.add_excel_xlxs(gj_next_step, libconstruction_result, result_task_id)
        print("下一步流程写入成功")

    # 完成任务单
    def complete_task(self):
        """
        完成任务单
        """
        log.info(' 文库构建结果表,点击完成任务单')
        self.clicks('css', enter_result_list_btn)
        self.wait_loading()
        self.sleep(0.5)

        self.clicks('css', result_complete_task_btn)
        if self.isElementExists('css', pageinfo):
            page_info = self.get_text('css', pageinfo)
            print(page_info)
            return page_info

        else:
            self.clicks('css', result_complete_task_comfirm)

            self.wait_loading()

            Screenshot(self.driver).get_img("文库构建结果表点击完成任务单按钮", "完成任务单成功，状态改为完成")
            task_status = self.get_text('css', detail_task_status)
            print(task_status)
            return task_status

    # 文库构建任务列表查询样本所在任务单
    def serach_task(self):
        """
        首页面查询已完成的样本任务单
        """
        lims_id = read_excel_col(wkgj_file_path, 'lims号')

        self.clicks('css', search)
        self.sleep(0.5)
        self.input('css', search_lims_sample_num, lims_id[0])
        self.sleep(0.5)
        self.clicks('css', search_confirm)
        self.wait_loading()
        self.sleep(0.5)
        samples = self.findelements('xpath', sample_page_list)
        print(len(samples))
        return len(samples)
