# -*- coding: utf-8 -*-
# @Time    : 2021/11/25
# @Author  : guanzhou.zhou
# @File    : 盒位管理元素定位
# -*-*************************************************************************************-*-

# -*-*****************列表页搜索元素定位# *****************-*-
"""
盒位管理列表页，搜索功能
"""
#列表页搜索按钮
hwgl_list_search_button=(
    '//*[@class="el-button filter-item baseClass-btn-search el-button--primary el-button--medium"]')

#列表页搜索按钮,搜索弹框中，盒子输入框
hwgl_list_search_box_name=(
    '//*[@class="dialogBoxSearch-form-boxName el-input el-input--medium el-input-group el-input-group--prepend el-input--suffix"]//input')

#搜索弹框中，点击确认按钮
hwgl_list_search_confirm=(
    '//*[@class="el-button baseClass-btn-confirm el-button--primary el-button--medium"]')

"""
盒位管理列表页，删除功能
"""
#列表中，选择一个盒子
hwgl_list_first_data=(
    '//*[@class="el-table__body-wrapper is-scrolling-none"]//descendant::td[1]')
#列表中，选择删除按钮
hwgl_list_detel=(
    '//*[@class="el-button filter-item baseClass-btn-delete el-button--primary el-button--medium"]')

#如果有盒子里有样本，系统会toast提示不能删，这个提示元素为
hwgl_list_detel_toast=(
    '//*[@class="el-message__content"]')

#删除弹框中，填入删除理由，点击确定
hwgl_list_detel_reason=(
    '//*[@class="dialogDelete-form-invalidReason el-textarea el-input--medium"]//textarea')
hwgl_list_detel_confirm=(
    '//*[@class="el-button baseClass-btn-confirm el-button--primary el-button--medium"]')

"""
盒位管理列表页，新增功能
"""

#新增按钮
hwgl_list_add_button=('//*[@class="el-button filter-item baseClass-btn-add el-button--primary el-button--medium"]')




#点击输入框后，输入盒子名称信息
hwgl_detail_box_name_value=('//*[@class="dialogSave-form-boxName el-input el-input--medium el-input-group el-input-group--prepend el-input--suffix"]//input')
#点击选择样本盒规格的输入框
hwgl_detail_box_size=('//*[@class="el-input el-input--medium el-input--suffix"]//input')

#下拉框弹框后，选择指定的规格
hwgl_detail_box_size_value=('//*[@class="el-select-dropdown__wrap el-scrollbar__wrap"]//li[@class="el-select-dropdown__item" and span[contains(.,"9*9")]]')
#下拉框弹框后，选择指定的规格,点击确定按钮
hwgl_detail_box_add_confirm=('//*[@class="el-button baseClass-btn-save el-button--primary el-button--medium"]//span')












