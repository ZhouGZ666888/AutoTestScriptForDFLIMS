# -*- coding: utf-8 -*-
# @Time    : 2022/08/25
# @Author  : guanzhong.zhou
# @File    : 文库构建元素定位
# -*-*************************************************************************************-*-
"""
文库构建首页列表元素定位
"""
# 搜索按钮
search = (
    '.filter-container .baseClass-btn-search')

# 搜索弹框lims号录入文本
search_lims_sample_num = (
    '.commonTaskList-form-sampleIdLims input')

# 搜素弹框确认
search_confirm = (
    '.dialog-search .el-dialog__footer .baseClass-btn-dialog-confirm')

# 新增按钮
add_sample_process_task = (
    '.filter-container .baseClass-btn-add')

##页面列表样本
sample_page_list = (
    '//*[@class="sample_receive_detail"]/descendant::tbody/tr')

# -*-*************************************************************************************-*-


'''
待选表元素定位
'''
# 选择样本类型点击下拉框
task_type = (
    '.select-task-type input')

# 样本类型选择下拉值，默认第一条
task_type_choice = (
    '.task-type-unique .el-select-dropdown__wrap li:nth-child(1)')

# 操作方式下拉框
operation_type = (
    '.createTask_content_choose .el-form.el-form--label-left div.el-row:nth-child(2) input')

# 操作方式下拉框
operation_type_choice = (
    '.select-operationType-options .el-select-dropdown__list li:nth-child(1)')

# 选择sop下拉框
select_sop = (
    '.select-sop-type input')

# 选择sop下拉值,m默认选择第一条
select_sop_choice = (
    '.sopId-unique .el-select-dropdown__wrap .el-select-group li:nth-child(1)')

# 核对lims样本号按钮
check_lims_sample_num = (
    '.createTask_content_choose .commonTaskDetail-btn-judgeLims')

# 核对样本号文本录入框
check_lims_sample_number_textarea = (
    '.dialog-expMgmt-detail textarea')

# 核对lims样本号确认按钮，元素定位
check_lims_sample_number_confirm = (
    '.dialog-expMgmt-detail .dialog-footer .qcResult-btn-confirm')

#查询结果有不存在样本号提示信息
error_info=(
    '//*[@aria-label="核对结果"]/div[@class="el-dialog__footer"]/descendant::span/button')


# 待选列表全选按钮
all_choice = (
    '.vxe-table--main-wrapper .vxe-table--header-wrapper .vxe-header--row .vxe-checkbox--icon.vxe-checkbox--unchecked-icon')

# 加入选中&保存按钮，元素定位
addSelect_or_save_btn = (
    '.commonTaskDetail-commonTaskDetailBtn-submit')

# 进入明细表按钮，元素定位
enter_detail_list_btn = (
    '.commonTaskDetail-commonTaskDetailBtn-goSchedule')

# 页面成功提示信息
page_success_info = (
    '//*[@class="el-message el-message--success"]/descendant::p')

# 页面失败提示信息
page_failed_info = (
    '//*[@class="el-message el-message--success"]')

'''
文库构建明细表元素定位
'''

# 列表全选按钮
detail_all_choice = (
    '.createTask_content_table .vxe-table--fixed-left-wrapper .vxe-header--row .vxe-checkbox--icon.vxe-checkbox--unchecked-icon')

# 样本数据获取样本数据总数量
detail_all_samples = (
    '.createTask_content_table .vxe-table--fixed-left-wrapper .vxe-table--body-wrapper tbody tr')

# *****************入库类型选择**************

# 明细表批量入库类型下拉框
detail_batch_storage_type = (
    '.button-list .libconstructionSchedule-btn-batchStorageType')

# 明细表批量入库类型下拉值
detail_batch_storage_type_choice = (
    '.baseClass-dropdown-batchStorageType li:nth-child(2) ')

# 批量包装余量
batch_remaining_sample_package_amount = (
    '.button-list .libconstructionSchedule-btn-handleBatchData')

# 批量包装余量弹框确认按钮
batch_remaining_sample_package_amount_comfirm = (
    '.batch-edit-dialog .el-dialog__footer .baseClass-btn-confirm')

# *********************************************表单录入**********************************************

# 自动生成96孔版位置表单定位
col_96_well_plate_position = (
    '.createTask_content_table .vxe-table--main-wrapper tbody tr:nth-child(1) .libconstructionSchedule-tableCol-positionInOrifice')

