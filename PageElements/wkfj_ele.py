# -*- coding: utf-8 -*-
# @Time    : 2022/08/26
# @Author  : guanzhong.zhou
# @File    : 文库富集元素定位
# -*-*************************************************************************************-*-
"""
文库富集首页列表元素定位
"""
# 搜索按钮
search = (
    '.filter-container .baseClass-btn-search')

# 搜索弹框lims号录入文本
search_lims_sample_num = (
    '.dialog-search .commonTaskList-form-sampleIdLims input')

# 搜索弹框确认
search_confirm = (
    '.dialog-search .el-dialog__footer .baseClass-btn-dialog-confirm')

# 新增按钮
add_sample_process_task = (
    '.filter-container .baseClass-btn-add')

##页面列表样本
sample_page_list = (
        '//*[@class="sample_receive_detail"]/descendant::tbody/tr')

# -*-*************************************************************************************-*-

"""
待选表元素定位,
"""

#任务类型下拉框
task_type='.select-task-type input'

#任务类型下拉值选择
task_type_choice='//*[@class="el-select-dropdown el-popper task-type-unique"]/descendant::span[text()="{}"]'

# 任务描述文本录入框
task_description = (
    '.poolingDetail-form-taskDesc input')

#操作方式下拉框
action_stlye='.poolingDetail-operationType-options input'

#操作方式下拉值选择
action_stlye_choice='.select-operationType-options li:nth-child(1)'


# 选择sop下拉框
select_sop = '.select-sop-type input'

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

#结果核对
result_check='//*[@aria-label="核对结果"]/div[@class="el-dialog__footer"]/descendant::button'
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

"""
文库富集明细表元素定位
"""

# 列表全选按钮
detail_all_choice = (
    '.createTask_content .show--head .vxe-table--fixed-left-wrapper .vxe-table--header-wrapper .vxe-checkbox--icon.vxe-checkbox--unchecked-icon')

#自动生成序号按钮
generatedSortNo='.button-list .baseClass-btn-generatedSortNo'

# 样本数据获取样本数据总数量
all_samples = (
    '.createTask_content .show--head .vxe-table--fixed-left-wrapper .vxe-table--body-wrapper tbody tr')

# 样本数据获取样本lims号
all_sample_lims = (
    '.schedule-experiment-table-height-auto-enrich .el-card__body .vxe-table--fixed-left-wrapper .vxe-table--body-wrapper tbody tr:nth-child({}) td:nth-child(2)')

#实设探针选择文本框
probe_select='.vxe-table--main-wrapper .vxe-table--body tbody tr:nth-child({}) .enrichmentSchedule-tableCol-actualProbe'
probe_select_input='.vxe-table--main-wrapper .vxe-table--body tbody tr:nth-child({}) ' \
              '.enrichmentSchedule-tableCol-actualProbe input'

#实设探针选项
probe_choice='.vxe-select--panel .vxe-select-option--wrapper div'

#进入量文本框定位
theoreticalUsedAmt='.vxe-table--main-wrapper .vxe-table--body tbody tr:nth-child({}) .enrichmentSchedule-tableCol-theoreticalUsedAmt'

#进入量文本录入框
theoreticalUsedAmt_input='.vxe-table--main-wrapper .vxe-table--body tbody tr:nth-child({}) ' \
                    '.enrichmentSchedule-tableCol-theoreticalUsedAmt input'
# 样本数据获取样本实验室号
all_sample_lab = (
    '.schedule-experiment-table-height-auto-enrich .el-card__body .vxe-table--main-wrapper .vxe-table--body-wrapper tbody tr:nth-child({}) td:nth-child(3)')
# *****************入库类型选择、批量粘贴导入**************

# 明细表批量入库类型下拉框
detail_batch_storage_type = (
    '.button-list .enrichmentSchedule-btn-handleStorage')

# 明细表批量入库类型下拉值,选余样入库
detail_batch_storage_type_choice = (
    '//ul[@class="el-dropdown-menu el-popper el-dropdown-menu--medium"]/descendant::li[text()="余样入库" and preceding-sibling::li[text()="不入库（样本用尽）"]]')

