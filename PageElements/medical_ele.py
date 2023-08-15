# -*- coding: utf-8 -*-
# @Time    : 2022/07/10
# @Author  : guanzhong.zhou
# @File    : 病历模块元素定位


"""列表页元素"""
# 搜索按钮，元素定位
search_btn = '.filter-container .baseClass-btn-search'
# 新增按钮，元素定位
add_btn ='.filter-container .baseClass-btn-add'
# 编辑按钮，元素定位
edit_btn ='.filter-container .baseClass-btn-edit'
# 查询框确认按钮，元素定位
search_sure_btn ='.baseClass-btn-confirm'
# 查询框电子病历号文本录入框，元素定位
search_medicalNum ='.medicalList-form-patientId input'
# 查询结果（取第一条）
search_result ='.el-table--medium .el-table__body-wrapper table tbody tr:nth-child(1)'

"""
患者信息
"""
# 参检人姓名，元素定位
Participants_name ='.medicalDetail-form-patientName input'
# 性别下拉框，元素定位
sex ='.medicalDetail-form-gender input'
# 未知性别
unknown_sex ='//*[@class="el-select-dropdown el-popper"]/descendant::li[following-sibling::li[child::span[text()="男性"]]]'
# 男性性别，元素定位
man_sex ='//*[@class="el-select-dropdown el-popper"]/descendant::li[child::span[text()="男性"]]'

# 女性性别，元素定位
woman_sex ='//*[@class="el-select-dropdown el-popper"]/descendant::li[child::span[text()="女性"]]'
# 身份号码，元素定位
identificationNo ='.medicalDetail-form-identificationNo input'





# 页面保存按钮，元素定位
save_btn ='.main-container .baseClass-btn-save'

# 保存成功结果提示语，元素定位
save_info ='//*[@class="el-message el-message--success"]/descendant::p'
prompt_msg ='//*[@class="el-message el-message--info"]/p'

#身份证信息与当前出生日期不符
brithday_error='.dialog-message .el-dialog__footer .baseClass-btn-continue-save'

# 身份证重复继续保存确认按钮，元素定位
continue_save_for_repeat ='.dialog-repeat .baseClass-btn-continue-save'

# 身份证信息与性别、出生日期不符,建档年龄与身份证信息不符，继续保存元素定位
continue_save ='.dialog-message .baseClass-btn-continue-save'

'''编辑页面元素'''
# 删除按钮
delete_btn ='.baseClass-btn-delete'

# 删除理由文本框
delete_reason ='.medicalDetail-form-reasonOfInvalid textarea'
# 删除理由确认按钮
delete_confirm ='.dialog-delete-reason .baseClass-btn-deleteReason-save'
# 删除页面，返回列表按钮
return_list ='.baseClass-btn-cancel'

loading = '//*[@class="el-loading-spinner"]/descendant::p[text()="Loading"]'