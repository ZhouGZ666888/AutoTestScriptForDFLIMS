from common.logs import log
from uitestframework.basepageTools import BasePage
from uitestframework.exceptionsTools import ElementNotFound
from retrying import retry

class EnterTab(BasePage):
    """
    系统左侧的点击tab进入页面的方法封装，减少维护成本
    """

    def enter_unresolve_job(self):
        """点击待办任务tab封装"""
        try:
            self.clicks('xpath', "//span[contains(text(),'待办任务')]")
        except Exception as e:
            log.warning("无法进入待办任务列表")
            raise ElementNotFound(e)

    def enter_crmorder(self):
        """点击病历和订单tab封装"""
        try:
            self.clicks('xpath', "//span[contains(text(),'病历和订单')]")
        except Exception as e:
            log.warning("无法进入病历和订单")
            raise ElementNotFound(e)

    def enter_crm(self):
        """点击病历tab封装"""
        try:
            self.clicks('xpath', "//span[contains(text(),'电子病历列表')]")
            self.wait_loading()
            self.sleep(0.5)
        except Exception as e:
            log.warning("无法进入电子病历列表")
            raise ElementNotFound(e)

    def enter_order(self):
        """点击订单tab封装"""
        try:
            self.clicks('xpath', "//span[contains(text(),'订单列表')]")
            self.wait_loading()
        except Exception as e:
            log.warning("无法进入订单列表")
            raise ElementNotFound(e)

    def enter_payment(self):
        """点击款项核对tab封装"""
        try:
            self.clicks('xpath', "//span[contains(text(),'款项核对')]")
            self.wait_loading()
        except Exception as e:
            log.warning("无法进入款项核对")
            raise ElementNotFound(e)

    def enter_samplereceive(self):
        """点击接样列表tab封装"""
        try:
            self.clicks('xpath', "//span[contains(text(),'样本接收列表')]")
            self.wait_loading()
        except Exception as e:
            log.warning("无法进入样本接收列表")
            raise ElementNotFound(e)

    def enter_workflow(self):
        """点击流转表tab封装"""
        try:
            self.clicks('xpath', "//span[contains(text(),'流转表')]")
            self.wait_loading()
        except Exception as e:
            log.warning("无法进入流转表")
            raise ElementNotFound(e)

    def enter_single_workflow(self):
        """点击单样本流转表tab封装 """
        try:
            self.clicks('xpath', "//span[contains(text(),'单样本流转表')]")
            self.wait_loading()
        except Exception as e:
            log.warning("无法进入单样本流转表")
            raise ElementNotFound(e)

    def enter_FJ_workflow(self):
        """ 点击富集混合样本tab封装 """
        try:
            self.clicks('xpath', "//span[contains(text(),'富集混合样本')]")
            self.wait_loading()
        except Exception as e:
            log.warning("无法进入富集混合样本列表")
            raise ElementNotFound(e)

    def enter_ZC_workflow(self):
        """点击定量混合样本tab封装"""
        try:
            self.clicks('xpath', "//span[contains(text(),'定量混合样本')]")
            self.wait_loading()
        except Exception as e:
            log.warning("无法进入定量混合样本列表")
            raise ElementNotFound(e)

    def enter_test_center(self):
        """点击实验中心tab封装 """
        try:
            self.clicks('xpath', "//span[contains(text(),'实验中心')]")
        except Exception as e:
            log.warning("无法进入实验中心")
            raise ElementNotFound(e)

    def enter_preparation(self):
        """点击样本处理tab封装"""
        try:
            self.clicks('xpath', "//span[contains(text(),'样本处理')]")
            self.wait_loading()

        except Exception as e:
            log.warning("无法进入样本处理列表")
            raise ElementNotFound(e)

    def enter_extraction(self):
        """点击核酸提取tab封装 """
        try:
            self.clicks('xpath', "//span[contains(text(),'核酸提取')]")
            self.wait_loading()
        except Exception as e:
            log.warning("无法进入核酸提取列表")
            raise ElementNotFound(e)

    def enter_mPCR(self):
        """点击mPCRtab封装 """
        try:
            self.clicks('xpath', "//*[@class='el-scrollbar']/descendant::span[contains(text(),'MPCR')]")
            self.wait_loading()
        except Exception as e:
            log.warning("无法进入mPCR列表")
            raise ElementNotFound(e)

    def enter_libconstruction(self):
        """点击文库构建tab封装"""
        try:
            self.clicks('xpath', "//span[contains(text(),'文库构建')]")
            self.wait_loading()
        except Exception as e:
            log.warning("无法进入文库构建列表")
            raise ElementNotFound(e)

    def enter_pooling(self):
        """点击文库富集tab封装"""
        try:
            self.clicks('xpath', "//span[contains(text(),'Pooling')]")
            self.wait_loading()
        except Exception as e:
            log.warning("无法进入文库富集列表")
            raise ElementNotFound(e)

    def enter_sequencing(self):
        """点击上机tab封装"""
        try:
            self.clicks('xpath', "//span[contains(text(),'上机测序')]")
            self.wait_loading()
        except Exception as e:
            log.warning("无法进入上机列表")
            raise ElementNotFound(e)

    @retry(stop_max_attempt_number=2)
    def enter_samplesheet(self):
        """点击在线samplesheet封装"""
        try:
            self.clicks('xpath', "//span[contains(text(),'在线samplesheet')]")
            self.wait_loading()
        except Exception as e:
            log.warning("无法进入在线samplesheet")
            raise ElementNotFound(e)


    @retry(stop_max_attempt_number=2)
    def enter_storage_center(self):
        """点击样本库位管理tab封装"""
        try:
            self.clicks('xpath', "//span[contains(text(),'样本库管理')]")
            self.sleep(1)
        except Exception as e:
            log.warning("无法进入样本库管理")
            raise ElementNotFound(e)

    def enter_deposit(self):
        """点击样本入库tab封装"""
        try:
            self.clicks('xpath', "//span[contains(text(),'样本入库')]")
            self.wait_loading()
        except Exception as e:
            log.warning("无法进入样本入库列表")
            raise ElementNotFound(e)

    def enter_withdraw(self):
        """点击样本出库tab封装"""
        try:
            self.clicks('xpath', "//span[contains(text(),'样本出库')]")
            self.wait_loading()
        except Exception as e:
            log.warning("无法进入样本出库列表")
            raise ElementNotFound(e)

    def enter_transfer(self):
        """点击样本/盒移位tab封装"""
        try:
            self.clicks('xpath', "//span[contains(text(),'盒移位')]")
            self.wait_loading()
            self.sleep(1)
        except Exception as e:
            log.warning("无法进入样本/盒移位列表")
            raise ElementNotFound(e)

    def enter_storage_user(self):
        """点击库位管理tab封装"""
        try:
            self.clicks('xpath',
                        "//*[@class='el-menu el-menu--inline']//descendant::li//descendant::span[contains(text(),'库位管理')]")
            self.wait_loading()
        except Exception as e:
            log.warning("无法进入库位管理列表")
            raise ElementNotFound(e)

    def enter_box_user(self):
        """点击样本盒管理tab封装"""
        try:
            self.clicks('xpath', "//span[contains(text(),'样本盒管理')]")
            self.wait_loading()
        except Exception as e:
            log.warning("无法进入样本盒管理列表")
            raise ElementNotFound(e)

    def enter_send_back(self):
        """点击样本外送tab封装"""
        try:
            self.clicks('xpath', "//span[contains(text(),'样本外送')]")
            self.wait_loading()
        except Exception as e:
            log.warning("无法进入样本外送列表")
            raise ElementNotFound(e)

    def enter_sop_center(self):
        """点击SOP主数据tab封装"""
        try:
            self.clicks('xpath', "//span[contains(text(),'SOP主数据')]")
            self.wait_loading()
        except Exception as e:
            log.warning("无法进入SOP主数据列表")
            raise ElementNotFound(e)

    def enter_qpcr_recheck(self):
        """点击QPCR复检任务tab封装 """
        try:
            self.clicks('xpath',
                        "//span[contains(text(),'QPCR复检') and parent::li[preceding-sibling::li[child::span[contains(text(),'上机')]]]]")
            self.wait_loading()

        except Exception as e:
            log.warning("无法进入QPCR复检")
            raise ElementNotFound(e)

    def enter_report_center(self):
        """点击报告任务列表tab封装"""
        try:
            self.clicks('xpath', "//span[contains(text(),'报告任务列表')]")
            self.sleep(0.5)
        except Exception as e:
            log.warning("无法进入报告任务列表")
            raise ElementNotFound(e)

    def enter_qpcr_reinspectionTask(self):
        """点击QPCR复检任务tab封装"""
        try:
            self.clicks('xpath', "//span[contains(text(),'QPCR复检任务')]")
            self.wait_loading()

        except Exception as e:
            log.warning("无法进入QPCR复检任务")
            raise ElementNotFound(e)

    def enter_report_upload(self):
        """点击报告上传tab封装"""
        try:
            self.clicks('xpath', "//span[contains(text(),'报告上传')]")
            self.wait_loading()

        except Exception as e:
            log.warning("无法进入报告上传列表")
            raise ElementNotFound(e)

    def report_writing_task_assignment(self):
        """报告编写任务分配"""
        try:
            self.clicks('xpath', "//span[contains(text(),'报告编写任务分配')]")
            self.wait_loading()

        except Exception as e:
            log.warning("无法进入报告编写任务分配")
            raise ElementNotFound(e)

    def enter_report_send(self):
        """ 点击报告发送tab封装"""
        try:
            self.clicks('xpath', "//span[contains(text(),'迪飞报告发送')]")
            self.wait_loading()

        except Exception as e:
            log.warning("无法进入报告发送列表")
            raise ElementNotFound(e)

    def enter_report_sequencing_sample(self):
        """点击上机样本匹配tab封装"""
        try:
            self.clicks('xpath', "//span[contains(text(),'上机样本匹配')]")
            self.wait_loading()

        except Exception as e:
            log.warning("无法进入上机样本匹配列表")
            raise ElementNotFound(e)

    @retry(stop_max_attempt_number=2)
    def enter_update_sample(self):
        """点击数据修改tab封装"""
        try:
            self.clicks('xpath',
                        '//*[@class="el-scrollbar__view"]/ul[@class="el-menu"]/li/span[contains(text(),"数据修改") and parent::li[following-sibling::li]]')
            self.wait_loading()

        except Exception as e:
            log.warning("无法进入数据修改列表")
            raise ElementNotFound(e)

    @retry(stop_max_attempt_number=2)
    def enter_select_data(self):
        """点击信息查询tab封装"""
        try:
            self.clicks('xpath', "//span[contains(text(),'信息查询')]")
            self.wait_loading()
        except Exception as e:
            log.warning("无法进入信息查询")
            raise ElementNotFound(e)

    def sample_project_info_change(self):
        """点击样本项目信息修改tab封装"""
        try:
            self.clicks('xpath', "//span[contains(text(),'样本项目信息修改')]")
            self.wait_loading()
        except Exception as e:
            log.warning("无法进入样本项目信息修改")
            raise ElementNotFound(e)

    def sample_message_notice(self):
        """点击样本消息通知"""
        try:
            self.clicks('xpath', "//span[contains(text(),'样本通知消息列表')]")
            self.wait_loading()
        except Exception as e:
            log.warning("无法进入样本通知消息列表")
            raise ElementNotFound(e)


eb = EnterTab(BasePage)
