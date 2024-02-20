# -*- coding: utf-8 -*-
# @Time    : 2021/11/25
# @Author  : guanzhou.zhou
# 流转表方法功能封装
from common.editYaml import get_order
from common.screenshot import Screenshot
from common.DataBaseConnection import executeSql
from PageElements.sample_workflow_ele import *
from uitestframework.basepageTools import BasePage

from common.logs import log


class SampleWorkflowPage(BasePage):
    """
    以下是针对单样本流转表的一些列操作，详情见方法说明
    """

    def workflow_search_by_sampleid(self, sample_lims_id):
        """
        将在单样本流转表搜索样本的方法提取出来
        """
        log.info("点击样本筛选按钮")
        self.clicks('xpath', workflow_samplesearch)
        self.sleep(0.5)
        log.info("点击LIMS号输入框")
        self.clicks('xpath', workflow_samplesearch_sample)

        log.info("右侧弹框打开后，点击输入框")

        self.sleep(0.5)
        log.info("输入框输入指定LIMS号")
        self.clicks('xpath', workflow_samplesearch_sample_value)
        self.input('xpath', workflow_samplesearch_sample_value, sample_lims_id)

        # 这里调用自定义截图方法
        Screenshot(self.driver).get_img("流转表根据lims号进行搜索","成功检索出样本")

        self.sleep(0.5)
        log.info("点击确定按钮")
        self.clicks('xpath', sampleid_confirm)
        self.sleep(0.5)
        log.info("点击最外层的确认按钮")
        self.clicks('xpath', search_sample_confirm)
        log.info("流转表LIMS号检索成功")
        self.wait_loading()

    def workflow_search_by_samplelab(self, sample_lab):
        """
        将在单样本流转表搜索样本的方法提取出来
        """
        log.info("点击样本筛选按钮")
        self.clicks('xpath', workflow_samplesearch)
        self.sleep(0.5)
        log.info("点击实验室样本号输入框")
        self.clicks('css', workflow_samplesearch_samplelab)
        self.sleep(0.5)
        log.info("右侧弹框打开后，点击输入框")
        self.clicks('css', workflow_samplesearch_samplelab_value)
        self.sleep(0.5)
        log.info("输入框输入指定实验室号")
        self.clicks('css', workflow_samplesearch_samplelab_value)
        self.input('css', workflow_samplesearch_samplelab_value, sample_lab)

        # 这里调用自定义截图方法
        Screenshot(self.driver).get_img("流转表根据lims号进行搜索","成功检索出样本")

        self.sleep(0.5)
        log.info("点击确定按钮")
        self.clicks('css', samplelab_confirm)
        self.sleep(0.5)
        log.info("点击最外层的确认按钮")
        self.click_by_js('xpath', search_sample_confirm)
        log.info("流转表LIMS号检索成功")
        self.wait_loading()

    def workflow_search_order(self):
        """
        在流转表搜索订单号
        """
        order = get_order()  # 读出样本审核通过对应的订单号

        log.info("点击样本筛选按钮")
        self.clicks('xpath', workflow_samplesearch)
        self.sleep(0.5)
        log.info("点击订单号输入框")
        self.clicks('xpath', workflow_samplesearch_order)
        self.sleep(0.5)
        log.info("右侧弹框打开后，点击输入框")
        self.clicks('xpath', workflow_samplesearch_order_value)
        self.sleep(0.5)
        log.info("输入框输入指定订单号:%s"%order)
        self.clicks('xpath', workflow_samplesearch_order_value)
        self.sleep(1)
        self.input('xpath', workflow_samplesearch_order_value, order)
        self.sleep(0.5)
        log.info("点击确定按钮")
        self.clicks('xpath', order_confirm)
        self.sleep(0.5)
        log.info("点击最外层的确认按钮")
        self.click_by_js('xpath', search_order_confirm)
        log.info("流转表订单号检索成功")
        self.wait_loading()

    def workflow_search_samplelimsid(self, sql):
        """
        在流转表搜索订单号
        """
        ret = executeSql.test_select_limsdb(sql)[0]  # 我们只取sql查询结果的第一个
        print("查询结果为:" + str(ret))
        if len(ret) == 0:
            sample_lims_id = 'null'
            print("当前系统中没有可以操作的数据，请检查")
        else:
            sample_lims_id = ret['sampleidlims']  # lims号
            print("lims号为:" + str(sample_lims_id))
            self.sleep(1)

            self.workflow_search_by_sampleid(sample_lims_id)  # 调用封装的流转表搜索样本的方法

        return sample_lims_id

    def workflow_search_samplelab(self, sql):
        """
        在流转表搜索订单号
        """
        ret = executeSql.test_select_limsdb(sql)[0]  # 我们只取sql查询结果的第一个
        print("查询结果为:" + str(ret))
        sample_lab = (ret['sampleidlab'].split('-'))[0]  # 实验室号第一部分
        print("实验室号第一部分为:" + str(sample_lab))
        self.sleep(1)
        self.refresh()
        self.workflow_search_by_samplelab(sample_lab)  # 调用封装的流转表搜索样本的方法

    def workflow_fg(self, sql):
        """
        在流转表分管操作，以在样本处理节点分管为例
        """
        sample_lims_id = self.workflow_search_samplelimsid(sql)  # 将sql查询的结果拿到
        print(sample_lims_id[0])
        self.sleep(0.5)
        if sample_lims_id == 'null':
            print('样本处理节点分管操作，当前系统没有可用的样本')
        else:
            log.info("全选处理节点样本")
            self.clicks('xpath', get_ybcl_allcheckbox)
            self.sleep(1)
            log.info("点击【产物分管】")
            if get_ybcl_allcheckbox:
                print("元素可见，点击按钮")
                self.clicks('xpath', sample_fg_button)
                self.wait_loading()
                log.info("选择样本数量，点击下一步")
                self.clicks('xpath', sample_fg_num)
                self.sleep(1)
                log.info("全选样本")
                self.clicks('xpath', sample_fg_allcheckbox)
                self.sleep(0.5)
                log.info("点击最后步骤按钮")
                self.clicks('xpath', sample_fg_laststep)
                self.sleep(1)
                log.info("选择样最后步骤")
                self.clicks('xpath', sample_fg_laststep_value)
                self.sleep(1)
                log.info("点击确定")
                self.clicks('css', sample_fg_laststep_confirm)
                self.sleep(1)
                log.info("点击修改项目信息")
                self.clicks('xpath', sample_fg_modify_project)
                self.sleep(1)
                log.info("勾选项目复选框")
                self.clicks('xpath', sample_fg_modify_project_value)
                self.sleep(1)
                log.info("点击确定")
                self.clicks('css', sample_fg_modify_project_confrim)
                self.sleep(1)
                log.info("点击分管弹框最外层的确定按钮")
                self.clicks('xpath', sample_fg_confirm)
                self.sleep(1)
                log.info("分管成功")
                self.wait_loading()
                self.refresh()
            else:
                print("元素不可见")

    def workflow_ck(self, sql):
        """
        在流转表对数据，出库
        """

        get_sample_lims_id = executeSql.test_select_limsdb(sql)[0]  # 将sql查询的结果拿到
        print("从实验中心读取到的接样节点入库样本为：" + str(get_sample_lims_id))
        self.sleep(0.5)

        if not get_sample_lims_id:
            print('当前系统没有可用的样本')
        else:
            self.workflow_search_by_sampleid(get_sample_lims_id['sample_id_lims'])  # 调用封装的流转表搜索样本的方法
            self.sleep(1)
            log.info("全选接样节点样本")
            self.clicks('xpath', get_ybjs_allcheckbox)
            self.sleep(1)
            log.info("点击【样本出库】")
            self.clicks('xpath', sample_ck_button)
            self.sleep(0.5)

            # 这里调用自定义截图方法
            Screenshot(self.driver).get_img("在流转表选中接样节点的数据点击出库按钮","打开出库弹框")

            log.info("全选样本")
            self.clicks('xpath', sample_ck_allcheckbox)
            self.sleep(0.5)
            log.info("点击【实验流程模板】")
            self.clicks('xpath', sample_ck_piplane)
            self.sleep(0.5)
            log.info("弹框中选择模板")
            self.clicks('xpath', sample_ck_piplane_value)
            self.sleep(0.5)
            log.info("点击确定")
            self.clicks('xpath', sample_ck_piplane_confirm)
            self.sleep(0.5)
            log.info("选择[是否保留原项目信息]")
            self.clicks('css', sample_ck_project)
            self.sleep(0.5)
            log.info("选择[是]")
            self.clicks('xpath', sample_ck_project_value)
            self.sleep(0.5)

            log.info("点击添加优化项目")
            self.clicks('css', add_project)
            self.sleep(0.5)
            log.info("选择页面中第一条优化项目")
            self.clicks('css', add_project_choice)
            self.sleep(0.5)
            log.info("选择优化项目后，点击确定")
            self.clicks('css', add_project_choice_confirm)
            self.sleep(0.5)

            log.info("点击【生成实验流程】按钮")
            self.clicks('xpath', sample_ck_confirm)
            self.sleep(0.5)
            log.info("填写出库理由")
            self.clicks('xpath', sample_ck_reason)
            self.sleep(0.5)
            self.input('xpath', sample_ck_reason, '国旗测试出库')
            self.sleep(0.5)
            Screenshot(self.driver).get_img("在出库弹框中录入出库信息", "录入出库信息成功")
            # 获取当前窗口句柄
            now_handle = self.get_current_window_handle()
            print('获取当前窗口句柄', now_handle)

            log.info("点击确定按钮")
            self.clicks('xpath', sample_ck_reason_confirm)
            self.wait_loading()

            # 获取所有窗口句柄
            all_handles = self.get_all_windows()
            for handle in all_handles:
                if handle != now_handle:
                    # 切换到新窗口句柄，即新打开的流转表页面
                    self.switch_to_window(handle)
                    self.sleep(0.5)
                    # 关闭新窗口句柄，关闭流转表页面
                    self.close()
            self.sleep(0.5)
            # 切换到旧窗口句柄，回到原页面
            self.switch_to_window(now_handle)
            self.refresh()

    def workflow_update_wkgj_wkfj(self, libtype, now):
        """
        在流转表对数据，做修改【建库+富集】信息的操作
        """

        # -------------------修改建库信息-------------------
        self.workflow_search_order()  # 调用封装的流转表搜索样本的方法
        self.sleep(0.5)
        log.info("全选建库节点样本")
        self.clicks('xpath', get_wkgj_allcheckbox)
        self.sleep(0.5)
        log.info("点击【修改建库信息】")
        self.clicks('xpath', update_wkgj_data_button)
        self.sleep(0.5)
        log.info("全选样本")
        self.clicks('css', update_wkgj_data_allcheckbox)
        self.sleep(0.5)
        log.info("点击【批量建库类型】")
        self.clicks('css', update_wkgj_data_libtype)
        self.wait_loading()
        log.info("选择指定建库类型")
        self.clicks('xpath', update_wkgj_data_libtype_value.format(libtype))
        self.sleep(0.5)
        log.info("点击【修改建库备注】")
        self.clicks('xpath', update_wkgj_data_remarks)
        self.sleep(0.5)
        log.info("输入框内输入备注信息")
        self.clicks('xpath', update_wkgj_data_remarks_value)
        self.sleep(0.5)
        self.input('xpath', update_wkgj_data_remarks_value, '董国奇修改建库备注信息')
        self.sleep(0.5)
        log.info("点击确定按钮")
        self.clicks('xpath', update_wkgj_data_remarks_confirm)
        self.sleep(0.5)
        log.info("点击保存修改按钮")
        self.clicks('xpath', update_wkgj_data_confirm)
        self.sleep(0.5)
        # -------------------修改富集信息-------------------
        log.info("点击【取消选中】按钮，开始修改富集信息环节")
        self.click_by_js('css', cancel_all_check)
        self.sleep(1)
        log.info("勾选富集样本复选框")
        self.click_by_js('css', get_wkfj_allcheckbox)
        self.sleep(0.5)
        log.info("点击【修改富集信息】按钮")
        self.clicks('xpath', update_wkfj_data_button)
        self.wait_loading()
        log.info("先选择一条样本设置预设探针")
        self.clicks('css',choice_one_sample)
        self.clicks('xpath', preinstallProbe_btn)
        self.sleep(0.5)
        self.clicks('css',preinstallProbe_choice)
        self.sleep(0.5)
        self.clicks('css',preinstallProbe_confirm)
        self.sleep(0.5)
        Screenshot(self.driver).get_img("修改富集信息为样本设置预设探针", "设置预设探针成功")

        log.info("全选修改富集信息样本复选框")
        self.click_by_js('css', update_wkfj_data_allcheckbox)
        self.sleep(0.5)
        log.info("点击【批量修改通量】")
        self.clicks('xpath', update_wkfj_thought)
        self.sleep(0.5)
        log.info("输入数据")
        self.clicks('xpath', update_wkfj_thought_value)
        self.sleep(0.5)
        self.input('xpath', update_wkfj_thought_value, '7.14')
        self.sleep(0.5)
        log.info("点击确定")
        self.clicks('xpath', update_wkfj_thought_confirm)
        self.sleep(0.5)
        log.info("点击【批量修改通量单位】按钮")
        self.clicks('css', update_wkfj_thought_unit)
        self.sleep(0.5)
        log.info("选择单位M")
        self.clicks('xpath', update_wkfj_thought_unit_value)
        self.sleep(0.5)
        log.info("点击填写富集备注按钮")
        self.clicks('xpath', update_wkfj_remarks_button)
        self.sleep(0.5)
        self.input('xpath', update_wkfj_remarks_value, '国旗测试富集备注')
        self.sleep(0.5)
        log.info("点击确定按钮")
        self.clicks('xpath', update_wkfj_remarks_reason_confirm)
        self.sleep(0.5)
        log.info("点击批量修改预计富集日期按钮")
        self.clicks('xpath', update_wkfj_pretime)
        self.sleep(1)
        log.info("点击输入框")
        self.clicks('xpath', update_wkfj_pretime_value)
        self.sleep(0.5)
        log.info("输入富集日期")
        self.input('xpath', update_wkfj_pretime_value, now)
        self.sleep(0.5)
        log.info("点击确定")
        self.clicks('xpath', update_wkfj_pretime_confirm)
        self.sleep(0.5)

        log.info("点击最外层的确认按钮")
        self.click_by_js('xpath', update_wkfj_confirm)
