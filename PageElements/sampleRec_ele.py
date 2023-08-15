# -*- coding: utf-8 -*-
# @Time    : 2022/07/15
# @Author  : guanzhong.zhou
# @File    : 样本接收列表模块元素定位


"""
样本接收首页元素
"""
# 查询按钮，元素定位
search_btn = (
    '.filter-container .baseClass-btn-search')
# 查询框，输入订单号文本框，元素定位
order_numb = (
    '.sampleReceiveList-form-orderCode input')

# 搜索按钮，元素定位
search_confirm = (
    '//*[@class="el-dialog el-dialog--center dialog-search"]/descendant::button[child::span[text()="搜索"]]')

# 选中查询结果，默认选中第一条
chioce_result = (
    '.dialog-search .el-dialog__body .el-table__body-wrapper table tbody tr:nth-child(1)')

# 订单查询弹框，选中查询结果点击编辑接样单按钮，元素定位
edit_sample_order = (
    '.dialog-search .dialog-footer .baseClass-btn-dialog-edit')

'''
样本接收-订单信息
'''
# 检测产品选择弹框
# test_item = (
#     '.sampleOrderInfo .show-product-dialog')
#
# # 检测产品弹框，搜索文本录入
# product_input = (
#     '//*[@class="tableTree_info_search"]/descendant::input')
# # 检测产品弹框，搜索按钮
# product_search_btn = (
#     '//*[@class="tableTree_info_search"]/descendant::button')
#
# # 检测产品选择
# choice_product = (
#     '//*[@class="tableTree_select"]/descendant::td[descendant::span[text()="迪感康"]]')
#
# # 选择检测产品，关闭弹框，元素定位
# close_button = (
#     '.dialog-select-product .el-dialog__footer .baseClass-btn-go-back')

# 项目选择弹框
project_name_chioce = (
    '.sampleOrder button')

# 项目名称文本框，元素定位
project_name_input = (
    '.edit-order-drawer .demo-ruleForm >div:nth-child(1) > div > div')

#所属项目选择弹框
project_search_input='.selectProject-form-id input'

# 项目查询搜索按钮
project_search_button = (
    '.dialog-search .baseClass-btn-search')

# 选择查询结果，默认选择第一条
chioce_project_result = (
    '.multi-table-dialog .dialog-table .vxe-table--body-wrapper table tbody tr:nth-child(1)')
# 项目查询框，返回按钮
back_button = (
    '.multi-table-dialog .el-dialog__footer .baseClass-btn-back')

# 修改订单信息确认按钮
order_project_confirm = (
    '.edit-order-drawer .editOrder-drawer__content .dialog-footer button:nth-child(2)')

'''
样本接收-样本明细(未审核)
'''
# 保存按钮
save_btn = (
    '#pane-0 .switch-tab >div:nth-child(2) button:nth-child(4)')

# 样本类型选择按钮，元素定位
sample_TypeName = (
    '#pane-0 .sampleDetail_content .sampleType-header')

# 样本类型选项弹框，查询录入文本框
original_specimen_type = (
    '.multi-table-dialog .sampleType-form-formInline-query input')

# 样本类型选项弹框，查询按钮(isdisplayed判断)
search_type_button = (
    '.multi-table-dialog .el-dialog__body .baseClass-btn-search')

# 样本类型选项弹框，选择查询结果,精确查找，选择第一条
chioce_search_result = (
    '.multi-table-dialog .el-dialog__body .dialog-table .vxe-table--body-wrapper table tr:nth-child(1)')
chioce_search_result1='//*[@aria-label="样本类型"]/descendant::span[text()="硕美抗凝血"]'
# 样本类型选项弹框，选择确认
specimen_type_comfirm = (
    '//*[@aria-label="样本类型"]/descendant::span/button[2]')

# 编辑页面，全选样本标签，元素定位
all_chioce = (
    '#pane-0 .sampleDetail_content .vxe-table--fixed-left-wrapper .vxe-table--header-wrapper .vxe-checkbox--unchecked-icon')
# 审核页面，全选样本标签，元素定位
review_all_chioce = (
    '.sampleDetail .box-card:nth-child(1) .vxe-table--fixed-left-wrapper .vxe-header--row .vxe-checkbox--icon.vxe-checkbox--unchecked-icon')
# 添加样本按钮，元素定位
add_sample = (
    '//div[contains(text(),"添加样本")]')
# 添加样本后，提示生成报告任务
get_report = '.el-message-box__wrapper .el-message-box__btns button:nth-child(1)'

#生成报告
create_report='//div[contains(text(),"生成报告任务")]'

# 获取添加的样本（全部）
all_samples = (
    '#pane-0 .vxe-table--fixed-left-wrapper .sampleDetail-tableCol-sortIndex')
# 从全部样本中依次获取样本实验室号（单个）
one_by_one_samplesLay = (
    '#pane-0 .vxe-table--fixed-left-wrapper tbody tr:nth-child({}) .sampleDetail-tableCol-sampleIdLabCore')

# 从全部样本中依次获取样本报告类型（单个）
one_by_one_samplesReportStyle = (
    '#pane-0 .vxe-table--fixed-left-wrapper tr:nth-child({}) .sampleDetail-tableCol-productId ')

# 选择报告类型
choice_report_type = '//*[@class="el-dialog el-dialog--center dialog-report-style"]/descendant::tr[descendant::div[text()="{}"]]'

