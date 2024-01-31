# -*- coding: utf-8 -*-
# @Time    : 2022/08/01
# @Author  : guanzhong.zhou
# @File    : 样本接收页面功能封装

from common.editYaml import *
from common.DataBaseConnection import executeSql
from conf.all_path import qpcr_task_refresh_sql, sampledata_path, sampleprocessing_file_path, \
    hstq_file_path_dxk, hstq_file_path_mNGS
from conf.execute_sql_action import ybjs_sql2, ybjs_sql, ybjs_get_order_product_id, ybjs_set_product, \
    ybjs_get_order_project_id, ybjs_set_project
from pageobj.loginPage import LoginPage
from common.screenshot import Screenshot
from common.xlsx_excel import add_write_excel_xlsx
from conf.config import create_lab_excel, specimen_list
from PageElements.sampleRec_ele import *
from uitestframework.basepageTools import BasePage
from common.logs import log
from uitestframework.exceptionsTools import MyBaseFailure, TimeoutExceptions


class SampleReceivePage(BasePage):
    """
    样本接收类页面基础方法
    """
    globals()
    lg = LoginPage(BasePage)

    # 查询已存在订单号，对该订单号进行接样
    def search_order(self):
        """
        查询已存在订单号，对该订单号进行接样
        """
        order = get_order()  # 获取订单号
        log.info('接样页面点击搜索按钮')

        self.click_by_js('css', search_btn)
        self.sleep(0.5)
        log.info('搜索框录入订单号：%s' % order)
        self.input('css', order_numb, order)
        self.sleep(0.5)
        self.clicks('xpath', search_confirm)
        self.sleep(0.5)

        # 这里调用自定义截图方法
        Screenshot(self.driver).get_img("样本接收，在搜索弹框中，根据lims号搜索","搜索出订单模块已有订单")

        self.clicks('css', chioce_result)
        self.sleep(0.5)
        log.info('选中搜索出的订单，进入样本接收详情页面')
        self.clicks('css', edit_sample_order)
        # 存在进入接样明细缓冲过长，这里加个页面刷新
        try:
            self.wait_loading()
            # 调用自定义截图方法
        except MyBaseFailure:
            self.refresh()
        except TimeoutExceptions:
            self.refresh()
        self.wait_loading()

    # 样本接收详情页面，增加样本项目信息、检测产品、订单备注
    def add_order_project(self):
        """
        样本接收详情页面，增加样本项目信息、订单备注
        """
        # order = get_order()  # 获取订单号

        try:
            self.clicks('css',project_name_chioce)
            self.sleep(0.5)
            self.clicks('css',project_name_input)
            self.wait_loading()
            self.input('css',project_search_input,'J019')
            self.sleep(0.5)
            self.clicks('css',project_search_button)
            self.wait_loading()
            self.clicks('css',chioce_project_result)
            self.wait_loading()
            self.clicks('css',back_button)
            self.wait_loading()
            self.clicks('css',order_project_confirm)
            self.wait_loading()
            log.info('选择样本所属项目J019')
            # order_project_id = executeSql.test_select_limsdb(ybjs_get_order_project_id)#sql插入法
            # executeSql.test_insertByParam(
            #     ybjs_set_project.format(order_project_id[0]["order_project_id"] + 1, order))

            # log.info('选择样本所属检测产品')
            # order_product_id = executeSql.test_select_limsdb(ybjs_get_order_product_id)
            # executeSql.test_insertByParam(
            #     ybjs_set_product.format(order_product_id[0]["order_product_id"] + 1, order))
        except Exception as a:
            log.error("设置样本接样模块，订单项目错误:%s"%a)



    # 封装选择样本类型方法
    def set_sampleType(self):
        """
        封装选择样本类型方法,样本类型为，硕美抗凝血类型
        """
        self.click_by_js('css', all_chioce)
        self.sleep(0.5)
        # 样本类型选择按钮，元素定位
        self.click_by_js('css', sample_TypeName)
        self.sleep(1)

        self.click_by_js('xpath', chioce_search_result1)
        self.click_by_js('xpath', specimen_type_comfirm)
        self.sleep(1)

        # 保存
        self.clicks('css', save_btn)
        self.wait_loading()

    # 新增样本
    def sampleRec_addSample(self):
        """
        新增2种报告类型的样本,共40个：
        DNA*30
        迪迅康-基础(8)*10

        """
        log.info('添加2种报告类型的样本，')
        # specimen_list = {'DNA': 20, '迪迅康-基础(8)': 10,'DNA+耐药':5}
        total = specimen_list.values()  # config模块导入specimen_list
        n = 0
        for d in total:
            n += d
        # 新增样本，数量根据字典设置数
        s = 0
        while s < n:
            self.clicks('xpath', add_sample)
            print('新增第', s + 1, "条样本")
            self.wait_loading()
            self.clicks('css', get_report)
            s += 1
        self.sleep(1)
        self.click_by_js('css', all_chioce)
        log.info('新增样本生成报告任务，')
        self.clicks('xpath', create_report)
        self.wait_loading()

    def add_sampleReportType(self):
        """添加样本的报告类型"""

        def choice_reportType(sType):
            for i in range(tips, tips + num):  # 报告类型数量，循环选中多少数量的样本
                self.click_by_js('css', one_by_one_samplesReportStyle.format(i + 1))  # 先选中对应样本
                self.sleep(0.2)
                log.info('选中第{}条样本'.format(i + 1))
                self.sleep(0.5)
                self.clicks('xpath', choice_report_type.format(sType))
                self.clicks('css', choice_report_type_confirm)
                self.sleep(0.5)
            for i in range(tips, tips + num):  # b报告类型数量，循环取消选中多少数量的样本
                log.info('取消选中第{}条样本'.format(i + 1))
                self.click_by_js('css', one_by_one_samplesLay.format(i + 1))  # 先选中对应样本
                self.sleep(0.2)

        lists = self.findelements('css', all_samples)
        print("统计新增样本总数：",len(lists))
        try:
            tips = 0  # 计数器
            for sampleType, num in specimen_list.items():  # 从字典取值，样本类型以及对应的要添加的数量
                if sampleType == 'DNA':  # 跟据取值依次判断
                    choice_reportType(sampleType)
                elif sampleType == '迪迅康-基础(8)':
                    choice_reportType(sampleType)
                elif sampleType == 'DNA+耐药':
                    choice_reportType(sampleType)
                tips += num  # 每次循环取不同样本，所以各样本数量相加，取其排序下标，在页面中根据对应下标进行定位
        except Exception as a :
            log.error('设置样本类型错误%s'%a)
        self.sleep(1)

        # 这里调用自定义截图方法
        Screenshot(self.driver).get_img("样本接收明细表，点击新增样本按钮，保存","保存新增样本成功")

    # 生成实验流程
    def generate_laboratory_process(self):
        """
        样本接收-样本明细(未审核),选择样本并生成实验流程，对应的报告类型与实验流程关系.
        DNA——血液分离；
        迪迅康-基础(8)-迪讯康-基础+真菌(8+4)（直接提取）；
        specimen_list = {'DNA': 30, '迪迅康-基础(8)': 10}
        """

        def expProcess(experiment):
            """选择实验流程方法封装"""
            for i in range(tips, tips + num):  # 从所有存在于实验流程弹框中的样本，根据样本类型值，与列表取值进行比对
                j = i + 1
                self.clicks('css', one_by_one_chioce_sample.format(j))  # 先选中对应样本
            self.click_by_js('css', laboratory_process_temp_btn)  # 点击选择实验流程按钮
            self.sleep(1)
            eles = LibProcessVisible.format(experiment)  # 选中样本类型对应的实验流程
            self.clicks('xpath', eles)
            self.sleep(0.5)
            self.clicks('xpath', LibProcessVisible_btn)  # 选择实验流程弹框确认按钮
            self.sleep(0.5)
            # 把前面已完成操作的样本进行取消选中，接下来选中其它类型的样本
            for i in range(tips, tips + num):
                j = i + 1
                self.clicks('css', one_by_one_chioce_sample.format(j))
                self.sleep(0.5)

        log.info('选中样本生成实验流程')
        self.click_by_js('css', all_chioce)
        self.sleep(1)
        log.info('生成实验室号')
        self.click_by_js('xpath', generateLibNub)
        self.wait_loading()

        self.click_by_js('xpath', generateLibProcessVisible)  # 点击生成实验流程
        self.wait_loading()

        # 这里调用自定义截图方法
        Screenshot(self.driver).get_img("样本接收，点击生成实验流程按钮","打开实验流程弹框")

        tips = 0
        for sampleType, num in specimen_list.items():  # 取出样本类型及其数量
            log.info('生成{}报告类型样本的实验流程'.format(sampleType))
            if sampleType == 'DNA':
                expProcess('血液分离')
            elif sampleType == "迪迅康-基础(8)":
                expProcess('迪迅康-基础(8)（直接提取）')
            elif sampleType == "DNA+耐药":
                expProcess('mPCR-核酸提取')

            tips += num  # 每次循环取不同样本，所以各样本数量相加，取其排序下标，在页面中根据对应下标进行定位
        # 点击生成实验流程确认
        self.clicks('css', generatelaboratoryprocess_btn)
        self.wait_loading()
        self.sleep(2)

    # 把所有样本信息保存到Excel中
    def save_all_samples_excel(self):
        """
        把所有样本信息保存到Excel中
        """
        # 读取sql
        with open(qpcr_task_refresh_sql, 'r', encoding='utf-8', errors='ignore') as f:
            sa = f.read()
        executeSql.test_updateByParam(sa)
        print('执行数据库刷新视图<+_+>')
        order = get_order()  # 获取订单号
        get_info = self.select_sql(ybjs_sql2.format(order))  # 获取接样表中样本的sample_id,实验室号和报告类型
        rec_sample_info = [list(dct.values()) for dct in get_info]  # 获取的样本信息转为二维列表
        print(rec_sample_info)

        # 存入一个报告类型为DAN的样本的实验室号，作为mNGS样本生成复检任务时使用
        sample_lab_nub = self.get_text('css', one_by_one_samplesLay.format(1))
        print(sample_lab_nub)
        urlData = read_yaml(sampledata_path)
        urlData["sample_lab"] = sample_lab_nub
        save_yaml(sampledata_path, urlData)  # 写入模式获取的URL地址到yaml文件中
        print("写入后的临时文件内容：", urlData)

        create_lab_excel()  # 初始化所有存储Excel文件；

        log.info('把所有样本信息保存到Excel中')
        get_info = self.select_sql(ybjs_sql2.format(order))  # 获取接样表中样本的sample_id,实验室号和报告类型
        rec_sample_info = [list(dct.values()) for dct in get_info]  # 获取的样本信息转为二维列表
        print(rec_sample_info)
        log.info('获取的存储信息{}'.format(rec_sample_info))
        for sampleType in rec_sample_info:
            limsListValues = []
            if sampleType[2] == "DNA":
                limsListValues.append(sampleType)
                add_write_excel_xlsx(sampleprocessing_file_path, limsListValues)
            elif sampleType[2] == "迪迅康-基础(8)":
                limsListValues.append(sampleType)
                add_write_excel_xlsx(hstq_file_path_dxk, limsListValues)
            elif sampleType[2] == "DNA+耐药":
                limsListValues.append(sampleType)
                add_write_excel_xlsx(hstq_file_path_mNGS, limsListValues)
        self.sleep(2)

    # 录入样本包装量、质检结果和样本计量
    def input_sampleamt(self):
        """
        录入样本包装量和样本计量，并提交审核
        """
        log.info('录入样本包装量')
        self.click_by_js('css', all_chioce)
        self.sleep(0.5)
        self.click_by_js('css', sample_PkgAmt)
        self.sleep(0.5)
        self.input('css', sample_PkgAmt_input, 1)
        self.clicks('css', sample_PkgAmt_input_comfirm_btn)
        self.sleep(0.5)

        log.info('录入样本计量')
        self.click_by_js('css', sample_amt)
        self.sleep(0.5)
        self.input('css', sample_amt_input, 20)
        self.sleep(0.5)
        self.clicks('css', sample_amt_input_comfirm_btn)
        self.sleep(0.5)

        self.executeJscript('document.getElementsByClassName("vxe-table--body-wrapper")[0].scrollLeft=2500')
        log.info('选择质检结果')
        self.clicks('css', isQcPassDialogVisible)
        self.sleep(0.5)
        self.clicks('xpath', isQcPassDialogVisible_input)
        self.sleep(0.5)
        self.clicks('xpath', isQcPassDialogVisible_comfirm_btn)
        self.sleep(0.5)

        log.info('录入样本备注')
        order = get_order()
        self.updata_sql(ybjs_sql.format(order))

        log.info('录入样本基本数据后，样本信息保存')
        self.clicks('css', save_btn)
        self.wait_loading()
        self.refresh()

    # 点击批量提交审核
    def submit_sample_for_review(self):
        """
        点击批量提交审核
        """
        log.info('选中样本，点击批量提交审核')
        self.click_by_js('css', all_chioce)
        self.sleep(0.5)
        self.clicks('css', batch_submit_for_review)
        self.wait_loading()

    # 切换登录用户进行审核
    def batch_submit_for_review(self):
        """
        切换登录用户进行审核
        """
        log.info('点击页面退出登录按钮，切换登录用户')
        self.click_by_js('css', logout_btn)
        self.sleep(1)
        self.click_by_js('xpath', logout_choice)
        self.sleep(1)

    def get_save_info(self):
        """
        获取数据操作后，页面给出的提示信息语
        Submit successfully
        review successfully
        """
        log.info('获取页面提示信息')
        if self.isElementExists('css', save_info):
            return self.get_text('css', save_info)
        else:
            return None

    # 切换待审核页面，查看待审核样本，并进行样本审核
    def batch_review(self):
        """
        切换待审核页面，查看待审核样本，并进行样本审核
        """
        log.info('登录后，切换到样本待审核页面')
        self.click_by_js('css', review_pending)
        self.wait_loading()
        self.sleep(1)
        log.info('待审核页面选中待审核样本，并点击批量审核按钮')
        # 全选样本数据
        self.clicks('css', all_chioce)
        self.sleep(1)
        # 点击批量完成审核按钮
        self.clicks('css', batch_checked_for_review)
        self.sleep(0.5)

        # 这里调用自定义截图方法
        Screenshot(self.driver).get_img("样本接收，审核页面选中待审核样本，点击批量审核","打开审核弹框")

        # 弹出框录入用户密码
        self.input('xpath', password_inpt, 1)
        # 点击下一步
        self.clicks('xpath', next_step)
        # 弹出框录入审核理由
        self.input('xpath', review_remarks, '测试')
        # 点击提交
        self.clicks('xpath', review_confirm)
        self.wait_loading()
if __name__ == '__main__':
    cd=SampleReceivePage(BasePage)
    cd.save_all_samples_excel()