# -*- coding: utf-8 -*-
# @Time    : 2022/010/10
# @Author  : guanzhong.zhou
# @File    : 样本外送模块页面功能封装
from common.editYaml import read_yaml, save_yaml
from common.screenshot import Screenshot
from common.xlsx_excel import read_excel_col
from PageElements.sample_outsend_ele import *
from conf.all_path import wkfj_file_path, functionpageURL_path, sampleOutDataFile, hstq_file_path_mNGS
from uitestframework.basepageTools import BasePage
from common.logs import log


class SampleOutSendPage(BasePage):
    """
    样本外送页面方法封装
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

    # 新建样本外送任务
    def add_sample_outsend_task(self):
        """
        新建样本外送任务
        """
        # 这里调用自定义截图方法
        Screenshot(self.driver).get_img("点击导航栏进入样本外送列表","进入模块成功")

        log.info('点击新建按钮新建样本外送任务，进入样本外详情页面')
        self.clicks('css', add_task)
        self.wait_loading()

        self.sleep(0.5)

        log.info('外送申请单详情页，选择外送类型：样本回寄')
        self.click_by_js('css', outsend_type)
        self.sleep(0.5)
        self.clicks('xpath', outsend_type_choice.format('样本回寄'))
        self.sleep(0.5)
        log.info('外送申请单详情页，选择接收方，患者家属')
        self.click_by_js('css', recipient)
        self.sleep(0.5)
        self.clicks('xpath', recipient_choice)
        self.sleep(0.5)
        log.info('外送申请单详情页，录入外送目的地地址')
        self.input('css', sendAddress, '测试地址')
        self.sleep(0.5)
        log.info('外送申请单详情页选择寄送方式，快递')
        self.click_by_js('css', sendMethod)
        self.sleep(0.5)
        self.clicks('xpath', sendMethod_choice)
        self.sleep(0.5)
        log.info('外送申请单详情页，录入跟踪信息')
        self.input('css', trackingInfo, '测试追踪消息')
        self.sleep(0.5)
        log.info('外送申请单详情页，选择关联项目J022')
        self.clicks('css', projectId)
        self.sleep(0.5)
        self.clicks('xpath', projectId_choice)
        self.sleep(0.5)
        log.info('外送申请单详情页，选择审核人')
        self.clicks('css', lastAuditedBy_btn)
        self.sleep(0.5)
        self.input('css', lastAuditedBy, '董国奇')
        self.click_by_js('xpath', lastAuditedBy_choice)
        self.sleep(0.5)

        log.info('保存样本外送任申请单')
        self.clicks('css', save_btn)
        self.wait_loading()
        self.sleep(0.5)

        # 这里调用自定义截图方法
        Screenshot(self.driver).get_img("样本外送明细详情页录入外送申请单信息，点击保存","保存外送申请单成功 ")

    # 待选样本表选择样本至明细表
    def add_sample_to_task(self):
        """
        样本外送审核操作
        """
        log.info('从实验模块-取核酸提取结果表样本数据当做外送样本')
        lims_nub = read_excel_col(hstq_file_path_mNGS, 'lims号')

        lims_id_str = "\n".join(lims_nub[:2])  # 取出Excel表中前两个样本，拼接成字符串录入到检索文本中
        print(lims_id_str)

        log.info("点击样本筛选按钮，录入样本lims号，筛选出外送样本")
        self.clicks('css', samplefilter)
        self.sleep(0.5)

        log.info("进入样本筛选弹框,录入lism号")
        self.clicks('css', sampleIdLims_input)
        self.input('css', lims_input, lims_id_str)
        self.sleep(0.5)
        if self.isDisplayed('css', lims_input_comfirm):
            self.clicks('css', lims_input_comfirm)

        log.info("录入筛选条件后，点击确认，进行搜索")
        self.clicks('css', detail_search_comfirm)
        self.wait_loading()
        self.sleep(0.5)

        log.info("选择筛选结果，添加至明细表")
        self.clicks('css', detail_all_choice)
        self.clicks('css', add_detail)
        self.wait_loading()

        log.info("进入明细表")
        self.clicks('css', to_detail)
        self.wait_loading()
        self.sleep(0.5)

    # 样本外送明细表处理、提交审核
    def outsend_detail_edit(self):
        """
        样本外送明细表处理、提交审核
        """
        urldata = read_yaml(functionpageURL_path)

        log.info("样本外送明细表全选样本")
        self.clicks('css', outsend_detail_all_choice)
        self.sleep(0.5)

        log.info('外送样本明细表是否全样外送选择：全部外送')
        self.moved_to_element('css', is_allOutsend)
        self.sleep(0.5)
        self.clicks('xpath', is_allOutsend_choice)
        self.sleep(0.5)
        Screenshot(self.driver).get_img("样本外送明细表添加样本，是否全样外送选择：全部外送","外送样本处理成功")
        log.info('提交审核')
        self.clicks('css', submit_btn)
        self.wait_loading()
        self.sleep(0.5)

        url = self.get_current_url()  # 获取当前页面URL地址
        print('获取的URL地址', url)
        urldata["url"] = url
        save_yaml(functionpageURL_path, urldata)  # 写入模式获取的URL地址到yaml文件中
        print("写入后的URL地址", urldata)



        task_status = self.get_text('css', detail_task_status)
        return task_status[3:].strip()

    # 部门审核人角色(样本外送)审核任务单
    def task_for_review(self):
        """
        部门审核人角色审核任务单
        """
        # 进入代办页面

        self.clicks('css', outsendsample_tab)
        self.sleep(0.5)
        log.info("进入样本外送待办tab页,点击进入按钮")
        self.clicks('css', outsend_review_btn)
        self.sleep(0.5)

        log.info("待办页面进入样本外送页面，弹出新页面，切换至新页面，并关闭旧页面")
        now_handle = self.get_current_window_handle()
        all_handles = self.get_all_windows()
        for handle in all_handles:
            if handle != now_handle:
                # 切换到新窗口句柄，即新打开的页面
                self.close()
                self.switch_to_window(handle)
        self.sleep(0.5)

        # 这里调用自定义截图方法
        Screenshot(self.driver).get_img("待办tab页进入样本外送明细审核页面","进入样本外送审核页面成功")

        log.info('点击完成审核')
        self.clicks('css', finishAudit_btn)
        self.wait_loading()
        Screenshot(self.driver).get_img("对外送样本进行审核样本外送审核","审核样本成功，样本状态为取样中")


        application_num = self.get_text('css', detail_task_id)
        application_status1 = self.get_text('css', detail_task_status)  # 取样中
        log.info('获取审核后的申请单号:{}和状态:{}'.format(application_status1,application_num))

        log.info('点击完成取样确认')
        self.clicks('css', check_btn)
        self.wait_loading()
        application_status2 = self.get_text('css', detail_task_status)  # 待寄送

        log.info('将获取的申请单号写入临时文件')
        application_num = application_num[5:].strip()
        urldata = read_yaml(sampleOutDataFile)
        urldata["sample_outsend_task_id"] = application_num
        save_yaml(sampleOutDataFile, urldata)  # 写入模式获取的URL地址到yaml文件中
        print("写入后的临时文件内容：", urldata)

        return application_status1[3:].strip(), application_status2[3:].strip()

    # 审核完成后，进行取样确认操作
    def sample_check(self):
        """
        在审核完成后，有权限用户进行取样确认操作
        """
        if self.isElementExists('css', outsendsample_tab):
            self.clicks('css', outsendsample_tab)

        log.info("进入样本外送待办tab页,点击进入按钮")
        self.clicks('css', outsend_review_btn)
        self.wait_loading()

        log.info("待办页面进入样本外送页面，弹出新页面，切换至新页面，并关闭旧页面")
        now_handle = self.get_current_window_handle()
        all_handles = self.get_all_windows()
        for handle in all_handles:
            if handle != now_handle:
                # 切换到新窗口句柄，即新打开的页面
                self.close()
                self.switch_to_window(handle)
                self.wait_loading()
        self.sleep(0.5)

        log.info('完成寄送操作')
        self.clicks('css', sendfinish_btn)
        self.wait_loading()
        self.sleep(0.5)

        log.info('获取完成寄送后的申请单状态')
        application_status = self.get_text('css', detail_task_status)  # 完成
        print(application_status)
        return application_status[3:].strip()

    # 样本外送申请列表检索
    def search_task(self):
        """
         样本外送申请列表检索申请单
        """
        log.info('根据申请单号检索')
        self.clicks('css', search_btn)
        self.sleep(0.5)

        urldata = read_yaml(sampleOutDataFile)
        application_num = urldata["sample_outsend_task_id"]

        self.input('css', search_lims_task_id, application_num)
        self.clicks('css', search_confirm)
        self.wait_loading()

        eles = self.findelements('xpath', sample_page_list)
        return eles

    def batch_submit_for_review(self):
        """
        切换登录用户进行审核
        """
        log.info('点击页面退出登录按钮，切换登录用户')
        self.click_by_js('css', logout_btn)
        self.sleep(1)
        self.click_by_js('xpath', logout_choice)
        self.sleep(1)
