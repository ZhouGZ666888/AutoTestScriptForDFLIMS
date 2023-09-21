# -*- coding: utf-8 -*-
# @Time    : 2022/11/25
# @Author  : guanzhou.zhou
# @File    : 盒位管理元素定位
# -*-*************************************************************************************-*-


"""
库位管理列表页，新增功能
"""

#列表页新增按钮（临时库）
kwgl_list_add_ls_button='.filter-container .baseClass-btn-add'

#新增临时库，点击输入库位名称
kwgl_list_add_ls_name='.dialogSave00-form-storageName input'

#新增临时库，下拉框选择库位位置
kwgl_list_add_ls_location_select='.dialogSave00-form-positionCode input'

#新增临时库，下拉框选择库位位置，这里我们指定A7位置
kwgl_list_add_ls_location='//*[@class="el-scrollbar__view el-select-dropdown__list"]//descendant::li//span[text()="A7"]'

#新增临时库，这里我们位置描述信息
kwgl_list_add_ls_location_desc='.dialogSave00-form-positionDesc input'

#新增临时库，添加使用人信息,编辑按钮
kwgl_list_add_ls_user='.baseClass-btn-user-01'

#新增临时库，添加使用人信息,编辑按钮，输入使用人姓名
kwgl_list_add_ls_username='.dialogUsers-form-usernameCn input'

#输入使用人姓名后选择联想结果
kwgl_list_add_ls_username_search='//*[@class="el-scrollbar__view el-autocomplete-suggestion__list"][1]'


#新增临时库，添加使用人信息,编辑按钮，输入使用人姓名,点击添加按钮
kwgl_list_add_ls_username_add_butoon='.dialog-users .baseClass-btn-add-line'

#新增临时库，输入姓名后，点击确定
kwgl_list_add_ls_username_add_confirmn='.dialog-users .el-dialog__footer .baseClass-btn-confirm'

#新增临时库，所有信息填写完毕后，点击确定按钮
kwgl_list_add_ls_confirm='.dialog-save-00 .el-dialog__footer .baseClass-btn-save'


"""
库位管理列表页，搜索功能
"""

#列表页，点击搜索按钮
kwgl_list_search_button='.filter-container .baseClass-btn-search'

#搜索弹框中，输入指定库位信息
kwgl_list_search_name='.dialog-search .dialogSearch-form-storageName input'

kwgl_list_search_confirm='.dialog-search .el-dialog__footer .baseClass-btn-confirm'








