# -*- coding: utf-8 -*-
# @Time    : 2022/09/22
# @Author  : guanzhong.zhou
# @File    : 报告---qpcr复检任务页面元素定位
# -*-*************************************************************************************-*-

# 筛选条件，上机号文本录入框元素定位
seqSampleIdLabs_input = (
    '.createTask_content .taskCreated-form-seqSampleIdLabs input')

# 筛选按钮
search_btn = (
    '.createTask_content .baseClass-btn-filter')

# 批量出库按钮
multiple_out = (
    '.createTask_content .baseClass-btn-qpcr-multiple-out')

# 样本信息
all_orders = (
    '.createTask_content .vxe-table--main-wrapper .vxe-table--body-wrapper table tbody tr:nth-child(1) td:nth-child({})')

