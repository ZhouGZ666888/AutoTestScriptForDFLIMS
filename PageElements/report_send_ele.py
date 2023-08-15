# -*- coding: utf-8 -*-
# @Time    : 2022/09/27
# @Author  : guanzhong.zhou
# @File    : 报告发送页面元素定位
# -*-*************************************************************************************-*-

# 筛选条件，订单号文本录入框元素定位
order_num = (
    '.reportSend-form-orderCode input')

# 筛选条件，订单号文本录入框
order_num_input = '.orderID-form-textareaValue textarea'

# 录入筛选条件确认按钮
order_num_input_confirm = '.dialog-orderID .dialog-footer .baseClass-btn-confirm'
# 筛选条件，报告完成日期
reportSend_form_completeDate = (
    '.reportSend-form-completeDate input')

# 筛选按钮
search_btn = (
    '.sarch-button-list .baseClass-btn-filter')

# 保存按钮
save_btn = (
    '.sarch-button-list .reportSend-btn-saveReport')

# 下载所选报告按钮
downloadAll_btn = (
    '.search-button-list .reportSend-btn-downloadAll')

# 全选按钮
all_choice = (
    '.reportSend-table .vxe-table--main-wrapper .vxe-table--header-wrapper .vxe-checkbox--icon.vxe-checkbox--unchecked-icon')

# 筛选结果
search_result = (
    '//*[@class="vxe-table--main-wrapper"]/descendant::tbody/tr')

# 表单审核状态表单定位
audit_status = (
    '//*[@class="vxe-table--main-wrapper"]/descendant::tbody/tr[1]/td[9]')

# 表单审核状态下拉定位
audit_status_select = (
    '//*[@class="vxe-table--main-wrapper"]/descendant::tbody/tr[1]/td[9]/div/div')

# 表单审核状态选择---已审核
audit_status_choice = (
    '/html/body/div[last()]/descendant::li[child::span[text()="已审核"] ]')
# 重置按钮
reset_btn = (
    '.sarch-button-list .baseClass-btn-reset')

# 页面提示信息，元素定位
page_info = (
    '//*[@class="el-message el-message--success"]')