# 选择报告确认
choice_report_type_confirm = '.dialog-report-style .el-dialog__footer .baseClass-btn-confirm'

# 生成实验室号
generateLibNub = '//span[contains(text(),"生成实验室号")]'

# 获取单个样本的报告类型值
one_sample_type = (
    '.sampleDetail_content .vxe-table--fixed-left-wrapper .vxe-table--body-wrapper table tbody tr:nth-child({}) .sampleDetail-tableCol-productId')

# 获取单个lims号值
one_lims_num = (
    '.sampleDetail_content .tid_1 .vxe-table--main-wrapper .vxe-table--body-wrapper table tbody tr:nth-child({}) .sampleDetail-tableCol-sampleIdLims')

# 获取单个实验室号值
one_laboratory_num = (
    '.sampleDetail_content .tid_1 .vxe-table--fixed-left-wrapper .vxe-table--body-wrapper table tbody tr:nth-child({}) .sampleDetail-tableCol-sampleIdLabCore')

# 获取实验室号列所有值
laboratory_num = (
    '//*[@class="el-card box-card sample-receiving-module-card2 is-always-shadow"]/descendant::div[@class="vxe-table--fixed-left-wrapper"]/descendant::tbody/tr/td[3]')
# 获取lims号列所有值
lims_num = (
    '//*[@class="el-card box-card sample-receiving-module-card2 is-always-shadow"]/descendant::div[@class="vxe-table--main-wrapper"]/descendant::tbody/tr/td[4]')

# 生成实验流程弹框按钮，元素定位
generateLibProcessVisible = (
    '//div[contains(text(),"生成实验流程")]')

# 实验流程弹框中选中全部样本
template_sample_all = (
    '//*[@aria-label="实验流程配置/预设探针"]/descendant::tbody/tr')

# 获取实验流程弹框样本类型
template_sample_type = (
    '//div[@aria-label="实验流程配置/预设探针"]/descendant::tbody/tr[{}]/td[5]')

# 实验流程弹框中按个数选中样本
one_by_one_chioce_sample = (
    '.dialog-genertLibProcess .vxe-table--main-wrapper .vxe-table--body-wrapper table tbody tr:nth-child({}) .vxe-cell--checkbox')

# 实验流程模板按钮
laboratory_process_temp_btn = (
    '.dialog-genertLibProcess .el-dialog__body .baseClass-btn-nextStep')

# 获取所有实验流程对象，安照名称进行选定
LibProcessVisible = (
    '//*[@aria-label="实验流程模板"]/descendant::tr/td[descendant::span[contains(text(),"{}")]][1]')

# 选中实验流程后确认按钮
LibProcessVisible_btn = (
    '//*[@aria-label="实验流程模板"]/descendant::span/button[2]')

# 实验流程弹框全部流程生成后确认
generatelaboratoryprocess_btn = (
    '.dialog-genertLibProcess .baseClass-btn-genertLab')

# 样本包装量，元素定位
sample_PkgAmt = (
    '#pane-0 .sampleDetail_content .samplePkgAmt-header')

# 样本包装量文本录入
sample_PkgAmt_input = (
    '.dialog-input .inputDialog-form-inputValue input')

# 样本包装量确认按钮
sample_PkgAmt_input_comfirm_btn = (
    '.dialog-input .el-dialog__footer .baseClass-btn-confirm')

# 样本计量，元素定位
sample_amt = (
    '#pane-0 .sampleDetail_content .sampleAmt-header')

# 样本计量文本录入框
sample_amt_input = (
    '.dialog-input .inputDialog-form-inputValue input')

# 样本计量文本录入确认
sample_amt_input_comfirm_btn = (
    '.dialog-input .el-dialog__footer .baseClass-btn-confirm')

# 质检结果，元素定位
isQcPassDialogVisible = (
    '#pane-0 .sampleDetail_content .sampleQcLevel-header')

# 质检结果弹框选项
isQcPassDialogVisible_input = (
    '//*[@aria-label="质检结果"]/descendant::td[descendant::span[text()="合格"]]')

# 质检结果弹框选项确认
isQcPassDialogVisible_comfirm_btn = (
    '//*[@aria-label="质检结果"]/descendant::div[@class="el-dialog__footer"]/span/button[2]')






# 批量提交审核
batch_submit_for_review = '#pane-0 .switch-tab >div:nth-child(2) button:nth-child(6)'

# 批量完成审核
batch_checked_for_review = '#pane-0 .switch-tab >div:nth-child(2) button:nth-child(7)'

#退出登录按钮
logout_btn='.navbar .right-menu div:nth-child(2) span'

#退出登录
logout_choice='//ul/li[child::span[text()="退出登录"]]'



# 保存样本信息后，页面提示信息
save_info = (
    '.el-message.el-message--success')

# 切换待审核按钮
review_pending = (
    '#pane-0 .switch-tab .el-radio-group label:nth-child(2)')

# 批量审核，输入审核人账号密码，密码录入文本框，元素定位
password_inpt = (
    '//*[@aria-label="电子签名"]/descendant::input[2]')

# 批量审核，输入账号密码弹框，下一步按钮，元素定位
next_step = (
    '//*[@aria-label="电子签名"]/descendant::button[3]')

# 批量审核，审核理由文本输入框，元素定位
review_remarks = (
    '//*[@aria-label="审核备注"]/descendant::textarea')

# 批量审核，审核理由录入后确认按钮，元素定位
review_confirm = (
    '//*[@aria-label="审核备注"]/descendant::button[2]')
