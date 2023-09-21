# -*- coding: utf-8 -*-
# @Time    : 2023/09/20
# @Author  : guanzhou.zhou
# @File    : samplesheet元素定位
# -*-*************************************************************************************-*-

# ***************samplesheet列表元素***************
# 搜索按钮
search = '.filter-container .baseClass-btn-search'

# 搜索弹框【上机任务单号】文本录入框
sj_taskid = '.dialog-search .search-form-taskId input'

# 搜索弹框【确认】按钮
search_confirn = '.dialog-search .baseClass-btn-search'

# 查看编辑按钮
edit_btn = '.filter-container .baseClass-btn-view'

# 搜索结果列表选择
search_result='.el-table__body-wrapper tbody tr:nth-child(1)'

# 数据表单-【是否可用】字段
is_available = ''

# 【是否可用】下拉框
is_available_input = ''

# 【是否可用】下拉值
is_available_choice = ''

# 【查看修改记录】按钮
modify_record = '.el-card__body .btn-view-modify'

# 【查看修改记录】弹框，【导出】按钮
modify_record_upload = ''

# 【查看修改记录】弹框，表单数据
modify_record_data='.record-dialog .el-table__body-wrapper tr'

# 【查看修改记录】弹框，【关闭】按钮
modify_record_close = ''

# 【保存&生成新版本】按钮
save_generate_new_version = '.detail-btn-saveDetail'

# 【保存&生成新版本】弹框，【修改原因及内容】文本输入框
reason_for_modification = '.version-dialog .changeReason-text textarea'

# 【保存&生成新版本】弹框，【确认生成新版本】按钮
reason_for_modification_confirn = '.version-dialog .changeReason-text-confirm'

# 【导出csv】按钮
download_csv_btn = '.detail-btn-exportCSV'

# 【导入csv】按钮
import_csv_btn = '.detail-btn-importCSV'

# 弹框上传标签
samples_upload = (
    '.dialog-upload-visible1 .el-upload--text input')

#【导入csv】弹框确认
download_csv_confirm='.dialog-upload-visible1 .el-dialog__footer .baseClass-btn-upload'

# 页面提示信息，元素定位
page_info = (
    '//*[@class="el-message el-message--success"]')
