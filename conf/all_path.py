import os
import time

# ----------------*-------------------------
# 获取主目录路径
dir_name_file = os.path.dirname(os.path.abspath(__file__))  # 获取当前文件目录路径
# os.path.abspath(__file__)获取文件路径，脚本的完整路径
dir_name = os.path.dirname(dir_name_file)  # 当前工程路径

# ----------------*设置日志、截图、报告路径-----------------------
# 指定输出日志到目录
log_path = os.path.join(os.path.join(dir_name, "output"), 'logs')

# 指定输出图片到目录
img_path = os.path.join(os.path.join(dir_name, "output"), 'img')

# 指定输出截图文件到目录
today = time.strftime('%Y%m%d', time.localtime(time.time()))  # 按格式获取当前时间(精确到天)
fileshot = os.path.join(os.path.join(dir_name, "output"), '回归测试记录{}.docx').format(today)

# 测试报告文件路径
report_path = os.path.join(os.path.join(dir_name, "report"))
# ----------------*--conf文件夹数据-----------------------
# 指定用例路径
conffile_path = os.path.join(os.path.join(dir_name, "conf"))

# ----------------*--data文件夹数据-----------------------


# 测试数据data主路径
file_path = os.path.join(dir_name, "data")

# 指定用例路径
case_path = os.path.join(dir_name, "testcase")
# 指定用例路径
case_xls_path = os.path.join(file_path, '测试用例表.xlsx')

# 系统中生成、下载等临时文件存储路径
excel_doc_file_path = os.path.join(file_path, 'download_file')

# ===========================data/sql_data执行数据================================
report_views_refresh_sql = os.path.join(os.path.join(file_path, 'sql_data'),
                                        'report_view_refresh.txt')  # 配置文件路径

qpcr_task_refresh_sql = os.path.join(os.path.join(file_path, 'sql_data'),
                                     'qpcr_task_view_refresh.txt')  # 配置文件路径

# ===================data/yaml_doc执行数据=============================
# 配置文件路径
testdata_path = os.path.join(file_path, 'yaml_doc', 'logindata.yaml')

# 记录订单号和病历信息文件
order_medical_info_path = os.path.join(file_path, 'yaml_doc', 'OrderMedicalInfo.yaml')

# 临时记录数据
sampledata_path = os.path.join(file_path, 'yaml_doc', 'sampledata.yaml')

# 各实验流程存储明细表、结果表URL路径，以便浏览器直接调用直接访问
functionpageURL_path = os.path.join(file_path, 'yaml_doc', 'functionPage_url.yaml')

# 文库定量明细表，样本上机分组号临时数据
wkdl_sequencing_group_number = os.path.join(file_path, 'yaml_doc', 'wkdl_result_sequencing_group_number.yaml')

# mNGS复检出库样本记录(qpcr复检任务类型)
mNGTaskSampleId = os.path.join(file_path, 'yaml_doc', 'mngs_qpcr_sampleid.yaml')

# 数据修改模块，记录实验流程某一环节的结果表表URL地址，用于直接访问该环节，进行数据修改
dataChangFile = os.path.join(file_path, 'yaml_doc', 'dataChang.yaml')

# 样本外送模块数据记录文件，包含外送申请单号等
sampleOutDataFile = os.path.join(file_path, 'yaml_doc', 'sampleOutData.yaml')

# QPCR复检任务，记录样本的上机分组号
sjNubForQpcrFile = os.path.join(file_path, 'yaml_doc', 'sjNubForQpcr.yaml')

# ===================以下是测试流转数据用到的表格data/excel_doc=============================

# 病历号记录表
medicalNumb_file_path = os.path.join(file_path, 'excel_doc', 'medicalNumb_id_lims.xlsx')

# 订单号记录表
order_file_path = os.path.join(file_path, 'excel_doc', 'order_id_lims.xlsx')

# 样本处理结果记录表
sampleprocessing_file_path = os.path.join(file_path, 'excel_doc', 'sampleprocessing_id_lims.xlsx')

# 核酸提取结果记录表,mNGS对照样本
hstq_file_path_mNGS = os.path.join(file_path, 'excel_doc', 'hstq_id_lims_mNGS.xlsx')

# 核酸提取迪讯康对照样本记录表
hstq_file_path_dxk = os.path.join(file_path, 'excel_doc', 'hstq_id_lims_dxk.xlsx')

# 文库构建结果记录表
wkgj_file_path = os.path.join(file_path, 'excel_doc', 'wkgj_id_lims.xlsx')

# 文库富集结果记录表
wkfj_file_path = os.path.join(file_path, 'excel_doc', 'wkfj_id_lims.xlsx')

# 上机结果记录表
sj_file_path = os.path.join(file_path, 'excel_doc', 'sj_id_lims.xlsx')

# QPCR-mNGS复检
qpcr_mngs_file_path = os.path.join(file_path, 'excel_doc', 'qpcr_mngs_lims.xlsx')

# QPCR-迪讯康
qpcr_dxk_file_path = os.path.join(file_path, 'excel_doc', 'qpcr_dxk_lims.xlsx')

# QPCR-其他
qpcr_other_file_path = os.path.join(file_path, 'excel_doc', 'qpcr_other_lims.xlsx')

# 样本入库类型样本lims号
ybrk_file_path = os.path.join(file_path, 'excel_doc', 'ybrk_id_lims.xlsx')

# 报告模块基本信息处理，写入报告的上机和不上机样本记录表
report_basic_info_process_path = os.path.join(file_path, 'excel_doc', 'report_basic_info_process.xlsx')

# MPCR模块样本记录表
mpcr_file_path = os.path.join(file_path, 'excel_doc', 'mpcr_id_lims.xlsx')

# ===================以下是实验流转中，mpcr、富集报告、上机等模块批量粘贴导入数据用到的表格和执行自动化上传文件的可执行文件data/import_excel=============================
# mpcr结果表批量导入产物浓度
mpcr_result_consistence_amt_import_path = os.path.join(file_path, 'import_excel', 'df-mpcr结果表导入产物浓度.xlsx')

# 文库富集明细表批量导入数据
wkfj_detail_import_path = os.path.join(file_path, 'import_excel', 'df-文库富集-明细表批量粘贴导入.xlsx')

# 文库富集结果表批量导入数据
wkfj_result_import_path = os.path.join(file_path, 'import_excel', 'df-文库富集-结果表批量粘贴导入.xlsx')

# 上机结果表FC质控结果表导入
sj_fc_quality_control_result = os.path.join(file_path, 'import_excel', '上机-结果表导入模板E.xlsx')

# 新建病历时用户身份证文件
identificationNo_file_path = os.path.join(file_path, 'import_excel', '自动化脚本用户身份证.xlsx')

# 批量粘贴盒内位置导入文件
position_in_box_path = os.path.join(file_path, 'import_excel', 'position_in_box_lims.xlsx')
