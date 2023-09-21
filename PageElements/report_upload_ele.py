# -*- coding: utf-8 -*-
# @Time    : 2022/09/19
# @Author  : guanzhong.zhou
# @File    : 报告上传页面元素定位
# -*-*************************************************************************************-*-

# 筛选条件，订单号文本录入框元素定位
order_num = '.reportUpload-form-orderCode input'

# 筛选按钮
search_btn = '.search-card .baseClass-btn-filter'

# 所有样本数量
all_samples = '.sample_receive_detail .vxe-table--fixed-left-wrapper .vxe-table--body-wrapper table tbody tr'

# 实验室样本编号单条表单
one_sample_lab = '.sample_receive_detail .vxe-table--fixed-left-wrapper .vxe-table--body-wrapper table tbody tr:nth-child({}) td:nth-child(2) a'

#获取上机分组号
sj_group_nub='.dialog-report-file .vxe-table--main-wrapper .vxe-table--body-wrapper table tbody tr:nth-child(1) td:nth-child(2)'

# 标记出报告样本星星勾选按钮
sample_report_tab = '.dialog-report-file .el-dialog__body .vxe-table--main-wrapper .vxe-table--body-wrapper table tbody tr:nth-child(1) td .star i'

# 关闭标记出报告样本
close_table = '.dialog-report-file .el-dialog__header button '

# 报告形式下拉框
report_style_form = '.sample_receive_detail .vxe-table--main-wrapper .vxe-table--body-wrapper table tbody tr:nth-child({}) .reportUpload-tableCol-reportStyle'

# 报告形式下拉按钮
report_style_btn = '.sample_receive_detail .vxe-table--main-wrapper .vxe-table--body-wrapper table tbody tr:nth-child({}) .reportUpload-tableCol-reportStyle input'

# 报告形式下拉值选择
report_style_choice = '//body/div[@class="el-select-dropdown el-popper"]/descendant::span[text()="收费报告"]'

# 报告文件编辑按钮
report_file_edit = '.sample_receive_detail .vxe-table--main-wrapper .vxe-table--body-wrapper table tbody tr:nth-child({}) .baseClass-btn-report-file-edit'

# 报告文件上传按钮
report_upload_btn = (
    '.dialog-upload-file div:nth-child(2) .el-upload input')

#提示确认1
info_confirm1='.el-message-box__wrapper .el-message-box__btns button:nth-child(2)'
#提示确认2
info_confirm2='.el-message-box__wrapper .el-message-box__btns button:nth-child(2)'
# 解读文件上传按钮
decode_upload_btn = (
    '.dialog-upload-file div:nth-child(3) .el-upload input')

# 其他文件上传按钮
other_upload_btn = (
    '.dialog-upload-file div:nth-child(4) .el-upload input')

# 报告文件上传弹框确认按钮
report_upload_comfirm = (
    '.dialog-upload-file .el-dialog__footer .baseClass-btn-confirm')

# 报告任务操作完成按钮
report_task_complete = '.sample_receive_detail .vxe-table--main-wrapper .vxe-table--body-wrapper table tbody tr:nth-child({}) .baseClass-btn-task-operation'

# QPCR复检任务新建按钮
qpcr_task_add_btn = '.sample_receive_detail .vxe-table--main-wrapper .vxe-table--body-wrapper table tbody tr:nth-child({}) .baseClass-btn-add-qpcr'

# 新建QPCR复检任务弹框-当日批次下拉框
report_belong_input = '.dialog-qpcr-recheck .el-dialog__body .qpcrReCheckDialog-form-dayBatchNo input'

# 新建QPCR复检任务弹框-当日批次下拉值选择
report_belong_choice = '//*[@class="el-select-dropdown el-popper"]/descendant::ul[@class="el-scrollbar__view el-select-dropdown__list"]/li/span[text()="1"]'

#样本要求下拉框
sample_style='.qpcrReCheckDialog-form-sampleTypeReq input'

#样本要求值下拉选择
sample_style_choice='//*[@class="el-select-dropdown el-popper"]/descendant::li[child::span[text()="核酸样本"]]'

#复检任务类型选择下拉框
qpcr_task_type='.qpcrReCheckDialog-form-taskType input'

#复检任务类型选择
qpcr_task_type_choice1='//span[contains(text(),"单物种")]'
qpcr_task_type_choice2='//span[contains(text(),"甲乙流")]'
qpcr_task_type_choice3='//span[contains(text(),"新冠")]'
qpcr_task_type_choice4='//span[contains(text(),"呼六")]'
# 添加菌种按钮
add_qpcr_basbacteria_btn = '.dialog-qpcr-recheck .el-dialog__body .baseClass-btn-add-qpcr-basbacteria-info'

# 添加菌种
add_qpcr_basbacteria = '//span[contains(text(),"大肠埃希菌")]/preceding-sibling::label/span'

# 添加菌种弹框确认按钮
add_qpcr_basbacteria_choice = 'body >div> .qpcrBasBacteriaInfoSearch .el-dialog__footer .baseClass-btn-confirm'

# 生成复检任务按钮
create_qpcr_task_btn = '.dialog-qpcr-recheck .el-dialog__footer .baseClass-btn-sure-01'

# 页面提示信息，元素定位
page_info = (
    '//*[@class="el-message el-message--success"]')
