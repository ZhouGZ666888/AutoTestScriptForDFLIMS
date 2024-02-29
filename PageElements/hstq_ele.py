# -*- coding: utf-8 -*-
# @Time    : 2022/08/10
# @Author  : guanzhong.zhou
# @File    : 核酸提取元素定位
# -*-*************************************************************************************-*-
"""
核酸提取首页列表元素定位
"""
# 搜索按钮
search = (
    '.filter-container .baseClass-btn-search')
# 搜索弹框lims号录入文本
search_lims_sample_num = (
    '.commonTaskList-form-sampleIdLims input')
# 搜索弹框确认
search_confirm = (
    '.dialog-search .dialog-footer .baseClass-btn-dialog-confirm')
# 新增按钮
add_sample_process_task = (
    '.filter-container .baseClass-btn-add')
##页面列表样本
sample_page_list = (
    '//div[@class="sample_receive_detail"]/descendant::tbody/tr')
# -*-*************************************************************************************-*-


"""
待选表元素定位
"""
# 选择样本类型点击下拉框
task_type = (
    '.select-task-type input')
# 样本类型选择下拉值，默认第一条
task_type_choice = (
    '.task-type-unique li:nth-child(1)')

# 操作方式点击下拉框
action_type = (
    '.select-operation-type input')

# 操作方式点击下拉值
operationType_choice = (
    '.operation-type-unique li:nth-child(1)')

# 选择sop下拉框
select_sop = (
    '.select-sop-type input')

# 选择sop下拉值
select_sop_choice = (
    '.sopId-unique .el-select-dropdown__list ul:nth-child(1) .el-select-group li:nth-child(1)')
# ****************************************************************


# 核对lims样本号按钮
check_lims_sample_num = (
    '.createTask_content_choose .commonTaskDetail-btn-judgeLims')

# 核对样本号文本录入框
check_lims_sample_number_textarea = (
    '.dialog-expMgmt-detail textarea')

# 核对lims样本号确认按钮，元素定位
check_lims_sample_number_confirm = (
    '.dialog-expMgmt-detail .dialog-footer .qcResult-btn-confirm')

