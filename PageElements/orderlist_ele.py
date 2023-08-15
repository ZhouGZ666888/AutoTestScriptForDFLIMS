# -*- coding: utf-8 -*-
# @Time    : 2022/07/12
# @Author  : guanzhong.zhou
# @File    : 订单模块元素定位


# 搜索订单按钮，元素定位
search_order = '.app-main .baseClass-btn-search'

# 新增订单按钮，元素定位
add_order = '.baseClass-btn-add'

# 编辑订单按钮，元素定位
edit_order = '.baseClass-btn-edit'

# 搜索弹框订单号文本录入框
search_order_input = '.orderList-form-orderCode input'

# 搜索弹框确认按钮
search_order_comfirm = '.dialog-search .baseClass-btn-confirm'

# 订单列表第一条订单，
first_order = '.orderList .el-table__body-wrapper table tbody tr:nth-child(1)'

"""
新增弹框元素
"""
# 新增订单号输入框，元素定位
order_num_input = '.dialog-create .orderList-form-create-orderCode input'

# 患者姓名输入框，元素定位
patient_name_input = '.dialog-create .orderList-form-create-patientName input'

# 新增订单保存按钮，元素定位
add_confirm = '.dialog-create .baseClass-btn-create-confirm'

"""
编辑订单元素
"""
# 保存按钮，元素定位
save_button = '.app-main .baseClass-btn-save'

# 选择电子病历号文本框，元素定位
ele_patient_number = '.orderDetail-form-orderInfo-patientId input'
####选择病历弹框####


# 病历搜索项【用户名】
patient_name = '.orderDetail-form-medical-patientName input'

# 病历搜索项【身份证号】
identification_numb = ' .orderDetail-form-medical-identificationNoWildCard input'

# 病历搜索按钮
search_num_button = '.dialog-medical .baseClass-btn-medical-search'

# 选择已存在的、类似的关联病历
similar_case = '.dialog-medical .el-dialog__body .dialog_table .el-table__body-wrapper table tbody tr:nth-child(1)'

# 选择病历后确认按钮，元素定位
ele_chioce_confirm = '.baseClass-btn-medical-confirm'

# 选择关联病历后点击确认，弹出解除关联确认弹框，确认按钮，元素定位
chioce_and_confirm = '.el-message-box__wrapper .el-message-box__btns button:nth-child(2)'

####临床诊断信息####

# 临床诊断页面元素定位
crmPatientDiagnosisHistory = '.orderDetail-form-crmPatientDiagnosisHistoryT-diagnosisInfo textarea'

# 用药史文本框页面元素定位
crmPatientTreatmentHistory = '.orderDetail-form-crmPatientTreatmentHistoryT-drugName textarea'

# 是否有输血史
isBloodOrganTh = '.orderDetail-form-orderInfo-isBloodOrganTh input'

# 输血史下拉选择
isBloodOrganTh_choice = 'body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:nth-child(2)'

####联系人信息####
# 添加联系人按钮，元素定位
add_new_contact = '.baseClass-btn-contact-add'

# 联系人姓名，元素定位
contact_name = '.vxe-table--body-wrapper  tr:nth-child(1) .orderDetail-tableCol-contactName'
# 联系人姓名文本录入，元素定位
contact_name_input = '.vxe-table--body-wrapper  tr:nth-child(1) .orderDetail-tableCol-contactName input'

# 联系人电话表单定位
contact_tel_numb = '.vxe-table--body-wrapper  tr:nth-child(1) .orderDetail-tableCol-contactMobile'
# 联系人电话文本录入
contact_tel_numb_input = '.vxe-table--body-wrapper  tr:nth-child(1) .orderDetail-tableCol-contactMobile input'

# chioce_contact_county = "//span[containstext,'本溪市']"
# 联系人详细地址
contact_address = '.vxe-table--body-wrapper  tr:nth-child(1) .orderDetail-tableCol-addrCityCode'
# 联系人详细地址录入
contact_address_input = '.vxe-table--body-wrapper  tr:nth-child(1) .orderDetail-tableCol-addrCityCode input'

####选择送检医生弹框####

# 选择送检医生文本框，元素定位
chioce_physician = '.orderDetail-orderInfo-doctorName input'

# 医生列表根据科室查询
search_by_department = '.dialog-doctor .orderDetail-form-doctor-departmentName input'

# 录入查询条件后，查询按钮
physician_search_button = '.dialog-doctor .baseClass-btn-doctor-search'

# 选择查询结果，默认选中第一条
chioce_department = '.dialog-doctor .el-dialog__body .dialog_table .el-table__body-wrapper table tbody tr:nth-child(1)'

# 选择医生后确认按钮
chioce_physician_confirm = '.dialog-doctor .dialog-footer .baseClass-btn-doctor-confirm'




# 销售人员姓名，
sales_information = '.orderDetail-orderInfo-salesName input'

# 选择销售人员，默认选中第一条
chioce_sale = '.el-select-dropdown .el-select-dropdown__list li:nth-child(1) .name'

# 应收金额弹框文本
payment_due = '.orderDetail-orderInfo-paymentDue input'

# 修改后的金额
fee_after_amendment = '.orderDetail-form-sum-amend input'

# 修改理由
amendment_reason = '.orderDetail-form-sum-amend_cause textarea'

# 修改金额确认
change_fee_confirm = '.dialog-payment .el-dialog__footer .baseClass-btn-payment-confirm'

#结算方式
pay_style='.orderDetail-orderInfo-settlementMethod input'

#结算方式选择
pay_style_choice='//*[@class="el-select-dropdown el-popper"]/descendant::span[text()="科研"]'

# 保存成功提示信息
save_success_info = '.el-message.el-message--success'
