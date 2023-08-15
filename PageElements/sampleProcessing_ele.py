# -*- coding: utf-8 -*-
# @Time    : 2021/11/25
# @Author  : guanzhong.zhou
# @File    : 样本处理元素定位
# -*-*************************************************************************************-*-
"""
样本处理首页列表元素定位
"""
# 搜索按钮
search = (
    '.filter-container .baseClass-btn-search')
# 搜索弹框lims号录入文本
search_lims_sample_num = (
    '//input[preceding-sibling::div[text()="LIMS样本号"]]')
# 搜索弹框确认
search_confirm = (
    '//*[@aria-label="搜索"]/descendant::button[4]')
# 新增按钮
add_sample_process_task = (
    '.filter-container .baseClass-btn-add')
##页面列表样本
sample_page_list = (
    '//div[@class="sample_receive_detail"]/descendant::tbody/tr')
# -*-*************************************************************************************-*-


'''
待选表元素定位
'''
# 选择任务类型点击下拉框
task_type = (
    '.select-task-type input')
# 样本类型选择下拉值，默认第一条
task_type_choice = (
    '.task-type-unique .el-select-dropdown__list li:nth-child(1)')
# 选择sop下拉框
select_sop = (
    '.select-sop-type input')
# 选择sop下拉值
select_sop_choice = (
    '.sopId-unique .el-select-group li:nth-child(1)')

# 核对lims样本号按钮
check_lims_sample_num = (
    '.createTask_content_choose .commonTaskDetail-btn-judgeLims')
# 核对样本号文本录入框
check_lims_sample_number_textarea = (
    '.dialog-expMgmt-detail textarea')
# 核对lims样本号确认按钮，元素定位
check_lims_sample_number_confirm = (
    '.dialog-expMgmt-detail .dialog-footer .qcResult-btn-confirm')

# 待选列表全选按钮
all_choice = (
    ' .vxe-table--header-wrapper.body--wrapper .vxe-checkbox--icon.vxe-checkbox--unchecked-icon')
# 加入选中&保存按钮，元素定位
addSelect_or_save_btn = (
    '.createTask_content_choose .commonTaskDetail-commonTaskDetailBtn-submit')
# 进入明细表按钮，元素定位
enter_result_list_btn = (
    '.createTask_content_choose .commonTaskDetail-commonTaskDetailBtn-goSchedule')
# 页面成功提示信息
page_success_info = (
    '//*[@class="el-message el-message--success"]')

# 页面失败提示信息
page_failed_info = (
    '//*[@class="el-message el-message--success"]')

'''
样本处理明细表元素定位
'''
# 样本列表数据全选按钮

# 生成排序号按钮
create_sort_number = (
    '.button-list .schedule-btn-sortNo')

# 列表全选按钮
detail_all_choice = (
    '.createTask_content_table .vxe-table--fixed-left-wrapper .vxe-header--row .vxe-checkbox--icon.vxe-checkbox--unchecked-icon')
# 批量入库类型下拉框
batch_storage_type = (
    '.button-list .schedule-btn-batchStorageType')
# 批量入库类型下拉值
batch_actual_data_choice = (
    '//ul/descendant::li[text()="余样入库" and preceding-sibling::li[text()="不入库（样本用尽）"]]')
# 批量实测数据
batch_actual_data = (
    '.button-list .baseClass-btn-batchData')
# 批量实测数据-样本计量（实测）
Acual_sample_amount = (
    '.dialog-experiment-actualSampleAmt input')
# 批量实测数据-包装量（实测）
Actual_sample_package_amount = (
    '.dialog-experiment-actualSamplePkgAmt input')

# 批量实测数据弹框按钮
batch_actual_data_btn = (
    '.dialog-experiment-data .el-dialog__footer .baseClass-btn-confirm')
# 批量余样数据
batch_remaining_data = (
    '.button-list .baseClass-btn-remainData')
# 计量余样录入框
remaining_sample_amount = (
    '.dialog-remain-remainingSampleAmt input')
# 包装余量录入框
remaining_sample_package_amount = (
    '.dialog-remain-remainingSamplePkgAmt input')

# 批量余样弹框确认按钮
batch_remaining_data_confirm = (
    '.dialog-remain-data .el-dialog__footer .baseClass-btn-confirm')

# 目标库位类型下拉框
target_storage_type = (
    '.button-list .baseClass-btn-deposit')

# 目标库位类型下拉值
target_storage_type_choice = (
    '//ul/descendant::li[text()="临时库" and following-sibling::li[text()="永久库"]]')

# 选择样本盒按钮
select_sample_box = (
    '//*[@class="button-list"]/descendant::button[child::span[text()="选择样本盒"]]')

# 入库弹框选择样本盒弹框target storage 搜索文本录入框
target_storage = (
    '.boxSearch-form-boxName input')

# 入库弹框选择样本盒弹框t搜索按钮
select_sample_box_search = (
    '.dialog-box-search .baseClass-btn-search')

# 选择样本盒值，默认选择列表第一条数据
select_sample_box_choice = (
    '.dialog-box-search .el-table__body-wrapper tr:nth-child(1)')

