# -*- coding: utf-8 -*-
# @Time    : 2021/11/25
# @Author  : guanzhou.zhou
# @File    : 流转表元素定位
# -*-*************************************************************************************-*-

# ===================流转表的元素如下===========================

"""
流转表搜索页的元素---订单号搜索
"""
# 列表页，样本筛选按钮
workflow_samplesearch = (
    '//*[@class="el-button baseClass-btn-search el-button--primary el-button--small"]')

# 搜索弹框中，点击订单输入框
workflow_samplesearch_order = (
    '//*[@class="click-orderCode-visible el-input el-input--medium el-input-group el-input-group--prepend"]//input')

# 点击订单输入框后，右侧弹出的输入框
workflow_samplesearch_order_value = (
    '//*[@class="order-code-input el-textarea el-input--medium"]//textarea')

# 点击确定按钮
order_confirm = (
    '//*[@class="el-drawer__body" and descendant::div[@class="order-code-input el-textarea el-input--medium"]]//button[@class="el-button baseClass-btn-jdrawer-confirm el-button--primary el-button--medium"]')

# 点击最外层的确认按钮
search_order_confirm = '//*[@class="el-button baseClass-btn-confirm el-button--primary el-button--medium"]//span[text()="确认"]'

"""
流转表搜索页的元素---样本号搜索
"""
# 点击【Lims样本号】输入框
workflow_samplesearch_sample = '//*[@class="click-sampleIdLims-visible el-input el-input--medium el-input-group el-input-group--prepend"]//input'

# 点击实验室样本号输入框
workflow_samplesearch_samplelab = '.click-sampleIdLab-visible input'

# 点击订单输入框后，右侧弹出的输入框
workflow_samplesearch_sample_value = (
    '//*[@class="sampleId-lims-input el-textarea el-input--medium"]//textarea')

# 点击实验室样本号输入框后，右侧弹出的输入框
workflow_samplesearch_samplelab_value = '.sampleId-lab-input textarea'

# 点击确定按钮
sampleid_confirm = (
    '//*[@class="el-drawer__body" and descendant::div[@class="sampleId-lims-input el-textarea el-input--medium"]]//button[@class="el-button baseClass-btn-jdrawer-confirm el-button--primary el-button--medium"]')

samplelab_confirm = '.baseClass-btn-jdrawer-confirm'

# 点击最外层的确认按钮
search_sample_confirm = (
    '//*[@class="el-button baseClass-btn-confirm el-button--primary el-button--medium"]//span[text()="确认"]')

"""
流转表搜索页的元素---实验室号搜索
"""
# 点击【Lims样本号】输入框
workflow_labcoresearch_sample = (
    '//*[@class="click-sampleIdLab-visible el-input el-input--medium el-input-group el-input-group--prepend"]//input')

# 点击订单输入框后，右侧弹出的输入框
workflow_labcoresearch_sample_value = (
    '//*[@class="sampleId-lab-textarea el-textarea el-input--medium"]//textarea')

# 点击确定按钮
labcore_confirm = (
    '//*[@class="el-drawer__body" and descendant::div[@class="sampleId-lab-input el-textarea el-input--medium"]]//button[@class="el-button baseClass-btn-jdrawer-confirm el-button--primary el-button--medium"]')

# 点击最外层的确认按钮
search_labcore_confirm = (
    '//*[@class="el-button baseClass-btn-confirm el-button--primary el-button--medium"]//span[text()="确认"]')

"""
流转表列表页的元素---分管操作
"""
# 勾选样本处理全选复选框
get_ybcl_allcheckbox = (
    '//*[@class="el-checkbox__inner"]//following-sibling::input[@value="样本处理"]/preceding-sibling::span')

# 点击【产物分管】按钮
sample_fg_button = (
    '//*[@class="el-button baseClass-btn-0-show-sample-separation el-button--primary el-button--small"]')

# 默认是下一步，即分1管
sample_fg_num = (
    '//*[@class="el-button baseClass-btn-next el-button--primary el-button--medium"]')

# 点击全选样本的复选框
sample_fg_allcheckbox = (
    '//*[@class="vxe-cell--title"]//span[@class="vxe-checkbox--icon vxe-checkbox--unchecked-icon"]')

# 点击最后步骤按钮
sample_fg_laststep = (
    '//*[@class="el-button btn_chlid baseClass-btn-last-step el-button--primary el-button--mini"]')