# 批量粘贴导入按钮
batch_paste_import_package = (
    '.button-list .enrichmentSchedule-btn-showDialogChannel')

# 批量粘贴导入弹框文本编辑框
batch_paste_import_package_textarea = (
    '.dialog-copy-data .el-dialog__body  textarea')

# 明细表批量粘贴导入弹框确认按钮
batch_paste_import_package_comfirm = (
    '.dialog-copy-data .el-dialog__footer .baseClass-btn-confirm')

#明细表批量粘贴导入弹框确认后index不一致提示框
batch_paste_import_package_comfirm_contiune=(
    '//*[@class="createTask"]/child::div[@class="el-dialog__wrapper"]/child::div[@aria-label="提示"]/child::div[@class="el-dialog__footer"]/descendant::button')

# *********************************************表单录入**********************************************
# 生成结果按钮
create_result = (
    '.schedule-experiment-table-height-auto-enrich .button-list .enrichmentSchedule-btn-handleGeneration')

# 提交按钮
submit_btn = (
    '.button-list .baseClass-btn-submit')

# 提交弹框确认按钮
submit_comfirm = (
    '.dialog-commit .dialog-footer .baseClass-btn-confirm')

#明细表自动计算
automatic='//span[text()="自动计算"]'

#自动计算规则不完整提示
tips='.el-message-box__wrapper .el-message-box__btns button'

# 生成结果状态表单展示
result_status='.createTask_content .vxe-editable .vxe-table--main-wrapper .vxe-table--body-wrapper table tbody tr:nth-child(1) td:nth-child({})'


# /************************入库****************************
# 入库按钮
deposit_into_storage = (
    '.button-list .baseClass-btn-storage')

# 入库弹框全选按钮
storage_all_choice = (
    '.el-dialog--center .vxe-table--main-wrapper .vxe-table--header-wrapper .vxe-checkbox--icon.vxe-checkbox--unchecked-icon')

# 入库弹框选择入库类型下拉框
target_storage_type = (
    '.dialog-check-storage .checkStorageDialog-btn-targetLocation')

# 入库弹框选择入库类型下拉值（临时库）
target_storage_type_value = (
    '//ul[@class="el-dropdown-menu el-popper el-dropdown-menu--medium"]/descendant::li[text()="临时库"]')

# 入库弹框选择样本盒按钮
batch_paste_sample_box = (
    '.checkStorageDialog-btn-selectBox')

# 入库弹框选择样本盒弹框target storage 搜索文本录入框
target_storage = (
    '.boxSearch-form-boxName input')

# 入库弹框选择样本盒弹框t搜索按钮
select_sample_box_search = (
    '.dialog-box-search .baseClass-btn-search')

# 入库弹框选选择样本盒值，默认选择列表第一条数据
select_sample_box_choice = (
    '.dialog-box-search .el-dialog__body .el-table__body-wrapper tbody tr:nth-child(1)')

# 入库弹框选择样本盒弹框，确认按钮
select_sample_box_comfirm = (
    '.dialog-box-search .dialog-footer .baseClass-btn-confirm')

# 批量粘贴盒内位置
batch_copy_BoxPosition = (
    '.checkStorageDialog-btn-batchCopyBoxPosition')

# 批量粘贴盒内位置文本录入
batch_copy_BoxPosition_input = (
    '.dialog-position-box-copy textarea')

# 批量粘贴盒内位置确认按钮
batch_copy_BoxPosition_comfirm = (
    '.dialog-position-box-copy .dialog-footer .baseClass-btn-confirm')

# 入库弹框下一步按钮
storage_next = (
    '.dialog-check-storage .el-dialog__footer button:nth-child(2)')



#提交状态文本定位
detail_sumbit_status=(
    '.createTask_content .vxe-table--main-wrapper .vxe-table--body-wrapper tbody tr:nth-child(1) td:nth-child({})')

# 样本列表滚动条
scroll_line = (
    '//*[@class="vxe-table--border-line"]')

# 保存结果按钮
detail_save_result = (
    '.createTask_content .row-bg button:nth-child(2)')