# 自动生成96孔版位置表单文本录入框
col_create_96_well_plate_position_input = (
    '.createTask_content_table .vxe-table--main-wrapper tbody tr:nth-child(1) .libconstructionSchedule-tableCol-positionInOrifice   input')

# 自动生成96孔板位置按钮
auto_create_96_well_plate_position = (
    '.button-list .libconstructionSchedule-btn-generate96')

# 自动计算按钮
detail_auto_calculate = (
    '.createTask_content .sampleDetail_header .button-list .libconstructionSchedule-btn-autoComplete')

# 提交按钮
submit_btn = (
    '.button-list .libconstructionSchedule-btn-submit')

# 提交弹框确认按钮
submit_comfirm = (
    '.dialog-commit .dialog-footer .baseClass-btn-confirm')

# /************************入库****************************
# 入库按钮
deposit_into_storage = '.button-list .libconstructionSchedule-btn-storage'

# 入库弹框全选按钮
storage_all_choice = '.el-dialog--center .vxe-table--main-wrapper .vxe-table--header-wrapper .vxe-checkbox--icon.vxe-checkbox--unchecked-icon'

# 入库弹框选择入库类型下拉框
target_storage_type = '.dialog-check-storage .checkStorageDialog-btn-targetLocation'

# 入库弹框选择入库类型下拉值（临时库）
target_storage_type_value = '//ul[@class="el-dropdown-menu el-popper el-dropdown-menu--medium"]/descendant::li[text()="临时库"]'

# 入库弹框选择样本盒按钮
batch_paste_sample_box = '.dialog-check-storage .checkStorageDialog-btn-selectBox'

# 入库弹框选择样本盒弹框target storage 搜索文本录入框
target_storage = '.boxSearch-form-boxName input'

# 入库弹框选择样本盒弹框t搜索按钮
select_sample_box_search = '.dialog-box-search .baseClass-btn-search'

# 入库弹框选选择样本盒值，默认选择列表第一条数据
select_sample_box_choice = '.dialog-box-search .el-dialog__body .el-table__body-wrapper tbody tr:nth-child(1)'

# 入库弹框选择样本盒弹框，确认按钮
select_sample_box_comfirm = '.createTask >div:nth-child(11) .dialog-box-search .el-dialog__footer .baseClass-btn-confirm'

# 批量粘贴盒内位置
batch_copy_BoxPosition = '.checkStorageDialog-btn-batchCopyBoxPosition'

# 批量粘贴盒内位置文本录入
batch_copy_BoxPosition_input = '.dialog-position-box-copy textarea'

# 批量粘贴盒内位置确认按钮
batch_copy_BoxPosition_comfirm = '.dialog-position-box-copy .dialog-footer .baseClass-btn-confirm'

# 入库弹框下一步按钮
storage_next = '.dialog-check-storage .dialog-footer button:nth-child(2)'


# *********************************************************************************
# 核酸浓度（实测）文本定位
consistenceAmt = (
    '.createTask_content_table .vxe-table--main-wrapper .vxe-table--body-wrapper tbody tr:nth-child(1) td.libconstructionSchedule-tableCol-consistenceAmt')

#核酸总量文本定位
actualTotalAmt=(
    '.createTask_content_table .vxe-table--main-wrapper .vxe-table--body-wrapper tbody tr:nth-child(1) td.libconstructionSchedule-tableCol-actualTotalAmt')

# 建库进入量文本定位
countamt = (
    '.createTask_content_table .vxe-table--main-wrapper .vxe-table--body-wrapper tbody tr:nth-child(1) .libconstructionSchedule-tableCol-usedTotalAmt  ')

# 余样体积文本定位
remaining_VolumeAmt = (
    '.createTask_content_table .vxe-table--main-wrapper .vxe-table--body-wrapper tbody tr:nth-child(1) .libconstructionSchedule-tableCol-remainingVolumeAmt  ')

# 余样总量文本定位
remaining_TotalAmt = (
    '.createTask_content_table .vxe-table--main-wrapper .vxe-table--body-wrapper tbody tr:nth-child(1) .libconstructionSchedule-tableCol-remainingTotalAmt  ')

# 提交状态文本定位
submit_status = (
    '.createTask_content_table .vxe-table--main-wrapper .vxe-table--body-wrapper tbody tr:nth-child(1) td:nth-child(27)')

