# -*- coding: utf-8 -*-
# @Time    : 2022/02/09
# @Author  : guanzhong.zhou
# @File    : 样本项目信息修改元素定位
# -*-*************************************************************************************-*-
"""
样本项目信息修改首页列表元素定位
"""
# 搜索按钮
search = (
    '.app-container .filter-container .baseClass-btn-search')

# 搜索弹框lims号录入文本
search_lims_sample_num = (
    '.dialog-search .el-dialog__body > form >div:nth-child(2) >div:nth-child(2) input')

# 搜索弹框实验室号录入文本
search_labrary_sample_num = (
    '.dialog-search .el-dialog__body > form >div:nth-child(2) >div:nth-child(1) input')

# 搜索弹框确认
search_confirm = (
    '.dialog-search .el-dialog__footer .baseClass-btn-search')

# 新增按钮
add_task = (
    '.app-container .filter-container .baseClass-btn-create')

##页面列表样本
sample_page_list = (
    '.project-table .el-table__body-wrapper tbody tr')

# -*-*************************************************************************************-*-

"""
新建
"""
# -修改理由文本录入框
change_reason = (
    '.dialog-createTask textarea')

# 修改理由弹框，下一步按钮
next_step = (
    '.dialog-createTask .el-dialog__footer .baseClass-btn-next')

#选择待修改样本-按lims号检索tab页
search_by_lims_tab=(
    '.dialog-closeStep1 #tab-0')

# 选择待修改样本-按lims号检索文本录入框
search_by_lims = (
    '#pane-0 textarea')

#选择待修改样本-按实验室号检索tab页
search_by_labCode_tab=(
    '.dialog-closeStep1 #tab-1')

# 选择待修改样本-按实验室号检索文本录入框
search_by_labCode = (
    '#pane-1 textarea')

# 选择待修改样本-下一步按钮
search_sample_comfirm = (
    '.dialog-closeStep1 .el-dialog__footer .baseClass-btn-next')

# 项目信息确认/修改/提交弹框，导出按钮
download_sampleInfo_btn = (
    '.dialog-closeStep2 .export-btn')

#项目信息确认/修改/提交弹框，下一步按钮
download_sampleInfo_comfirm = (
    '.dialog-closeStep2 .el-dialog__footer .el-button--primary')

#项目信息确认/修改/提交，导入按钮
upload_sampleInfo_btn=(
    '.dialog-closeStep3 .upload-project input')

#项目信息确认/修改/提交，提交修改任务单
sampleProjectInfo_submit=(
    '.dialog-closeStep3 .el-dialog__footer .baseClass-btn-submit')

# 页面成功提示信息
page_success_info = (
    '//*[@class="el-message el-message--success"]')