# 进入结果表按钮
enter_result_list_btn = (
    '.createTask_content .row-bg button:nth-child(3)')

"""
文库富集结果表元素定位
"""
# 样本列表数据全选按钮
result_all_choice = (
    '.createTask_content .show--head .vxe-table--fixed-left-wrapper .vxe-table--header-wrapper .vxe-checkbox--icon.vxe-checkbox--unchecked-icon')

# 批量导入数据按钮
result_batch_paste_import = (
    '.createTask_content .sampleDetail_header .button-list .enrichmentResults-btn-batchCopy')

# 批量粘贴导入弹框文本编辑框
result_batch_paste_import_package_textarea = (
    '.dialog-copy-data .el-dialog__body textarea')

# 明细表批量粘贴导入弹框确认按钮
result_batch_paste_import_package_comfirm = (
    '.dialog-copy-data .el-dialog__footer .baseClass-btn-confirm')

# 获取所有样本lims号
result_samples_lims = (
    '.createTask_content_table .vxe-table--fixed-left-wrapper .vxe-table--body-wrapper tbody tr:nth-child({}) td:nth-child(4)')

# 获取所有样本富集名称
result_enrichment_library_name = (
    '.createTask_content_table .vxe-table--fixed-left-wrapper .vxe-table--body-wrapper tbody tr:nth-child({}) td:nth-child(5)')




# 选中全部样本数量,用来计总数
result_samples_for_total = (
    '.createTask_content_table .vxe-table--fixed-left-wrapper .vxe-table--body-wrapper tbody tr')

# 选中全部样本，依次获取，用来对依次获取的样本进行表单数据录入
result_samples_all = (
    '.createTask_content_table .vxe-table--main-wrapper .vxe-table--body-wrapper tbody tr:nth-child({}) td:nth-child(13)')

#Pooling浓度1表单定位
consistenceAmtOne='.vxe-table--main-wrapper .vxe-table--body-wrapper table tbody tr:nth-child({}) .enrichmentResults-tableCol-consistenceAmtOne'
consistenceAmtOne_input='.vxe-table--main-wrapper .vxe-table--body-wrapper table tbody tr:nth-child(1) ' \
                   '.enrichmentResults-tableCol-consistenceAmtOne input'

#Pooling浓度2表单定位
consistenceAmtTwo='.vxe-table--main-wrapper .vxe-table--body-wrapper table tbody tr:nth-child({}) .enrichmentResults-tableCol-consistenceAmtTwo'
consistenceAmtTwo_input='.vxe-table--main-wrapper .vxe-table--body-wrapper table tbody tr:nth-child(1) ' \
                   '.enrichmentResults-tableCol-consistenceAmtTwo input'

#自动计算
result_automatic='//*[@class="button-list"]/descendant::span[text()="自动计算"]'

# 提交按钮
result_submit = (
    '.sampleDetail_header .button-list .baseClass-btn-submit')

#结果表是否已提交文本定位
result_sumbit_status='.createTask_content_table .vxe-table--main-wrapper .vxe-table--body-wrapper tbody tr:nth-child(1) td:nth-child(17)'

# 返回明细表
goback_detail = '.createTask_content .row-bg button:nth-child(1)'

# 返回明细表确认
goback_page_info = '.dialog-back .el-dialog__footer .baseClass-btn-next'

# 提交确认按钮
result_submit_comfirm = (
    '.dialog-result-commit .dialog-footer .baseclass-btn-confirm')

# 完成任务单按钮
result_complete_task_btn = (
    '.createTask_content .row-bg button:nth-child(3)')

# 完成任务单提示弹框确认按钮
result_complete_task_comfirm = (
    '//div[@class="el-message-box__wrapper"]/descendant::button[child::span][2]')

# 任务单号
task_id = (
    '//*[@class="el-card__header"]/div/div/div[2]/span[1]')

# 明细表任务单号
detail_task_id = (
    '.createTask .clearfix div span:nth-child(1)')

# 结果表任务单号
result_task_id = (
    '.createTask .clearfix div span:nth-child(1)')

# 任务单状态
task_status = (
    '.createTask .clearfix div span:nth-child(3)')