# 弹框中选择样本处理
sample_fg_laststep_value = (
    '//*[@class="el-table__body-wrapper is-scrolling-none"]//div[text()="样本处理"]')

# 点击确定
sample_fg_laststep_confirm = (
    '.dialog-last-step .el-dialog__footer .baseClass-btn-confirm')

# 点击【修改后项目信息】
sample_fg_modify_project = (
    '//*[@class="el-button border_size baseClass-btn-open-project el-button--primary el-button--mini"]')

# 弹框里勾选项目号复选框
sample_fg_modify_project_value = (
    '//*[@class="vxe-header--row"]//span[@class="vxe-checkbox--icon vxe-checkbox--unchecked-icon"]')

# 选完项目，点击确定按钮
sample_fg_modify_project_confrim = (
    '.dialog-select-project .el-dialog__footer .baseClass-btn-confirm')

# 点击最外层的确定按钮
sample_fg_confirm = (
    '//*[@aria-label="样本分管"]//button[@class="el-button baseClass-btn-confirm el-button--primary el-button--medium"]')

"""
流转表列表页的元素---出库操作
"""
# 勾选样本接收全选复选框
get_ybjs_allcheckbox = (
    '//*[@class="el-checkbox__inner"]//following-sibling::input[@value="样本接收"]/preceding-sibling::span')

# 点击【样本出库】按钮
sample_ck_button = (
    '//*[@class="el-button baseClass-btn-0-show-sample-outbound el-button--primary el-button--small"]')

# 弹框中，全选复选框
sample_ck_allcheckbox = (
    '//*[@class="vxe-cell--title"]//span[@class="vxe-checkbox--icon vxe-checkbox--unchecked-icon"]')

# 点击【实验流程模板】
sample_ck_piplane = ('//*[@class="el-button baseClass-btn-next-step el-button--primary el-button--mini"]')
# 选择核酸提取模板
sample_ck_piplane_value = ('//*[@class="el-table__body-wrapper is-scrolling-none"]//descendant::div[text()="核酸提取"]')
# 点击确定
sample_ck_piplane_confirm = (
    '//*[@aria-label="实验流程模板"]//button[@class="el-button baseClass-btn-confirm el-button--primary el-button--medium"]')
# 选择[是否保留原项目信息]
sample_ck_project = (' .baseClass-btn-keep-original-project-info')
# 选择是
sample_ck_project_value = ('//*[@class="el-dropdown-menu el-popper el-dropdown-menu--medium"]//li[text()="保留"]')
# 点击【生成实验流程】按钮
sample_ck_confirm = ('//*[@class="el-button baseClass-btn-genertlab el-button--primary el-button--mini"]')
# 填写出库理由
sample_ck_reason = ('//*[@class="task-form-ruleForm-reasonOfWithdraw el-textarea el-input--medium"]/textarea')
# 点击确定按钮
sample_ck_reason_confirm = (
    '//*[@class="el-dialog dialog-out-storage"]//button[@class="el-button baseClass-btn-confirm el-button--primary el-button--medium"]')

# 添加优化项目
add_project = '.baseClass-btn-new-project'

# 选择优化项目
add_project_choice = '.dialog-optimization-project .el-dialog__body .vxe-table--body-wrapper table tbody tr:nth-child(1)'

# 选择优化项目确认
add_project_choice_confirm = '.dialog-optimization-project .el-dialog__footer .baseClass-btn-confirm'

"""
流转表列表页的元素---修改建库信息操作
"""
# 全选建库节点按钮
get_wkgj_allcheckbox = (
    '//*[@class="el-checkbox__input"]//following-sibling::input[@value="文库构建"]/preceding-sibling::span')

# 点击【修改建库信息】按钮
update_wkgj_data_button = (
    '//*[@class="el-button baseClass-btn-0-show-edit-libconstruction-type el-button--primary el-button--small"]')

# 全选样本复选框
update_wkgj_data_allcheckbox = (
    '.vxe-header--row .vxe-cell--title .vxe-checkbox--unchecked-icon')

# 点击【批量建库类型】按钮
update_wkgj_data_libtype = (
    ' .el-dialog--center .baseClass-btn-libconstruction')

# 下拉框选择建库类型
update_wkgj_data_libtype_value = (
    '//*[@class="el-dropdown-menu el-popper el-dropdown-menu--medium"]//li[@class="el-dropdown-menu__item" and text()="{}"]')

# 点击【修改建库备注】
update_wkgj_data_remarks = (
    '//*[@class="el-button border_size baseClass-btn-show-remarks el-button--primary el-button--mini"]')

