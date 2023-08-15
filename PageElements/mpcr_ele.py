# -*- coding: utf-8 -*-
# @Time    : 2023/05/22
# @Author  : guanzhong.zhou
# @File    : mpcr页面元素定位
# -*-*************************************************************************************-*-


"""
MPCR首页元素定位
"""
# 搜索项lims号录入文本
search_lims_sample_num = (
    '.search-list >form>div>div:nth-child(5) input')
# 搜索按钮
search_btn = (
    '.search-list >div>button:nth-child(2)')
# 新增按钮
add_sample_MPCR_task = (
    '.table-list .baseClass-btn-add')
##页面列表样本
sample_page_list = (
    '.table-list .sample_receive_detail .vxe-table--main-wrapper .vxe-table--body-wrapper table tbody tr')
# -*-*************************************************************************************-*-


"""
MPCR待选表元素定位
"""
# 任务类型下拉选择框
task_type = '.task_info_form .select-task-type input'
# 任务类型下拉选择
task_type_choice = '//*[@class="el-select-dropdown el-popper task-type-unique"]/descendant::span[contains(text(),"结核耐药mPCR")]'

# 选择sop下拉框
task_sop = '.task_info_form .select-task-sopId input'
# 选项sop下拉选择
task_sop_choice = '.task-type-sopId .el-scrollbar .el-select-dropdown__wrap ul ul:nth-child(1) .el-select-group li:nth-child(1)'

# 操作方式下拉框
action_type = '.task_info_form .select-operation-type input'

# 操作方式点击下拉值
operationType_choice = '//*[@class="el-select-dropdown el-popper operation-type-unique"]/descendant::span[contains(text(),"人工")]'

# 核对lims样本号按钮
check_lims_sample_num = '.task_info_form .body-btns .commonTaskDetailNew-btn-judgeLims button'

# 核对样本号文本录入框
check_lims_sample_number_textarea = '//*[@aria-label="核对LIMS样本号"]/descendant::textarea'

# 核对lims样本号确认按钮，元素定位
check_lims_sample_number_confirm = '//*[@aria-label="核对LIMS样本号"]/descendant::button[span[contains(text(),"确 定")]]'

# 待选列表全选按钮
all_choice = '.vxe-table--main-wrapper .vxe-table--header-wrapper .vxe-header--row .vxe-checkbox--icon.vxe-checkbox--unchecked-icon'

# 加入选中&保存按钮，元素定位
addSelect_or_save_btn = '.head-list .commonTaskDetailNew-commonTaskDetailBtn-submit'

# 进入明细表按钮，元素定位
enter_detail_list_btn = '.head-list .commonTaskDetailNew-commonTaskDetailBtn-goSchedule'

# 页面成功提示信息
page_success_info = '//*[@class="el-message el-message--success"]/descendant::p'

"""
MPCR明细表元素定位
"""
# 明细表列表全选按钮
detail_all_choice = '.createTask_content .show--head .vxe-table--fixed-left-wrapper .vxe-table--header-wrapper .vxe-checkbox--icon.vxe-checkbox--unchecked-icon'

# 明细表自动计算按钮
detail_auto_complete = '.button-list .mpcr-btn-autoComplete'

# 明细表提交按钮
sumbit_btn = '.button-list .mpcr-btn-submit'

# 明细表提交弹框确认按钮
submit_comfirm = '.dialog-commit .dialog-footer button'

# 明细表保存按钮
detail_save_btn = '.button-list .mpcr-btn-save'

# 明细表任务单号
detail_task_id = '.header_test'

# *********************************入库****************************************
# 入库按钮
deposit_into_storage = '.button-list .mpcr-btn-deposit'

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
# ------------------------------------------------------------------

# 进入结果表按钮
go_result = '.head-list .baseClass-btn-goResults'


"""
MPCR结果表元素定位
"""
# 结果表全选按钮
result_all_choice = '.createTask_content .show--head .vxe-table--fixed-left-wrapper .vxe-table--header-wrapper .vxe-checkbox--icon.vxe-checkbox--unchecked-icon'

# 结果表lims号获取
result_all_samples = '.createTask_content_table .vxe-table--fixed-left-wrapper .vxe-table--body-wrapper table tbody tr td:nth-child(2) span'

# 结果表修改NTC对照
ntc_choice_btn = '.button-list .baseClass-btn-changeNtc'

# 结果表ntc查询
ntc_search = '//*[@aria-label="修改NTC对照"]/descendant::button[child::span[contains(text(),"搜索")]]'

