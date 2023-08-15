# -*- coding: utf-8 -*-
# @Time    : 2022/09/21
# @Author  : guanzhong.zhou
# @File    : 报告上传及QPCR复检任务生成模块页面方法封装
import openpyxl
from common.editYaml import *
from common.screenshot import Screenshot
from PageElements.report_upload_ele import *
from conf.all_path import sampledata_path, excel_doc_file_path, sjNubForQpcrFile
from uitestframework.basepageTools import BasePage
from uitestframework.exceptionsTools import NotFoundError
from common.logs import log


class ReportUploadPage(BasePage):
    """报告-基本信息任务分配模块页面基础方法封装"""
    # 定义类变量
    tips = None
    # 上传报告文件需要包含患者姓名和订单号，分别取出保存为文件名



    def search_by_order(self):

        """
        根据订单号查询报告列表
        :return: allOrder_len
        """
        order = get_order()  # 订单Excel获取订单号
        log.info("按订单号搜索:{}".format(order))
        self.input('css', order_num, order)
        self.sleep(1)
        self.click_by_js('css', search_btn)  # 点击查询
        self.wait_loading()
        samples = self.isElementExists('css', all_samples)
        if samples:
            allOrder = self.findelements('css', all_samples)  # 获取查询结果数量
            allOrder_len = len(allOrder)
        else:
            allOrder_len = 0
        return allOrder_len

    def tip_report_qpcr_sample(self):
        """标记qpcr复检样本"""
        # 从yaml文件读取接样模块存入的原始样本实验室号，用来在报告模块选择对应的样本任务
        sampleLab = read_yaml(sampledata_path)
        lab_nub = sampleLab['sample_lab'][:10]
        log.info('从yaml文件读取接样模块存入的原始样本实验室号：{}'.format(lab_nub))

        # 循环找出与接样时写入的原始样本实验室号一致的样本
        log.info("标记qpcr复检样本")
        sample = self.isElementExists('css', all_samples)
        if sample:
            samples = self.findelements('css', all_samples)
            self.sleep(0.5)
            for i in range(0, len(samples)):
                sample_lab = self.get_text('css', one_sample_lab.format(i + 1))
                ReportUploadPage.tips = i + 1
                if sample_lab[:10] == lab_nub:
                    self.sleep(0.5)
                    self.click_by_js('css', one_sample_lab.format(i + 1))
                    self.wait_loading()

                    # 存入上机号，在 复检任务界面取出作查询用
                    sj_nub = self.get_text('css', sj_group_nub)
                    print("取出上机号：", sj_nub)
                    sjdata = read_yaml(sjNubForQpcrFile)
                    sjdata["sj_nub"] = sj_nub[:10]
                    save_yaml(sjNubForQpcrFile, sjdata)  # 写入模式获取的上机样本号到yaml文件中

                    self.clicks('css', sample_report_tab)
                    self.wait_loading()
                    self.clicks('css', close_table)
                    break
        else:
            raise NotFoundError

    def reportStyle(self):
        """选择报告形式"""
        log.info("选择报告形式")
        print(ReportUploadPage.tips)
        print(report_style_form.format(ReportUploadPage.tips))

        self.click_by_js('css', report_style_form.format(ReportUploadPage.tips))
        self.sleep(1)
        self.click_by_js('css', report_style_btn.format(ReportUploadPage.tips))
        self.sleep(0.5)
        self.clicks('xpath', report_style_choice)
        self.wait_loading()

    def upload_report_file(self):
        """上传报告文件"""
        testdata = read_yaml(order_medical_info_path)
        name = testdata['username']  # 读取病历模块患者姓名
        order = get_order()  # 读取订单号
        # 创建上传报告文件
        wb = openpyxl.Workbook()
        ws = wb.active
        ws.title = 'test_sheet1'
        ws.cell(row=1, column=2).value = 1
        file_name = "报告上传文件_" + str(name) + "_" + str(order)  # 新建Excel文件，以读取的患者姓名和订单号为文件名
        print(file_name)
        wb.save(excel_doc_file_path + '/' + '{}.xlsx'.format(file_name))  # 保存文件
        report_file_path = os.path.abspath(excel_doc_file_path + '/' + '{}.xlsx'.format(file_name))

        log.info("上传报告文件")
        self.click_by_js('css', report_file_edit.format(ReportUploadPage.tips))  # 点击报告文件编辑按钮
        self.wait_loading()
        # 上传报告文件
        # 执行JS，修改上传控件样式，由不显示变为显示，以便上传文件
        self.executeJscript(
            "document.querySelector('.dialog-upload-file div:nth-child(2) .el-upload input').style.setProperty('display','block','important');")

        self.input('css', report_upload_btn, report_file_path)  # 用send_keys方法上传文件
        self.clicks('css', info_confirm1)
        self.sleep(0.5)
        self.clicks('css', info_confirm2)
        report_info = self.get_save_info()
        log.info("上传报告文件{}".format(report_info))
        self.sleep(1)
        return report_info

    def upload_other_file(self):
        # 上传其他文件
        log.info("上传其他文件")
        self.executeJscript(
            "document.querySelector('.dialog-upload-file div:nth-child(4) .el-upload input').style.setProperty('display','block','important');")
        # 创建doc类型的其他文件
        with open(excel_doc_file_path + '/' + '自动化测试其他文件上传.doc', 'w', encoding='utf-8') as f:
            f.write('自动化测试解读文件上传')
        other_file_path = os.path.abspath(excel_doc_file_path + '/' + '自动化测试其他文件上传.doc')
        self.input('css', other_upload_btn, other_file_path)  # 用send_keys方法上传文件
        other_report_info = self.get_save_info()
        # 这里调用自定义截图方法
        Screenshot(self.driver).get_img("报告上传，上传其他文件")
        self.sleep(1)
        self.clicks('css', report_upload_comfirm)
        self.wait_loading()
        print("上传其它文件", other_report_info)
        return other_report_info

    def upload_decode_file(self):
        # 上传解读文件
        testdata = read_yaml(order_medical_info_path)
        name = testdata['username']  # 读取病历模块患者姓名
        order = get_order()  # 读取订单号
        file_name = "报告上传文件_" + str(name) + "_" + str(order)  # 新建Excel文件，以读取的患者姓名和订单号为文件名
        #上传解读文件
        self.executeJscript(
            "document.querySelector('.dialog-upload-file div:nth-child(3) .el-upload input').style.setProperty('display','block','important');")
        # 创建TXT类型的解读文件
        with open(excel_doc_file_path + '/' + '{}_解读文件.txt'.format(file_name), 'w', encoding='utf-8') as f:
            f.write('自动化测试解读文件上传')
        decode_file_path = os.path.abspath(excel_doc_file_path + '/' + '{}_解读文件.txt'.format(file_name))
        self.input('css', decode_upload_btn, decode_file_path)  # 用send_keys方法上传文件
        if self.isDisplayed('xpath', '//body/div[4]'):
            self.clicks('css', info_confirm2)
        decode_info = self.get_save_info()
        log.info("上传解读文件{}".format(decode_info))
        # 这里调用自定义截图方法
        Screenshot(self.driver).get_img("报告上传，上传解读文件")
        self.sleep(1)
        return decode_info

    def create_qpcrReinspect_task(self):
        """
        生成QPCR复检任务
        """
        log.info("新建QPCR复检任务")
        self.click_by_js('css', qpcr_task_add_btn.format(1))
        self.wait_loading()
        log.info("新建QPCR复检任务,选择当日批次")
        self.click_by_js('css', report_belong_input)
        self.sleep(0.5)
        self.click_by_js('xpath', report_belong_choice)

        log.info("新建QPCR复检任务,选择样本要求")
        self.clicks('css', sample_style)
        self.sleep(0.5)
        self.clicks('xpath', sample_style_choice)

        log.info("新建QPCR复检任务,选择复检任务类型")
        self.clicks('css', qpcr_task_type)
        self.sleep(0.5)
        self.clicks('xpath', qpcr_task_type_choice1)


        log.info("新建QPCR复检任务,添加菌种")
        self.clicks('css', add_qpcr_basbacteria_btn)
        self.clicks('xpath', add_qpcr_basbacteria)

        # 这里调用自定义截图方法
        Screenshot(self.driver).get_img("新建QPCR复检任务,添加菌种")
        self.clicks('css', add_qpcr_basbacteria_choice)  # 添加菌种弹框确认按钮
        self.clicks('css', create_qpcr_task_btn)  # 添加菌种弹框确认按钮
        self.wait_loading()

    def complete_report_task(self):
        """
        完成报告任务
        """
        log.info("完成报告任务")
        self.sleep(1)
        print(report_task_complete.format(ReportUploadPage.tips))

        self.click_by_js('css', report_task_complete.format(ReportUploadPage.tips))
        self.wait_loading()
        self.sleep(1)
        pageinfo = self.get_text('css', report_task_complete.format(1))
        print('报告任务单状态', pageinfo)
        return pageinfo

    def get_save_info(self):
        """
        获取数据操作后，页面给出的提示信息语
        Submit successfully
        review successfully
        """
        log.info('获取页面提示信息')
        if self.isElementExists('xpath', page_info):
            return self.get_text('xpath', page_info)
        else:
            return None