# 点击输入框内
update_wkgj_data_remarks_value = (
    '//*[@class="editlibconstructionType-form-textarea el-textarea el-input--medium"]//textarea')

# 点击确定按钮
update_wkgj_data_remarks_confirm = (
    '//*[@class="el-dialog el-dialog--center dialog-visible1" and @aria-label="批量修改建库备注"]//button[@class="el-button baseClass-btn-confirm el-button--primary el-button--medium"]')

# 点击最外层弹框的确定按钮
update_wkgj_data_confirm = (
    '//*[@aria-label="修改建库信息"]//button[@class="el-button baseClass-btn-save el-button--primary el-button--medium"]')

"""
流转表列表页的元素---修改富集信息操作
"""
# 取消刚刚选择的建库节点
cancel_all_check = (
    '.baseClass-pageName-libconstruction > span')

# 全选富集节点的复选框
get_wkfj_allcheckbox = (
    '.baseClass-pageName-pooling > span:nth-child(1)')

# 点击【修改富集信息】按钮
update_wkfj_data_button = (
    '//*[@class="el-button baseClass-btn-0-show-edit-probe el-button--primary el-button--small"]')

# 选择一条样本
choice_one_sample='.dialog-probe .el-dialog__body .vxe-table--fixed-left-wrapper .vxe-table--body-wrapper table tbody tr:nth-child(1) td:nth-child(2)'

#批量修改预设探针按钮
preinstallProbe_btn= '//span[text()="批量修改预设探针"]'

#选择探针弹框，第一条探针数据
preinstallProbe_choice='.batch-edit-probe .el-dialog__body .el-table__body-wrapper tbody tr:nth-child(1)'

#选择探针弹框,确定按钮
preinstallProbe_confirm='.batch-edit-probe .el-dialog__footer .baseClass-btn-confirm'

# 全选样本复选框
update_wkfj_data_allcheckbox = (
    '.vxe-table--fixed-left-wrapper .vxe-table--header-wrapper .vxe-checkbox--unchecked-icon')

# 点击【批量修改通量】
update_wkfj_thought = (
    '//*[@class="el-button btn_chlid baseClass-btn-show-throughput el-button--primary el-button--mini"]')

# 输入数据
update_wkfj_thought_value = (
    '//*[@class="editprobe-form-sampleFlux el-input el-input--medium el-input-group el-input-group--prepend el-input--suffix"]/input')

# 点击确定按钮
update_wkfj_thought_confirm = (
    '//*[@aria-label="批量修改预设通量"]//button[@class="el-button baseClass-btn-confirm el-button--primary el-button--small"]')

# 点击【批量修改通量单位】按钮
update_wkfj_thought_unit = (' .baseClass-btn-throughput-unit')
# 选择单位M
update_wkfj_thought_unit_value = ('//*[@class="el-dropdown-menu__item" and text()="M"]')
# 点击填写富集备注按钮
update_wkfj_remarks_button = (
    '//*[@class="el-button btn_chlid baseClass-btn-show-dialogVisible1 el-button--primary el-button--mini"]')
# 输入框内填写备注信息
update_wkfj_remarks_value = ('//*[@class="editprobe-form-textarea el-textarea el-input--medium"]//textarea')
# 点击确定
update_wkfj_remarks_reason_confirm = ('//*[@class="el-dialog el-dialog--center dialog-visible1" and '
                                      '@aria-label="批量修改富集备注"]//button[@class="el-button baseClass-btn-confirm el-button--primary el-button--medium"]')
# 点击批量修改预计富集日期按钮
update_wkfj_pretime = (
    '//*[@class="el-button btn_chlid baseClass-btn-show-dialogVisible2 el-button--primary el-button--mini"]')
# 点击输入框
update_wkfj_pretime_value = (
    '//*[@class="el-input el-input--medium el-input-group el-input-group--prepend el-input--suffix"]//input')
# 点击确定按钮
update_wkfj_pretime_confirm = (
    '//*[@aria-label="批量修改预计富集日期"]//button[@class="el-button baseClass-btn-confirm el-button--primary el-button--medium"]')

# 点击保存全部按钮
update_wkfj_confirm = (
    '//*[@class="el-button baseClass-btn-save el-button--primary el-button--mini"]/span[text()="保存全部"]')

# 出库新建实验流程打开新的流转表页面，功能提示信息
close_btn = '//body/div[2]/descendant::span[contains(text(),"关闭")]'