# 样本列表滚动条
scroll_line = (
    '//*[@class="vxe-table--border-line"]')

# 保存结果按钮
detail_save_result = (
    '.createTask_content .is-justify-end .baseClass-btn-save')

# 进入结果表按钮
enter_result_list_btn = (
    '.createTask_content .baseClass-btn-goResults')

'''
文库构建结果表元素定位
'''
# 样本列表数据全选按钮
result_all_choice = (
    '.createTask_content_table .vxe-table--fixed-left-wrapper .vxe-header--row .vxe-checkbox--icon.vxe-checkbox--unchecked-icon')

# *****************产物类型****************************************

# 修改产物类型
result_change_product_type = (
    '.button-list .baseClass-btn-changeResultType')

# 修改产物类型弹框数据选择，默认选择第一条
result_change_product_type_choice = (
    '.multi-table-dialog .el-dialog__body .vxe-table--body-wrapper table tbody tr:nth-child(1)')

# 修改产物类型弹框数据选择，确认
result_change_product_type_comfirm = (
    '.multi-table-dialog .dialog-footer .baseClass-btn-confirm')

error_info_box='//div[child::div[@class="el-dialog el-dialog--center dialog-show-error"]]'

# 修改产物类型，类型不一致提示框确认按钮
result_change_product_type_continue_comfirm = (
    '.dialog-show-error .el-dialog__footer .baseclass-btn-confirm')

# *****************批量数据****************************************
# 批量数据按钮
result_batch_data = (
    '.button-list .baseClass-btn-batchData')

# 批量数据弹框，产物包装量
result_sample_package_amount = (
    '.libconstructionResults-dialogBatchData-samplePkgAmt input')

# 批量数据弹框，包装单位下拉框
result_sample_package_amount_unit = (
    '.libconstructionResults-dialogBatchData-samplePkgAmtUnit input')

# 批量数据弹框，包装单位下拉值（管 ）
result_sample_amount_unit_choice = (
    '.libconstructionResults-samplePkgAmtUnit li:nth-child(5)')

# 批量数据弹框，圆打印份数文本框
result_number_of_ircular_labels_printed = (
    '.libconstructionResults-dialogBatchData-noOfRoundLabels input')

# 批量数据弹框，长打印份数文本框
result_number_of_rectangular_labels_printed = (
    '.libconstructionResults-dialogBatchData-noOfLongLabels input')

# 批量数据弹框，Adapter浓度下拉框
adapter_concentration = (
    '.libconstructionResults-dialogBatchData-adapterConsistenceAmt input')

# 批量数据弹框，Adapter浓度下拉值选择
adapter_concentration_choice = (
    '.libconstructionResults-adapterConsistenceAmt .el-select-dropdown__list li:nth-child(1)')

# 批量数据弹框，循环数
pcr_cycle = (
    '//input[preceding-sibling::div[text()="循环数"]]')

# 批量数据弹框，文库体积
library_volume = (
    '.libconstructionResults-dialogBatchData-volumeAmt input')

# 批量数据弹框，确认按钮
result_batch_data_comfirm = (
    '.dialog-batch-edit .el-dialog__footer .baseClass-btn-confirm')

# *********************修改预计富集时间**************************
# 预计富集时间按钮
edit_estimated_enrichment_time = (
    '.button-list .baseClass-btn-setLibconstructionResultPoolingList')

# 预计富集时间弹框全选
edit_estimated_enrichment_time_all_choice = (
    '.dialog-showLibconstructionResultPooling .el-dialog__body .vxe-table--main-wrapper .vxe-checkbox--icon.vxe-checkbox--unchecked-icon')

# 预计富集时间弹框，录入时间弹框按钮
batch_edit_estimated_enrichment_date = (
    '.dialog-showLibconstructionResultPooling .taskInitial-btn-dialogVisible2')

# 预计富集时间弹框，时间录入文本
estimated_enrichment_data = (
    '.lims_dialog .dialog-dialogVisible2 .el-dialog__body input')

# 预计富集时间弹框，时间录入文本确认按钮
estimated_enrichment_data_comfirm = (
    '.lims_dialog .el-dialog__footer .baseClass-btn-dialog-confirm')