# 结果表ntc选择
ntc_choice = '//*[@aria-label="修改NTC对照"]/descendant::tbody/tr[1]'

# 结果表ntc选择后保存
ntc_choice_confirm_btn = '//*[@aria-label="修改NTC对照"]/descendant::button[child::span[contains(text(),"保 存")]]'

# 结果表批量数据按钮
result_batch_data = '.button-list .baseClass-btn-handleBatchData'

# 结果表批量-mPCR产物包装量
sampl_package_amount = '.dialog-batch-data .mpcrResults-dialogBatchData-mpcr input'

# 结果表批量-包装单位
sampl_package_amount_unit = '.dialog-batch-data .mpcrResults-dialogBatchData-samplePkgAmtUnit input'

# 结果表批量-包装单位下拉选择
sampl_package_amount_unit_choice = '//*[@class="el-select-dropdown el-popper mpcrResults-samplePkgAmtUnit"]/descendant::li[span[text()="管"]]'

# 结果表批量-圆标签打印份数
circular_labels_print = '.dialog-batch-data .mpcrResults-dialogBatchData-noOfRoundLabels input'

# 结果表批量-长标签打印份数
long_labels_print = '.dialog-batch-data .mpcrResults-dialogBatchData-noOfLongLabels input'

# 结果表批量-循环数
number_cycles = '.dialog-batch-data .mpcrResults-dialogBatchData-loopNum input'

# 结果表批量-mPCR产物体积
volume_mPCR_product = '.dialog-batch-data .mpcrResults-dialogBatchData-volumeAmt input'

# 结果表批量-弹框确认按钮
batch_data_confirm_btn = '.dialog-batch-data .el-dialog__footer button:nth-child(2)'

# 结果表导入mPCR产物浓度
import_mpcr_consistence_amt = '.button-list .mpcrResult-btn-batchConsistenceAmt'

# 结果表导入mPCR产物浓度弹框文本录入框
import_mpcr_consistence_amt_input = '//*[@aria-label="导入mPCR产物浓度"]/descendant::textarea'

# 结果表导入mPCR产物浓度弹框确认按钮
import_mpcr_consistence_amt_confirm_btn = '//*[@aria-label="导入mPCR产物浓度"]/descendant::button[child::span[text()="确定"]]'

# 结果表批量粘贴盒内位置
batch_paste_position = '.button-list .baseClass-btn-batchPositionInBox'

# 结果表批量粘贴盒内位置弹框文本录入框
batch_paste_position_input = '//*[@aria-label="批量粘贴盒内位置"]/descendant::textarea'

# 结果表批量粘贴盒内位置弹框确认按钮
batch_paste_position_confirm_btn = '//*[@aria-label="批量粘贴盒内位置"]/descendant::button[child::span[text()="确定"]]'

# 结果表自动判读
result_auto_complete_btn = '.button-list .baseClass-btn-autoComplete'

# 结果表修改产物类型
product_type = '.button-list .baseClass-btn-changeResultType'

# 结果表选择产物类型
choice_product_type = '//*[@aria-label="修改产物类型"]/descendant::tbody/tr[1]'

# 结果表选择产物类型弹框确认按钮
choice_product_type_confirm = '//*[@aria-label="修改产物类型"]/descendant::button[child::span[contains(text(),"确 定")]]'

# 结果表选择产物类型确认提示弹框确认按钮
choice_product_type_tip = '.common-task-results-new > div:nth-child(3) .el-dialog__footer button:nth-child(2)'

# 结果表保存按钮
result_save_btn = '.button-list .mpcrResult-btn-save'

# 结果表提交完成
result_sumbit_btn = '.button-list .mpcrResult-btn-commit'

# 结果表提交确认
result_submit_comfirm = '.dialog-result-commit .el-dialog__footer button:nth-child(2)'

# 结果表任务单号
result_task_id = '.header_test'

#结果表样本提交状态
result_sample_status='.createTask_content_table .vxe-table--main-wrapper .vxe-table--body-wrapper table tbody tr:nth-child(1) td:nth-child(4) div div '

# 返回明细表
go_back = '.head-list .baseClass-btn-goSchedule'
# 返回上一步确认
go_back_confirm = '.dialog-back .el-dialog__footer .baseClass-btn-next'

# 完成任务单
result_complete_task_btn = '.head-list .baseClass-btn-completeTask'

# 任务单状态
result_task_status = '.header_status'
