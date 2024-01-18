# -*- coding: utf-8 -*-
# @Time    : 2024/01/11
# @Author  : guanzhong.zhou
# @File    : 文库定量页面元素定位
# -*-*************************************************************************************-*-


"""
文库定量首页元素定位
"""
# 搜索项lims号录入文本
search_lims_sample_num = '.search-list .commonTaskList-form-sampleIdLims input'
# 搜索按钮
search_btn ='.search-list-btns .baseClass-btn-dialog-search'

# 新增按钮
add_sample_task = '.table-list .baseClass-btn-add'
##页面列表样本
sample_page_list = (
    '.table-list .sample_receive_detail .vxe-table--main-wrapper .vxe-table--body-wrapper table tbody tr')
# -*-*************************************************************************************-*-

"""
文库定量待选表元素定位
"""
# 选择sop下拉框
task_sop = '.task_info_form .select-task-sopId input'
# 选项sop下拉选择
task_sop_choice = '.task-type-sopId .el-scrollbar .el-select-dropdown__wrap ul ul:nth-child(1) .el-select-group li:nth-child(1)'

# 核对lims样本号按钮
check_lims_sample_num = '.task_info_form .body-btns .commonTaskDetailNew-btn button'

# 核对样本号文本录入框
check_lims_sample_number_textarea = '//*[@aria-label="核对LIMS样本号"]/descendant::textarea'

# 核对lims样本号确认按钮，元素定位
check_lims_sample_number_confirm = '.dialog-match .el-dialog__footer .sampleId-btn-confirm'

# 待选列表全选按钮
all_choice = '.vxe-table--main-wrapper .vxe-table--header-wrapper .vxe-header--row .vxe-checkbox--icon.vxe-checkbox--unchecked-icon'

# 加入选中&保存按钮，元素定位
addSelect_or_save_btn = '.head-list .commonTaskDetailNew-commonTaskDetailBtn-submit'

# 进入明细表按钮，元素定位
enter_detail_list_btn = '.head-list .commonTaskDetailNew-commonTaskDetailBtn-goSchedule'

# 页面成功提示信息
page_success_info = '//*[@class="el-message el-message--success"]/descendant::p'

"""
文库定量明细表元素定位
"""
# 明细表列表全选按钮
detail_all_choice = '.createTask_content .show--head .vxe-table--fixed-left-wrapper .vxe-table--header-wrapper .vxe-checkbox--icon.vxe-checkbox--unchecked-icon'

#明细表全部样本总数
detail_all_samples='.createTask_content_table .vxe-table--main-wrapper .vxe-table--body-wrapper table tbody tr'


#定量混合产物名称表单定位
quantifying_mix_product_name='.createTask_content_table .vxe-table--main-wrapper .vxe-table--body-wrapper table tbody tr:nth-child({}) td:nth-child(6)'

#定量混合产物名称表单录入
quantifying_mix_product_name_input='.createTask_content_table .vxe-table--main-wrapper .vxe-table--body-wrapper table tbody tr:nth-child({}) td:nth-child(6) input'

#定量明细表生成结果按钮
create_result='//*[@class="button-list"]/descendant::span[text()="生成结果"]'

#定量明细表index重复判定提示
create_result_tips='.common-task-schedule-new > div:nth-child(12)'
#定量明细表index重复判定提示确认按钮
create_result_tips_btn='.common-task-schedule-new > div:nth-child(12) .el-dialog__footer .baseClass-btn-confirm'

# 明细表自动计算按钮
detail_auto_complete = '.button-list .btn-autoComplete'

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
文库定量结果表元素定位
"""
# 结果表全选按钮
result_all_choice = '.createTask_content .show--head .vxe-table--fixed-left-wrapper .vxe-table--header-wrapper .vxe-checkbox--icon.vxe-checkbox--unchecked-icon'

# 结果表样本总数
result_all_samples = '.createTask_content_table .vxe-table--fixed-left-wrapper .vxe-table--body-wrapper table tbody tr'

#定量混合产物体积表单定位
quantifying_mix_product_vol='.createTask_content_table .vxe-table--main-wrapper .vxe-table--body-wrapper table tbody tr:nth-child({}) td:nth-child(4)'

#定量混合产物体积表单录入
quantifying_mix_product_vol_input='.createTask_content_table .vxe-table--main-wrapper .vxe-table--body-wrapper table ' \
                              'tbody tr:nth-child({}) td:nth-child(4) input'

#定量混合产物浓度表单定位
quantifying_mix_product_consistenceAmt='.createTask_content_table .vxe-table--main-wrapper .vxe-table--body-wrapper ' \
                                       'table tbody tr:nth-child({}) td:nth-child(5)'

#定量混合产物浓度表单录入
quantifying_mix_product_consistenceAmt_input='.createTask_content_table .vxe-table--main-wrapper ' \
                                          '.vxe-table--body-wrapper table tbody ' \
                            'tr:nth-child({}) td:nth-child(5) input'

#定量混合产物总量表单定位
quantifying_mix_product_total='.createTask_content_table .vxe-table--main-wrapper .vxe-table--body-wrapper table ' \
                              'tbody ' \
                            'tr:nth-child({}) td:nth-child(6)'

#定量混合产物总量表单录入
quantifying_mix_product_total_input='.createTask_content_table .vxe-table--main-wrapper .vxe-table--body-wrapper ' \
                                    'table tbody ' \
                            'tr:nth-child({}) td:nth-child(6) input'


# 结果表保存按钮
result_save_btn = '.button-list .mpcrResult-btn-save'

# 结果表提交完成
result_sumbit_btn = '.button-list .mpcrResult-btn-commit'

# 结果表提交确认
result_submit_comfirm = '.dialog-result-commit .el-dialog__footer button:nth-child(2)'

# 结果表任务单号
result_task_id = '.header_test'

#结果表样本提交状态
result_sample_status='.createTask_content_table .vxe-table--main-wrapper .vxe-table--body-wrapper table tbody tr:nth-child(1) td:nth-child(12)'

# 返回明细表
go_back = '.head-list .baseClass-btn-goSchedule'
# 返回上一步确认
go_back_confirm = '.dialog-back .el-dialog__footer .baseClass-btn-next'

# 完成任务单
result_complete_task_btn = '.head-list .baseClass-btn-completeTask'

# 任务单状态
result_task_status = '.header_status'