# 预计富集时间弹框确认按钮
edit_estimated_enrichment_time_comfirm = (
    '.dialog-showLibconstructionResultPooling .el-dialog__footer .baseClass-btn-dialog-confirm')

# *******************Adapter选择******************

# adapter表单定位
adapter = (
    '.createTask_content_table .vxe-table--main-wrapper tbody tr:nth-child({}) .libconstructionResults-tableCol-indexId  ')

# adapter弹框选择，默认第一个
adapter_choice = (
    '//*[@class="el-dialog__wrapper dialog-index"]/descendant::tr[child::td[child::div[text()="A1"]]]')

# adapter弹框确认按钮
adapter_comfirm = (
    '.dialog-index .el-dialog__footer .qcResult-btn-confirm')

# adapter浓度表单定位
adapter_concentration_form = (
    '//*[@class="vxe-table--body-wrapper body--wrapper"]/table/tbody/tr[{}]/td[9]')

# adapter浓度下拉选择按钮
adapter_concentration_form_select = (
    '//*[@class="vxe-table--body-wrapper body--wrapper"]/table/tbody/tr[{}]/td[9]/div/div/div/input')

# adapter浓度下拉选择
adapter_concentration_form_choice = (
    '//div[@class="el-select-dropdown el-popper"]/descendant::li[1]')

# *************要录入数据表单定位*****************************

# 生成盒内位置
result_postionInBox = '.button-list .baseClass-btn-positionInBox'

# 生成盒内位置,确认生成
result_postionInBox_confirm = '.dialog-positionInBox .el-dialog__footer .baseClass-btn-confirm'

# 生成盒内位置,覆盖提示
result_postionInBox_info_confirm = '.el-message-box__wrapper .el-message-box__btns button:nth-child(2)'
# **************************


# 获取所有样本lims号
result_samples_lims = (
    '.createTask_content_table .vxe-table--fixed-left-wrapper .vxe-table--body-wrapper tbody tr:nth-child({}) td:nth-child(2)')

# 获取所有样本实验室号
result_samples_laboratory = (
    '.createTask_content_table .vxe-table--fixed-left-wrapper .vxe-table--body-wrapper tbody tr:nth-child({}) td:nth-child(3)')

# 盒内位置表单定位
result_position_in_box = (
    '//*[@class="createTask_content_table"]/div[1]/div[2]/div[2]/table/tbody/tr[{}]/td[16]')

# 盒内位置文本录入框定位
result_position_in_box_input = (
    '.ultrafracResults-tableCol-positionInTmpBox input')

# 选中全部样本数量,用来计总数
result_samples_for_total = (
    '.createTask_content_table .vxe-table--fixed-left-wrapper .vxe-table--body-wrapper tbody tr')

# 选中全部样本，依次获取，用来对依次获取的样本进行表单数据录入
result_next_step = (
    '.createTask_content_table .vxe-table--main-wrapper .vxe-table--body-wrapper tbody tr:nth-child(1)')

# 结果表自动计算按钮
result_auto_calculate = (
    '.button-list .baseClass-btn-autoComplete')

# 结果表自动计算提示框确认按钮
result_auto_calculate_promote = (
    '.el-message-box__wrapper .el-message-box__btns .el-button--default')

# 提交按钮
result_submit = (
    '.button-list .baseClass-btn-submit')

# 提交确认按钮
result_submit_comfirm = (
    '.dialog-result-commit .dialog-footer .baseclass-btn-confirm')

# 完成任务单按钮
result_complete_task_btn = (
    '.createTask_content .baseClass-btn-completeTask')

# 保存任务单
result_save_task = (
    '.createTask_content .baseClass-btn-save')

# 完成任务单提示弹框确认按钮
result_complete_task_comfirm = (
    '.el-message-box__wrapper .el-message-box__btns .el-button--primary ')

# 明细表任务单号
detail_task_id = (
    '.createTask .clearfix div span:nth-child(1)')

# 结果表任务单号
result_task_id = (
    '.createTask .clearfix div span:nth-child(1)')

# 任务单状态
detail_task_status = (
    '.createTask .clearfix div span:nth-child(3)')

#页面提示信息
pageinfo=(
    '.el-message.el-message--error .el-message__content')

# 返回明细表
goback_detail = '.createTask .baseClass-btn-goSchedule'

# 返回明细表确认
goback_page_info = '.el-dialog__wrapper .el-dialog__footer .baseClass-btn-continue'