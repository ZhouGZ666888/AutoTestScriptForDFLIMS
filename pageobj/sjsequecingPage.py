# -*- coding: utf-8 -*-
# @Time    : 2022/08/31
# @Author  : guanzhong.zhou
# @File    : 上机模块页面功能封装
from datetime import datetime
import pyperclip, time, xlrd
from selenium.webdriver.common.keys import Keys
from common import editYaml
from common.screenshot import Screenshot
from common.DataBaseConnection import executeSql
from common.xlsx_excel import read_excel_col, pandas_write_excel
from PageElements.sj_sequecing_ele import *
from conf.all_path import sj_file_path, functionpageURL_path, position_in_box_path, qpcr_task_refresh_sql, \
    sj_fc_quality_control_result, sampledata_path
from conf.execute_sql_action import *
from uitestframework.basepageTools import BasePage
from uitestframework.exceptionsTools import NotFoundError, MyBaseFailure
from common.logs import log


class SjSequecingPage(BasePage):
    """
    上机页面方法封装
    """

    # 打开指定页面
    def enter_function_page(self, url):
        """
        进入指定url页面
        """
        js = 'window.open("{}");'
        self.executeJscript(js.format(url))
        self.wait_loading()
        self.sleep(1)

    # 获取页面提示信息
    def get_pageinfo(self):
        """
        获取页面操作提示信息
        Task list saved successfully---保存样本到任务单成功
        Submit successfully---提交成功
        sample in storage successfully---入库成功
        """

        return self.get_text('xpath', page_success_info)

    # 新增任务单
    def add_task(self):
        """
        新建上机任务单
        """

        # 获取当前时间
        str_time = time.strftime("%Y.%m.%d %H:%M:%S", time.localtime())

        log.info("上机首页，点击新建按钮，进入样本待选表，新增上机任务")
        self.clicks('css', add_task)
        self.wait_loading()

        log.info("录入上机批次号")
        self.input('css', sequencing_batch_number, str_time + "批次")
        self.sleep(0.5)

        log.info("选择测序仪")
        self.clicks('css', instrument)
        self.wait_loading()
        self.input('css', instrument_search, 'Nextseq550DX-2')
        self.sleep(0.5)
        self.clicks('css', instrument_search_btn)
        self.wait_loading()
        self.clicks('css', instrument_choice)
        self.sleep(0.5)
        self.clicks('css', instrument_comfirm)
        self.sleep(0.5)

        log.info("运行模式")
        self.click_by_js('css', runningMode)
        self.sleep(0.5)
        self.clicks('css', runningMode_choice)
        self.sleep(0.5)

        log.info("实际上机时间")
        self.input('css', seqStartTime, str_time)
        self.sleep(0.5)

        log.info("samplesheet名称")
        self.input('css', samplesheetname, time.strftime("%m_%d")+'_samplesheet')
        self.sleep(0.5)

        log.info("任务描述")
        self.input('css', task_des, '自动化测试任务')
        self.sleep(0.5)

        log.info(" 选择上机SOP")
        self.clicks('css', select_sequecing_sop)
        self.sleep(0.5)
        self.clicks('css', select_sequecing_sop_choice)
        self.wait_loading()

        log.info("选择 上机实验员")
        self.clicks('css', sequencing_laboratory_personnel)
        self.input('css', sequencing_laboratory_personnel, 'dgq')
        self.wait_loading()
        self.clicks('css', sequencing_laboratory_personnel_choice)
        self.sleep(1)

    # 根据数据流转Excel中的上机样本lims号，在待选表中进行比对并选择
    def get_sequecing_sample_from_excel(self):
        """从对应的Excel中获取上一步流传下来的本节点的待选表lims样本号,g根据没页显示13条时，通过滚动下拉进度条，依次判断选取样本"""
        log.info(" 从上一步流转Excel中获取上机样本号,根据样本lims号文本进行点击选择")

        lims_nub = read_excel_col(sj_file_path, '上机用LIMS号')
        print(lims_nub)
        s = self.findelements('css', all_samples)
        try:
            for i in range(0, len(s)):
                laboratorys = self.get_text('css', lims_number.format(i + 1))
                # print(laboratorys)
                if laboratorys in lims_nub:  # 判定当前取值是否与上次一样，以此来判断是否下拉到底
                    # print('来了，点它')
                    self.click_by_js('css', lims_number.format(i + 1))
                    self.sleep(0.5)
        except NotFoundError as e:
            print(e)

    # 根据数据流转Excel中的上机样本lims号，在待选表中进行比对并选择
    def get_sequecing_sample_from_excel_by_scoll(self):
        """
         从对应的Excel中获取上一步流传下来的本节点的待选表lims样本号,g根据没页显示13条时，通过滚动下拉进度条，依次判断选取样本
        """
        log.info(" 从上一步流转Excel中获取上机样本号,根据样本lims号文本进行点击选择")

        lims_nub = read_excel_col(sj_file_path, '上机用LIMS号')
        print(lims_nub)

        # 下面为滚动下拉进行判断
        used_list = []  # 滚动计数，前面滚动了100像素（每行50像素，共两行），这里从3*50开始，即第三行开始校验，后面依次增加1行
        nubs = 1
        scoll = True
        try:
            while scoll:
                # 因为弹框每次只显示11条数据，所以需要一边滑动下拉，一边进行数据判定；第一次下拉100xp后，后面每次下拉50xp，把每行都排在第二行的位置上
                for i in range(0, 13):
                    laboratorys = self.get_text('css', lims_number.format(i + 1))

                    # 判断是否符合条件
                    if laboratorys in lims_nub:  # 判定当前取值是否与上次一样，以此来判断是否下拉到底
                        print(laboratorys)
                        if laboratorys not in used_list:
                            print('来了，点它')
                            self.click_by_js('css', lims_number.format(i + 1))
                            self.sleep(0.5)
                        else:
                            scoll = False
                    elif laboratorys in used_list:
                        scoll = False
                    used_list.append(laboratorys)
                jsscript = 'document.querySelector(".createTask_content_table .vxe-table--main-wrapper .vxe-table--body-wrapper.body--wrapper").scrollTop=50+650*{}'.format(
                    nubs)
                self.executeJscript(jsscript)
                nubs += 1
        except  Exception as s:
            print(s)

    # 加入选中样本&保存任务单
    def addSelect_or_save_task(self):
        """
        加入选中样本&保存任务单
        """
        log.info("调用选择样本方法-----")
        self.get_sequecing_sample_from_excel()
        log.info(" 选中核对后的样本，点击【加入选中样本&保存】")
        self.clicks('css', addSelect_or_save_btn)

        # 调用自定义截图方法
        Screenshot(self.driver).get_img("上机待选表点击核对lims号，录入样本号进行查询，勾选查询结果，并保存任务单号","保存任务单成功")

        pageinfo = self.get_pageinfo()
        self.wait_loading()
        # 获取上机任务单号，在samplesheet模块查询使用
        taskid = self.get_text('css', task_id)
        sampledata = editYaml.read_yaml(sampledata_path)
        sampledata['sj_taskid'] = taskid[5:].strip()
        editYaml.save_yaml(sampledata_path, sampledata)
        return pageinfo

    # 进入明细表或结果表
    def enter_result_list(self, types, ele, page):
        """
        待选表或者明细表，在进入下一节点时，获取下一节点URL地址，并写入临时数据文件中
        :param types: 定位类型
        :param ele: 点击进入下一节点元素定位
        :param page: 下一节点页面名称
        """
        urldata = editYaml.read_yaml(functionpageURL_path)

        self.clicks(types, ele)
        log.info('点击按钮进入{}'.format(page))
        self.wait_loading()

        url = self.get_current_url()  # 获取当前页面URL地址
        print('获取的URL地址', url)
        urldata["url"] = url
        editYaml.save_yaml(functionpageURL_path, urldata)  # 写入模式获取的URL地址到yaml文件中

        print("写入后的URL地址", urldata)

    # 浓度调整前明细表生成结果操作
    def detail_before_concentration_adjustment_create_concentration_adjustment_result(self):
        """
        浓度调整前明细表生成结果操作
        """
        self.clicks('css', before_concentration_adjustment_all_choice)  # 列表全选按钮
        self.clicks('css', before_concentration_adjustment_create_concentration_adjustment_result)  # 生成结果按钮
        self.wait_loading()
        # 调用自定义截图方法
        Screenshot(self.driver).get_img("浓度调整前明细表点击生成结果按钮","生成结果成功")
        self.sleep(0.5)

    # 浓度调整前明细表提交
    def detail_before_concentration_adjustment_sumbit(self):
        """
        上机明细表，样本提交操作
        """
        log.info(" 上机浓度调整前明细表样本提交")
        self.clicks('css', before_concentration_adjustment_all_choice)  # 列表全选按钮
        self.sleep(0.5)
        self.clicks('css', before_concentration_adjustment_submit)  # 提交按钮
        self.sleep(0.5)
        # 调用自定义截图方法
        Screenshot(self.driver).get_img("浓度调整前明细表点击提交按钮","弹出提交确认按钮")
        self.clicks('css', before_concentration_adjustment_submit_comfirm)  # 提交弹框确认按钮
        self.wait_loading()

    # 浓度调整前明细表入库
    def detail_before_concentration_adjustment_sumbit_into_storage(self):
        """
        上机浓度调整前明细表样本入库操作
        """
        log.info("上机浓度调整前明细表，样本入库操作")
        self.clicks('css', before_concentration_adjustment_all_choice)  # 列表全选按钮
        self.sleep(0.5)
        self.clicks('css', before_concentration_adjustment_deposit_into_storage)  # 入库按钮
        self.sleep(1)
        self.clicks('css', storage_all_choice)  # 入库弹框全选按钮
        self.sleep(0.5)

        log.info("上机明细表，样本入库选择入样本盒")
        self.clicks('css', batch_paste_sample_box)  # 入库弹框选择样本盒按钮
        self.wait_loading()
        self.input('css', target_storage, '自动化测试用(勿删)')
        self.sleep(0.5)
        self.clicks('css', select_sample_box_search)
        self.wait_loading()
        self.clicks('css', select_sample_box_choice)  # 入库弹框选选择样本盒值，默认选择列表第一条数据
        self.clicks('css', select_sample_box_comfirm)  # 入库弹框选选择样本盒弹框，确认按钮
        self.sleep(1)

        log.info("上机明细表，样本入库录入盒内位置")
        taskstatus = self.get_text('css', before_concentration_detail_task_id)  # 获取任务单号
        lims_id = executeSql.test_select_limsdb(
            sj_detail_before_concentration_sql2.format(taskstatus[5:].strip()))  # 从数据库获取当前任务单号下样本lims号

        lims_list = [item[key] for item in lims_id for key in item]  # 把获取的lims号转换为一维列表
        nub_list = [str(i) for i in range(1, len(lims_list) + 1)]  # 根据lims样本数量，生成数字列表，作为盒内位置编号用
        res = [list(i) for i in zip(lims_list, nub_list)]  # 将lims号和数字编号转换为二维列表格式，写入Excel
        print(res)
        pandas_write_excel(res, position_in_box_path)  # 把样本号和盒内位置编号写入Excel模板

        data = xlrd.open_workbook(position_in_box_path)  # 从Excel读取模板样本号和盒内位置编号
        num_list = []
        for index in range(0, len(lims_list)):
            tables = data.sheets()[0]
            # allrows = tables.nrows
            vals = tables.row_values(index)
            imp_data = '\t'.join(map(str, vals))
            num_list.append(imp_data)
        print("\n".join(map(str, num_list)))
        pyperclip.copy("\n".join(map(str, num_list)))

        # 粘贴到【批量粘贴盒内位置】文本框
        self.clicks('css', batch_copy_BoxPosition)
        self.sleep(0.5)
        self.findelement('css', batch_copy_BoxPosition_input).send_keys(Keys.CONTROL, 'v')
        self.sleep(0.5)
        self.clicks('css', batch_copy_BoxPosition_comfirm)
        self.sleep(1)

        # 调用自定义截图方法
        Screenshot(self.driver).get_img("浓度调整前明细表点击入库按钮，在弹框中录入库位信息和盒内位置后点击下一步","样本入库成功")

        self.clicks('css', storage_next)
        self.wait_loading()

        self.executeJscript('document.getElementsByClassName("vxe-table--body-wrapper")[0].scrollLeft=3450')
        self.sleep(0.5)
        pageinfo = self.get_text('css', before_concentration_sumbit_status)
        print(pageinfo)
        return pageinfo

    # 浓度调整后明细表批量数据录入、自动计算
    def detail_after_concentration_adjustment_auto_calculate(self):
        """
        浓度调整后明细表批量数据录入、自动计算
        """
        # 数据库更新文库体积
        taskstatus = self.get_text('css', before_concentration_detail_task_id)
        self.updata_sql(sj_detail_after_concentration_sql1.format(taskstatus[5:].strip()))
        self.refresh()  # 刷新页面
        self.wait_loading()

        log.info(" 批量数据")
        self.clicks('css', after_concentration_adjustment_all_choice)  # 全选数据
        self.clicks('css', after_concentration_adjustment_datch_data)  # 浓度调整后明细表批量数据按钮
        self.sleep(0.5)
        self.input('css', after_concentration_adjustment_datch_data_used_amount, 5)  # 浓度调整后明细表批量数据,耗用量录入
        self.input('css', after_concentration_adjustment_datch_data_sequencer_read_length, 50)  # 浓度调整后明细表批量数据,测序读长
        self.clicks('css', after_concentration_adjustment_datch_data_comfirm)  # 浓度调整后明细表批量数据弹框确认
        self.sleep(1)

        log.info(" 自动计算")
        self.clicks('css', after_concentration_adjustment_auto_calculate)  # 浓度调整后明细表自动计算
        self.wait_pageinfo_end()

        log.info(" 保存")
        self.clicks('css', after_concentration_adjustment_save)
        self.wait_loading()

    # 浓度调整后明细表确认上机
    def detail_after_concentration_adjustment_confirm_sequencing(self):
        """
        确认上机
        """
        log.info(" 全选并点击确认上机")
        self.clicks('css', after_concentration_adjustment_all_choice)
        self.sleep(0.5)
        self.clicks('css', after_concentration_adjustment_confirm_sequencing)  # 点击确认上机按钮
        self.input('css', after_concentration_adjustment_confirm_sequencing_data,
                   datetime.now().strftime('%Y.%m.%d %H:%M:%S'))  # 录入实际上机时间
        self.clicks('xpath', after_concentration_adjustment_sequencing_data_confirm)  # 点击确认上机按钮

        try:
            self.wait_loading()
            # 调用自定义截图方法
            Screenshot(self.driver).get_img("浓度调整后明细表点击确认上机按钮","确认上机成功")
        except MyBaseFailure:
            self.refresh()
        self.sleep(1)

        # 读取sql
        with open(qpcr_task_refresh_sql, 'r', encoding='utf-8', errors='ignore') as f:
            sa = f.read()
        executeSql.test_updateByParam(sa)
        print('执行数据库刷新视图成功<+_+>')

        self.sleep(1)

    # 浓度调整后明细表 生成samplesheet
    def detail_after_concentration_adjustment_create_samplesheet(self):
        """
        生成samplesheet
        """
        log.info(" 全选并点击生成samplesheet")
        self.clicks('css', after_concentration_adjustment_all_choice)  # 全选样本
        self.sleep(0.5)
        self.clicks('css', after_concentration_adjustment_create_samplesheet)  # 点击生成samplesheet按钮
        self.sleep(1)
        self.clicks('xpath', after_concentration_adjustment_create_samplesheet_choice)  # 选择samplesheet模板
        self.sleep(1)
        self.clicks('css', after_concentration_adjustment_create_samplesheet_comfirm)
        self.wait_loading()
        try:
            if self.isDisplayed('css', tips):
                self.clicks('css', tips)
        except:
            self.refresh()

    # 浓度调整后明细表 提交
    def detail_after_concentration_adjustment_submit(self):
        """
        提交
        """
        taskstatus = self.get_text('css', before_concentration_detail_task_id)
        self.updata_sql(sj_detail_after_concentration_sql3.format(taskstatus[5:].strip()))
        self.refresh()  # 刷新页面
        self.wait_loading()

        self.clicks('css', after_concentration_adjustment_all_choice)  # 全选样本
        self.clicks('css', after_concentration_adjustment_submit)
        self.sleep(0.5)
        # 调用自定义截图方法
        Screenshot(self.driver).get_img("浓度调整后明细表点击提交按钮","弹出提交确认按钮")
        self.clicks('css', after_concentration_adjustment_submit_comfirm)
        self.wait_loading()

    # 浓度调整后明细表 入库
    def detail_after_concentration_adjustment_deposit_into_Storage(self):
        """
        入库
        """
        self.clicks('css', after_concentration_adjustment_all_choice)  # 全选样本
        self.sleep(0.5)

        self.clicks('css', after_concentration_adjustment_deposit_into_Storage)  # 入库按钮
        self.sleep(0.5)
        self.clicks('css', storage_all_choice)  # 入库弹框全选按钮
        self.sleep(0.5)

        log.info(" 浓度调整后明细表，样本入库选择入样本盒")
        self.clicks('css', batch_paste_sample_box)  # 入库弹框选择样本盒按钮
        self.wait_loading()
        self.input('css', target_storage, '自动化测试用(勿删)')
        self.sleep(0.5)
        self.clicks('css', select_sample_box_search)
        self.wait_loading()
        self.clicks('css', select_sample_box_choice)  # 入库弹框选选择样本盒值，默认选择列表第一条数据
        self.clicks('css', select_sample_box_comfirm)  # 入库弹框选选择样本盒弹框，确认按钮
        self.sleep(1)

        log.info("上机明细表，样本入库录入盒内位置")
        taskstatus = self.get_text('css', after_concentration_detail_task_id)  # 获取任务单号
        lims_id = executeSql.test_select_limsdb(
            sj_detail_after_concentration_sql2.format(taskstatus[5:].strip()))  # 从数据库获取当前任务单号下样本lims号

        lims_list = [item[key] for item in lims_id for key in item]  # 把获取的lims号转换为一维列表
        nub_list = [str(i) for i in range(1, len(lims_list) + 1)]  # 根据lims样本数量，生成数字列表，作为盒内位置编号用
        res = [list(i) for i in zip(lims_list, nub_list)]  # 将lims号和数字编号转换为二维列表格式，写入Excel
        print(res)
        pandas_write_excel(res, position_in_box_path)  # 把样本号和盒内位置编号写入Excel模板

        data = xlrd.open_workbook(position_in_box_path)  # 从Excel读取模板样本号和盒内位置编号
        num_list = []
        for index in range(0, len(lims_list)):
            tables = data.sheets()[0]
            # allrows = tables.nrows
            vals = tables.row_values(index)
            imp_data = '\t'.join(map(str, vals))
            num_list.append(imp_data)
        print("\n".join(map(str, num_list)))
        pyperclip.copy("\n".join(map(str, num_list)))

        # 粘贴到【批量粘贴盒内位置】文本框
        self.clicks('css', batch_copy_BoxPosition)
        self.findelement('css', batch_copy_BoxPosition_input).send_keys(Keys.CONTROL, 'v')
        self.sleep(0.5)
        self.clicks('css', batch_copy_BoxPosition_comfirm)
        self.sleep(1)

        # 调用自定义截图方法
        Screenshot(self.driver).get_img("浓度调整后明细表点击入库按钮，在弹框中录入库位信息和盒内位置后点击下一步","样本入库成功")

        self.clicks('css', storage_next)
        self.wait_loading()

        self.executeJscript('document.getElementsByClassName("vxe-table--body-wrapper")[0].scrollLeft=4000')
        self.sleep(0.5)
        pageinfo = self.get_text('css', after_concentration_sumbit_status)  # 获取提交状态
        print(pageinfo)
        return pageinfo

    # 结果表导入FC质控结果表
    def import_fc_quality_control_result(self):
        """

        """
        log.info("上机结果表导入FC质控结果表")
        self.clicks('css', result_submit_result_btn)
        # 执行修改元素属性js
        self.executeJscript(
            "document.querySelector('.dialog-upload .el-dialog__body .upload-demo input').style.setProperty('display','block','important');")
        self.sleep(0.5)

        self.input('css', result_samples_number, sj_fc_quality_control_result)
        self.sleep(1)
        self.clicks('css', result_samples_upload)
        self.wait_loading()
        self.sleep(1)

    # 完成任务单
    def complete_task(self):
        """
        完成任务单
        """
        log.info(" 上机结果表,点击完成任务单")
        self.clicks('css', result_complete_task_btn)
        try:
            self.wait_loading()
            # 调用自定义截图方法
            Screenshot(self.driver).get_img("上机结果表点击完成任务单按钮","完成任务单成功，状态改为完成")
        except MyBaseFailure:
            self.refresh()
        self.wait_loading()

        taskstatus = self.get_text('css', task_status)
        print(taskstatus)
        return taskstatus

    # 上机任务列表根据上机批次号查询样本所在任务单
    # def serach_task(self):
    #     """
    #     首页面查询已完成的样本任务单
    #     """
    #     lims_id = read_excel_xlsx_list_col(all_path.wkdl_file_path, 0, '实验室号')
    #
    #     self.clicks('css', search)
    #     self.sleep(1)
    #     self.input('xpath', search_task_sample_num, lims_id[0][0])
    #     self.sleep(1)
    #     self.clicks('xpath', search_confirm)
    #     self.wait_loading()
    #     self.sleep(1)
    #     samples = self.findelements('xpath', sample_page_list)
    #     print(len(samples))
    #     return len(samples)