# 查询样本样本错误时报错弹框
search_err_info = '//*[@aria-label="核对结果"]'

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
核酸提取明细表元素定位
'''

# 生成排序号按钮
create_sort_number = (
    '.button-list .extractionSchedule-btn-sortNo')

# 列表第一条数据
first_sample = (
    '.createTask_content_table .vxe-table--fixed-left-wrapper .vxe-table--body-wrapper tbody tr:nth-child(1) .vxe-checkbox--icon.vxe-checkbox--unchecked-icon')

# 列表全选按钮
detail_all_choice = (
    '.createTask_content_table .vxe-table--fixed-left-wrapper .vxe-header--row .vxe-checkbox--icon.vxe-checkbox--unchecked-icon')

# 存在部分选中时的列表全选按钮
detail_path_choice = (
    '.createTask_content_table .vxe-table--fixed-left-wrapper .vxe-header--row .vxe-checkbox--icon.vxe-checkbox--indeterminate-icon')

# 获取原始样本的样本计量值(实测)，回写到分管后的样本中
actualSampleAmt = (
    '.createTask_content_table .vxe-table--main-wrapper .vxe-table--body-wrapper tbody tr:nth-child(1) .extractionSchedule-tableCol-actualSampleAmt  ')

# *****************************************分管****************************************************
# 选择第一条样本进行分管操作
choice_one_sample = (
    '.createTask_content_table .vxe-table--fixed-left-wrapper .vxe-table--body-wrapper tr:nth-child(1) .extractionSchedule-tableCol-sortNo  ')

# 分管按钮
aliquot_sample = (
    '.button-list .extractionSchedule-btn-dividedSample')

#分管前注意事项提示框
aliquot_before_tips='.el-message-box__wrapper .el-message-box__btns button:nth-child(2)'

# 分管弹框全选按钮
aliquot_sample_all_choice = (
    '.el-dialog .el-dialog__body .vxe-table--main-wrapper .vxe-table--header-wrapper table .vxe-checkbox--unchecked-icon')

# 分管弹框分管数文本录入
aliquot_number = '//*[@aria-label="样本分管"]/descendant::input'

# 分管弹框分管数文本录入后批量填入按钮
aliquot_number_batch_edit = '//*[@aria-label="样本分管"]/descendant::form/descendant::button'

# 分管弹框下一步按钮
aliquot_sample_next = (
    '//*[@class="dialog-divided"]/descendant::button[span[text()="下一步"]]')

# 封管最后步骤弹框全选
aliquot_sample_last_step_all_choice = (
    '.dialog-divide-next .vxe-table--header-wrapper .vxe-header--row .vxe-checkbox--icon.vxe-checkbox--unchecked-icon')

# 分管批量输入
aliquot_sample_batch_data = '.dialog-divide-next .el-dialog__body button'

# 分管批量输入"是否做mPCR"定位
aliquot_sample_ismPCR = (
    '.dialog-divided > div:nth-child(2) > div:nth-child(2) .el-dialog__body .vxe-table--main-wrapper .vxe-table--body-wrapper tbody tr td:nth-child(2)')

# 分管批量输入"是否做mPCR"下拉
aliquot_sample_ismPCR_input = '.dialog-divided > div:nth-child(2) > div:nth-child(2) .el-dialog__body .vxe-table--main-wrapper .vxe-table--body-wrapper tbody tr td:nth-child(2) input'

# 分管批量输入"是否做mPCR"下拉选择“否”
aliquot_sample_ismPCR_chioce = '.dialog-divided > div:nth-child(2) > div:nth-child(2) .el-dialog__body ' \
                               '.vxe-table--main-wrapper .vxe-table--body-wrapper tbody tr td:nth-child(2) li:nth-child(2)'

# 分管批量输入"最后步骤"定位
aliquot_sample_lastStep = (
    '.dialog-divided > div:nth-child(2) > div:nth-child(2) .el-dialog__body .vxe-table--main-wrapper '
    '.vxe-table--body-wrapper tbody tr td:nth-child(3)')

# 分管批量输入"最后步骤"下拉
aliquot_sample_lastStep_input = '.dialog-divided > div:nth-child(2) > div:nth-child(2) .el-dialog__body ' \
                                '.vxe-table--main-wrapper .vxe-table--body-wrapper tbody tr td:nth-child(3) input'

# 分管批量输入"最后步骤"下拉选择“上机”
aliquot_sample_lastStep_chioce = '.dialog-divided > div:nth-child(2) > div:nth-child(2) .el-dialog__body .vxe-table--main-wrapper .vxe-table--body-wrapper tbody tr td:nth-child(3) .vxe-select-option--wrapper div:nth-child(3)'

# 分管批量输入"建库类型"定位
aliquot_sample_libType = (
    '.dialog-divided > div:nth-child(2) > div:nth-child(2) .el-dialog__body .vxe-table--main-wrapper '
    '.vxe-table--body-wrapper tbody tr td:nth-child(4)')

# 分管批量输入"建库类型"下拉
aliquot_sample_libType_input = '.dialog-divided > div:nth-child(2) > div:nth-child(2) .el-dialog__body ' \
                               '.vxe-table--main-wrapper .vxe-table--body-wrapper tbody tr td:nth-child(4) input'

# 分管批量输入"建库类型"下拉选择“DNA建库”
aliquot_sample_libType_chioce = '.dialog-divided > div:nth-child(2) > div:nth-child(2) .el-dialog__body .vxe-table--main-wrapper .vxe-table--body-wrapper tbody tr td:nth-child(4) >div >div >div:nth-child(3) >div > div:nth-child(1)'

#分管批量录入确认按钮
aliquot_sample_confirm_btn='.dialog-divided > div:nth-child(2) > div:nth-child(2) .el-dialog__footer button:nth-child(2)'


#分管预设通量


# 明细表分管弹框分管后确认按钮
aliquot_sample_last_step_comfirm = '.dialog-divide-next .dialog-footer .baseClass-btn-confirm'

# 明细表批量入库类型下拉框
detail_batch_storage_type = '.button-list .extractionSchedule-btn-batchStorage'
# 明细表批量入库类型下拉值
detail_batch_storage_type_choice = (
    '//ul[@class="el-dropdown-menu el-popper baseClass-dropdown-batchStorage el-dropdown-menu--medium"]/descendant::li[text()="余样入库"]')

# 添加对照
add_ntc = '.button-list .extractionSchedule-btn-addNTC'

# 对照大类选择框
ntc_choice = '.dialog-ntc .select-ntc-optionsBig input'

# 选择NTC对照类型
choice_ntc_type = '.select-ntc-optionsBig .el-select-dropdown__list li:nth-child(1)'

#选择对照样本类型
choice_ntc_sample_type='.dialog-ntc .select-ntcType-options input'

#选择mNGS对照类型
ntc_mNGS='.select-ntcType-options .el-select-dropdown__list li:nth-child(1)'

# 迪讯康类型
ntc_dxk = '.select-ntcType-options .el-select-dropdown__list li:nth-child(2)'

# 添加ntc确认按钮
add_ntc_confirm = '.dialog-ntc .el-dialog__footer .baseClass-btn-confirm'

#添加对照确认按钮
add_duizhao_confirm='.createTask >div:nth-child(14) .el-dialog__footer button:nth-child(2)'

# 明细表批量数据按钮
detail_batch_data = (
    '.button-list .extractionSchedule-btn-batchData')

# 明细表批量数据，样本进入量
detail_used_sample_amount = (
    '.extractionSchedule-formBatchData-usedSampleAmt input')

# 明细表批量数据，包装余量
detail_remaining_sample_package_amount = (
    '.extractionSchedule-formBatchData-remainingSamplePkgAmt input')

# 明细表批量数据，包装单位下拉框
detail_sample_package_amount_unit = (
    '.extractionSchedule-formBatchData-samplePkgAmtUnit input')

# 明细表批量数据，包装单位下拉值
detail_sample_package_amount_unit_value = (
    '/html/body/div[last()]/div[1]/div[1]/ul/li[5]')

# 明细表批量数据，包装余量单位下拉框
detail_remaining_sample_package_amount_unit = (
    '.extractionSchedule-formBatchData-remainingSamplePkgUnit input')

# 明细表批量数据，包装余量单位下拉值
detail_remaining_sample_package_amount_unit_value = (
    '/html/body/div[last()]/div[1]/div[1]/ul/li[5]')

# 明细表批量数据弹框，确认按钮
detail_batch_data_comfirm = (
    '.dialog-batch-edit .el-dialog__footer .baseClass-btn-confirm')

# 自动计算按钮
detail_auto_calculate = (
    '.button-list .extractionSchedule-btn-autoComplete')

# 提交按钮
submit_btn = (
    '.button-list .extractionSchedule-btn-commit')

# 提交弹框确认按钮
submit_comfirm = (
    '.dialog-commit .dialog-footer .baseClass-btn-confirm')

# **************************************************************************入库
# 入库按钮
deposit_into_storage = (
    '.button-list .extractionSchedule-btn-deposit')

# 入库弹框全选按钮
storage_all_choice = (
    '.el-dialog--center .vxe-table--main-wrapper .vxe-table--header-wrapper .vxe-checkbox--icon.vxe-checkbox--unchecked-icon')


# 入库弹框选择样本盒按钮
batch_paste_sample_box ='//button[child::span[text()="选择样本盒"]]'

# 入库弹框选择样本盒弹框target storage 搜索文本录入框
target_storage = (
    '.boxSearch-form-boxName input')

# 入库弹框选择样本盒弹框搜索按钮
select_sample_box_search = (
    '.dialog-box-search .baseClass-btn-search')

# 入库弹框选选择样本盒值，默认选择列表第一条数据
select_sample_box_choice = (
    '.el-dialog--center .el-dialog__body .el-table__body-wrapper table tbody tr:nth-child(1)')

# 入库弹框选择样本盒弹框，确认按钮
select_sample_box_comfirm = (
    '.createTask > div:nth-child(9) .dialog-box-search .el-dialog__footer .baseClass-btn-confirm')

# 批量粘贴盒内位置
batch_copy_BoxPosition = (
    '.checkStorageDialog-btn-batchCopyBoxPosition')

# 批量粘贴盒内位置文本录入
batch_copy_BoxPosition_input = (
    '.positionBoxCopy-form-textareaValue textarea')

# 批量粘贴盒内位置确认按钮
batch_copy_BoxPosition_comfirm = (
    '.dialog-position-box-copy .dialog-footer .baseClass-btn-confirm')

# 入库弹框下一步按钮
storage_next = (
    '.dialog-check-storage .dialog-footer button:nth-child(2)')

# 明细表提交状态文本定位
submit_status = (
    '.createTask_content_table .vxe-table--main-wrapper .vxe-table--body-wrapper tbody tr:nth-child(1) td:nth-child('
    '26)')

# 获取所有样本数量
all_samples = (
    '.createTask_content_table .vxe-table--fixed-left-wrapper .vxe-table--body-wrapper tbody tr')

# 保存结果按钮
detail_save_result = (
    '.createTask_content .baseClass-btn-save')
# 进入结果表按钮
goResult = (
    '.createTask_content .baseClass-btn-goResult')

'''
核酸提取结果表元素定位
'''
# 生成排序号
sortNo = (
    '.button-list .extractionResults-btn-sortNo')

# 样本列表数据全选按钮
result_all_choice = (
    '.createTask_content_table .vxe-table--fixed-left-wrapper .vxe-table--header-wrapper .vxe-checkbox--icon.vxe-checkbox--unchecked-icon')

# 修改产物类型
result_change_product_type = (
    '.button-list .baseClass-btn-changeResultType')

# 修改产物类型弹框数据选择，默认选择第一条
result_change_product_type_choice = (
    '//*[@aria-label="产物类型"]/descendant::tr[descendant::span[text()="游离DNA"]]')

# 修改产物类型弹框数据选择，确认
result_change_product_type_comfirm = (
    '//*[@aria-label="产物类型"]/descendant::button[4]')

# 修改产物类型，类型不一致提示框确认按钮
result_change_product_type_continue_comfirm = (
    '.dialog-show-error .el-dialog__footer .baseclass-btn-confirm')

# 批量数据按钮
result_batch_data = (
    '.button-list .baseClass-btn-batchData')

# 批量数据弹框，产物包装量
result_product_amount = (
    '.extractionResults-dialogBatchData-samplePkgAmt input')

# 批量数据弹框，包装单位下拉框
result_sample_amount_unit = (
    '.extractionResults-dialogBatchData-samplePkgAmtUnit input')

# 批量数据弹框，包装单位下拉值（管 ）
result_sample_amount_unit_choice = (
    '//*[@class="el-select-dropdown__wrap el-scrollbar__wrap"]/descendant::li[child::span[text()="管"]]')

# 批量数据弹框，圆标签打印份数文本框
result_sample_package_amount = (
    '.extractionResults-dialogBatchData-noOfRoundLabels input')

# 批量数据弹框，长标签打印份数文本框
result_sampl_package_amount_unit = (
    '.extractionResults-dialogBatchData-noOfLongLabels input')

# 批量数据弹框，产物体积
result_sampl_package_amount_unit_choice = (
    '.extractionResults-dialogBatchData-volumeAmt input')

# 批量数据弹框，确认按钮
result_batch_data_comfirm = (
    '//*[@aria-label="批量数据"]/descendant::button[2]')

# 结果表自动计算按钮
result_auto_calculate = (
    '.button-list .baseClass-btn-autoComplete')

# 结果表自动计算提示框确认按钮
result_auto_calculate_promote = (
    '.el-message-box__wrapper .el-message-box__btns .el-button--default')

# 生成盒内位置
result_postionInBox = '.button-list .extractionResults-btn-postionInBox'

# 生成盒内位置,确认生成
result_postionInBox_confirm = '.dialog-positionInBox .el-dialog__footer .baseClass-btn-confirm'

# 生成盒内位置,覆盖提示
result_postionInBox_info_confirm = '.el-message-box__wrapper .el-message-box__btns button:nth-child(2)'

# 提交按钮
result_submit = (
    '.button-list .extractionResults-btn-submit')

# 临时库实验室审核人录入框
nextProcessorId = (
    '.dialog-result-commit .result-commit-nextProcessorId input')

# 临时库实验室审核人录入选择
nextProcessorId_choice = (
    '.el-select-dropdown__wrap.el-scrollbar__wrap li:nth-child(1)')

# 提交确认按钮
result_submit_comfirm = (
    '.dialog-result-commit .dialog-footer .baseclass-btn-confirm')

# 结果表提交状态文本定位
result_sample_status = (
    '.createTask_content_table .vxe-table--main-wrapper .vxe-table--body-wrapper table tbody tr:nth-child(1) '
    'td:nth-child(8)')

# 完成任务单按钮
result_complete_task_btn = (
    '.createTask_content .baseClass-btn-completeTask')

# 保存结果按钮
result_save_result = (
    '.createTask_content .baseClass-btn-save')
# 返回样本明细
goback_detail_table = '.createTask_content .baseClass-btn-goSchedule'

# 返回样本明细提示确认
goback_detail_table_confirm = '.dialog-back .el-dialog__footer .baseClass-btn-next'

# 明细表任务单号
detail_task_id = (
    '.createTask .clearfix div span:nth-child(1)')
# 结果表任务单号
result_task_id = (
    '.createTask .clearfix div span:nth-child(1)')
# 任务单状态
task_status = (
    '.createTask .clearfix div span:nth-child(3)')
