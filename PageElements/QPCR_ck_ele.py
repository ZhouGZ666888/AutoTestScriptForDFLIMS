# -*- coding: utf-8 -*-
# @Time    : 2022/09/09
# @Author  : guanzhou.zhou
# @File    : 流转表元素定位
# -*-*************************************************************************************-*-

# ===================样本出库的元素如下===========================


"""
样本出库列表页的元素---QPCR出库元素
"""
# 新建QPCR出库单
add_qpcr = '.filter-container .baseClass-btn-add-qpcr'

# QPCR出库样本录入
qpcr_sample_input = '.dialog-text-input .textInputDialog-form-packet textarea'

# QPCR出库样本录入,确定按钮
qpcr_sample_input_confirm = '.dialog-text-input .el-dialog__footer .baseClass-btn-confirm'

# 切换到核酸提取table页
get_table = '.dialog-qpcr-sample-out #tab-extraction'

# QPCR出库页面样本全选按钮
qpcr_all_chioce = '.dialog-qpcr-sample-out .el-tabs__content #pane-extraction .vxe-table--main-wrapper .vxe-table--header-wrapper .vxe-checkbox--icon.vxe-checkbox--unchecked-icon'

# QPCR检测菌种选择按钮
qpcr_check_bacteria_btn = '.dialog-qpcr-sample-out .el-tabs__content #pane-extraction .baseClass-btn-check-bacteria'

# 选择菌种
choice_bacteria = '.multi-table-dialog .vxe-table--main-wrapper table tbody tr:nth-child({}) .multi-table-tableCol-bacteriaName'

# 选择菌种确认
choice_bacteria_confirm = '//*[@aria-label="添加检测菌种"]/descendant::button[3]'

# 选择菌种后，保存全部，下一步按钮
save_and_last = '.dialog-qpcr-sample-out .el-dialog__footer .baseClass-btn-next-step'

# qpcr填写出库理由
qpcr_out_reason = '.qpcrSampleOut .dialog-out-storage .qpcrSampleOut-form-reasonOfWithdraw textarea'

# 填写出库理由确认
qpcr_out_reason_confirm = '.qpcrSampleOut .dialog-out-storage .el-dialog__footer .baseClass-btn-confirm'

# QPCR出库后生成节点提示信息（请确认本次出库的建库节点的样本配置了正确的建库类型）
sample_info = '.el-message-box__wrapper .el-message-box__container .el-message-box__message p'

# QPCR出库后生成节点提示信息确认按钮
sample_info_confirm = '.el-message-box__wrapper .el-message-box__btns button'


#输入错误样本号后，系统提示弹框，确认按钮
error_sample_confirm='.el-message-box__wrapper .el-message-box__btns button'

#QPCR样本出库取消按钮
cannel_btn='.dialog-qpcr-sample-out > div:nth-child(3) >span >button'