# 选择样本盒弹框，确认按钮
select_sample_box_comfirm = (
    '.dialog-box-search .dialog-footer .baseClass-btn-confirm')

# 提交按钮
submit_btn = (
    '.button-list .schedule-btn-submit')

# 提交弹框确认按钮
submit_comfirm = (
    '.dialog-commit .baseClass-btn-confirm')

# 入库按钮
deposit_into_storage = (
    '//*[@class="button-list"]/descendant::button[child::span[text()="入库"]]')

# 入库弹框全选按钮
storage_all_choice = (
    '.el-dialog--center .vxe-table--main-wrapper .vxe-table--header-wrapper .vxe-checkbox--unchecked-icon')

# 入库弹框下一步按钮
storage_next = (
    '//*[@aria-label="填写入库信息"]/descendant::button[child::span[text()="下一步"]]')

#提交状态文本
submit_status=(
    '.createTask_content_table .vxe-table--main-wrapper .vxe-table--body-wrapper tbody tr:nth-child(1) td:nth-child(16)')



# 保存结果按钮
detail_save_result = (
    '.createTask_content .baseClass-btn-save')

# 进入结果表按钮
goResult = (
    '.createTask_content .baseClass-btn-goResult')

'''
样本处理结果表元素定位
'''
# 样本列表数据全选按钮
result_all_choice = (
    '.createTask_content_table .vxe-table--fixed-left-wrapper .vxe-table--header-wrapper .vxe-checkbox--icon.vxe-checkbox--unchecked-icon')

# 批量数据按钮
batch_data = (
    '.button-list .baseClass-btn-batchData')

# 批量数据弹框，产物计量文本
product_amount = (
    '.batch-edit-dialog .el-dialog__body form>div:nth-child(1)>div:nth-child(1) input')

# 批量数据弹框，计量单位下拉框
sample_amount_unit = (
    '.batch-edit-dialog .el-dialog__body form>div:nth-child(1)>div:nth-child(2) input')

# 批量数据弹框，计量单位下拉值
sample_amount_unit_choice = (
    '/html/body/div[last()]/div[1]/div[1]/ul/li[2]')

# 批量数据弹框，产物包装量文本框
sample_package_amount = (
    '.batch-edit-dialog .el-dialog__body form>div:nth-child(2)>div:nth-child(1) input')

# 批量数据弹框，包装单位下拉框
sampl_package_amount_unit = (
    '.batch-edit-dialog .el-dialog__body form>div:nth-child(2)>div:nth-child(2) input')

# 批量数据弹框，包装单位下拉值
sampl_package_amount_unit_choice = (
    '/html/body/div[last()]/div[1]/div[1]/ul/li[5]')

# 批量数据弹框,标签打印份数
number_of_labels_printed = (
    '.batch-edit-dialog .el-dialog__body form>div:nth-child(3)>div:nth-child(1) input')

# 批量数据弹框，确认按钮
batch_data_comfirm = (
    '.batch-edit-dialog .el-dialog__footer .baseClass-btn-confirm')

# 获取所有样本lims总数
samples_lims = (
    '.createTask_content_table .vxe-table--fixed-left-wrapper .vxe-table--body-wrapper tbody tr td:nth-child(3)')

# 获取所有样本lims号
samples_lims_num = (
    '.createTask_content_table .vxe-table--fixed-left-wrapper .vxe-table--body-wrapper tbody tr:nth-child({}) td:nth-child(3)')

# 获取所有样本实验室号总数
samples_laboratory = (
    '.createTask_content_table .vxe-table--fixed-left-wrapper .vxe-table--body-wrapper tbody tr td:nth-child(4)')

# 获取所有样本实验室号
samples_laboratory_nub = (
    '.createTask_content_table .vxe-table--fixed-left-wrapper .vxe-table--body-wrapper tbody tr:nth-child({}) td:nth-child(4)')



#结果表提交状态文本定位
result_sample_status=(
    '.createTask_content_table .vxe-table--main-wrapper .vxe-table--body-wrapper tbody tr:nth-child(1) td:nth-child(16)')

# 提交按钮
result_submit = (
    '.button-list .baseClass-btn-submit')

#样本处理结果表提交，录入实验室审核人
lab_boaby='.dialog-result-commit input'
#选择实验室审核人
choice_lab_baby='//li[child::span[text()="周官钟"]]'

# 提交确认按钮
result_submit_comfirm = (
    '.dialog-result-commit .el-dialog__footer .baseclass-btn-confirm')

#返回样本明细
goback_detail_table='.createTask_content .baseClass-btn-back'

#返回样本明细提示确认
goback_detail_table_confirm='.dialog-back .el-dialog__footer .baseClass-btn-next'

# 完成任务单按钮
complete_task_btn = (
    '.createTask_content .baseClass-btn-finish')


# 任务单状态
task_status = (
    '.createTask .clearfix div span:nth-child(3)')

# 明细表任务单号
detail_task_id = (
    '.createTask .clearfix div span:nth-child(1)')

# 结果表任务单号
result_task_id = (
    '.createTask .clearfix div span:nth-child(1)')

