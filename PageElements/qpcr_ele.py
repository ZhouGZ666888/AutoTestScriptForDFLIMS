# -*- coding: utf-8 -*-
# @Time    : 2022/09/14
# @Author  : guanzhong.zhou
# @File    : qpcr页面元素定位
# -*-*************************************************************************************-*-


"""
QPCR首页元素定位
"""
# 编辑按钮
edit_btn = (
    '.filter-container .baseClass-btn-edit')
# 搜索lims号录入文本
search_lims_sample_num = (
    '.search-list > form > div > div:nth-child(2) input')
# 搜索按钮
search_btn = (
    '.search-list .baseClass-btn-dialog-search')
# 新增按钮
add_sample_QPCR_task = (
    '.table-list .table-header .baseClass-btn-add')
##页面列表样本
sample_page_list = (
    '.sample_receive_detail .vxe-table--main-wrapper .vxe-table--body-wrapper table tr')
# -*-*************************************************************************************-*-


"""
QPCR待选表元素定位
"""
# 任务类型下拉选择框
task_type = '.select-task-type input'
# 任务类型下拉选择
task_type_choice = '//*[@class="el-select-dropdown el-popper task-type-unique"]/descendant::span[contains(text(),"{}")]'

# 选择sop下拉框
task_sop = '.select-task-sopId input'
# 选项sop下拉选择
task_sop_choice = '.task-type-sopId .el-select-dropdown__list >ul:nth-child(1) .el-select-group li:nth-child(1)'

# 核对lims样本号按钮
check_lims_sample_num = (
    '//span[contains(text(),"核对LIMS样本号")]')

# 核对样本号文本录入框
check_lims_sample_number_textarea = (
    '.dialog-match .el-dialog__body textarea')

# 核对lims样本号确认按钮，元素定位
check_lims_sample_number_confirm = (
    '//*[@aria-label="核对LIMS样本号"]/descendant::button[4]')

# 待选列表全选按钮
all_choice = (
    '.vxe-table--main-wrapper .vxe-table--header-wrapper .vxe-header--row .vxe-checkbox--icon.vxe-checkbox--unchecked-icon')

# 加入选中&保存按钮，元素定位
addSelect_or_save_btn = (
    '.head-list .commonTaskDetailNew-commonTaskDetailBtn-submit')

# 进入明细表按钮，元素定位
enter_detail_list_btn = (
    '.head-list .commonTaskDetailNew-commonTaskDetailBtn-goSchedule')

# 页面成功提示信息
page_success_info = (
    '//*[@class="el-message el-message--success"]/descendant::p')

# 页面失败提示信息
page_failed_info = (
    '//*[@class="el-message el-message--success"]')

"""
qpcr明细表元素定位
"""
# 列表全选按钮
detail_all_choice = (
    '.createTask_content_table .vxe-table--fixed-left-wrapper .vxe-header--row .vxe-checkbox--icon.vxe-checkbox--unchecked-icon')

# 自动计算按钮
auto_complete = '.button-list .btn-first'

# 提交按钮
sumbit_btn = '//span[contains(text(),"提交")]'

# 提交弹框确认按钮
submit_comfirm = (
    '.dialog-commit .dialog-footer .baseClass-btn-confirm')

# 添加NC
add_nc_pc = '//span[contains(text(),"添加NC&PC")]'
# *********************************入库****************************************
# 入库按钮
deposit_into_storage = (
    '//span[text()="入库"]')

# 入库弹框全选按钮
storage_all_choice = '.deposit-drawer .deposit-drawer__content .drawer-content .show--head .vxe-table--main-wrapper .vxe-table--header-wrapper table tr .vxe-checkbox--unchecked-icon'

# 入库弹框选择样本盒按钮
batch_paste_sample_box = '.deposit-drawer .button-add button:nth-child(2)'

# 入库弹框选择样本盒弹框target storage 搜索文本录入框
target_storage = '.deposit-drawer form > div:nth-child(2) >div:nth-child(2) input'

# 入库弹框选择样本盒弹框t搜索按钮
select_sample_box_search = '.deposit-drawer form > div:nth-child(1) > div:nth-child(3) button'

# 入库弹框选选择样本盒值，默认选择列表第一条数据
select_sample_box_choice = '.deposit-drawer .drawer-content >div:nth-child(2) .el-table__body-wrapper table tbody tr:nth-child(1)'

# 入库弹框选择样本盒弹框，确认按钮
select_sample_box_comfirm = '//*[@aria-label="选择样本盒"]/section/div/div[2]/descendant::button[2]'

# 批量粘贴盒内位置
batch_copy_BoxPosition = '.deposit-drawer .button-add button:nth-child(4)'

# 批量粘贴盒内位置文本录入
batch_copy_BoxPosition_input = '//*[@aria-label="批量粘贴盒内位置"]/descendant::textarea'

# 批量粘贴盒内位置确认按钮
batch_copy_BoxPosition_comfirm = '//*[@aria-label="批量粘贴盒内位置"]/div[3]/descendant::button[2]'

# 入库弹框确认按钮
storage_next = '//*[@aria-label="填写入库信息"]/section/div/div[2]/descendant::button[2]'

# 明细表保存按钮
detail_save_btn = '.createTask_content .baseClass-btn-save'

# 进入结果表按钮
go_result = '.head-list button:nth-child(2)'

# 明细表任务单号
detail_task_id = (
    '.head-list .header_test')
# 提交状态文本定位
submit_status = (
    '.createTask_content_table .vxe-table--main-wrapper .vxe-table--body-wrapper tbody tr:nth-child(1) td:nth-child(12)')

# ************QPCR结果表元素定位**************
result_all_choice = '.createTask_content_table .vxe-table--fixed-left-wrapper .vxe-header--row .vxe-checkbox--icon.vxe-checkbox--unchecked-icon'

# 导出复孔信息
export_out_btn = '//span[text()="导出复孔信息"]'

# 导入复孔信息
export_in_btn = '//span[text()="导入复孔结果"]'

# 导入复孔信息录入文本框
export_in_input = '.dialog-info-import textarea'

# 导入复孔信息文本框确认
export_in_input_confirm = '.dialog-info-import .el-dialog__footer .baseClass-btn-confirm'

# 自动判读
sumbit_auto_Complete = '//span[text()="自动判读"]'

# 提交完成
result_sumbit_btn = '//span[text()="提交完成"]'

# 结果表样本提交状态
sample_status = '.createTask_content_table .vxe-table--main-wrapper .vxe-table--body-wrapper table tbody tr:nth-child(1) td:nth-child({})'

# 返回上一步
go_back = '//span[text()="返回明细表"]'
# 返回上一步确认
go_back_confirm = '.dialog-back .el-dialog__footer .baseClass-btn-next'

# 保存结果
result_save = '//span[text()="保存结果"]'

# 完成任务单
result_complete_task_btn = '//span[text()="完成任务单"]'

# 任务单状态
result_task_status = (
    '.head-list .header_status')
