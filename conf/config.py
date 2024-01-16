# 各模块配置信息
# *************#
from conf.all_path import sampleprocessing_file_path, hstq_file_path_mNGS, wkgj_file_path, hstq_file_path_dxk, \
    wkfj_file_path, sj_file_path, qpcr_mngs_file_path, qpcr_dxk_file_path, qpcr_other_file_path, ybrk_file_path, \
    report_basic_info_process_path, mpcr_file_path, wkdl_file_path, wkfj_probe_file_path
from common.xlsx_excel import write_excel_xlsx_by_openpyxl

# 样本接收模块生成样本数量
# specimen_list = {'DNA': 4, '迪迅康-基础(8)': 3,'DNA+耐药':3}
specimen_list = {'DNA': 20, '迪迅康-基础(8)': 10,'DNA+耐药':5}

"""
数据库配置
"""
# 表名

# 样本处理结果表
preparation_result = 'exp_preparation_result_t'

# 提取结果表
extraction_result = 'exp_extraction_result_t'

# mpcr结果表
exp_mpcr_result_t = 'exp_mpcr_result_t'

# 构建结果表
libconstruction_result = 'exp_libconstruction_result_t'

# 富集结果表
pooling_result = 'exp_pooling_result_t'

# 定量结果表
libquant_result = 'exp_libquant_result_t'


def create_lab_excel():
    """
    新建各实验节点的Excel记录结果表样本下一步流程
    """
    all_laboratorys = ['样本处理', '核酸提取', '文库构建', '文库富集', '上机', 'QPCR-mNGS复检', '迪讯康-QPCR', '其他-QPCR', '样本入库',
                       '写入报告样本', '核酸提取-迪讯康样本','富集有探针','MPCR','文库定量']
    value = [["lims号", "实验室号", "当前节点", "任务单号"]]  # 其他
    value4 = [["lims号", "实验室号", "报告类型", "任务单号"]]  # 其他
    value1 = [["上机用LIMS号", "上机分组号", "当前节点", "任务单号"]]  # 上机

    write_excel_xlsx_by_openpyxl(sampleprocessing_file_path, all_laboratorys[0], value4)  # 样本处理数据流转Excel
    write_excel_xlsx_by_openpyxl(hstq_file_path_mNGS, all_laboratorys[1], value)  # 核酸提取mNGS对照样本数据流转Excel
    write_excel_xlsx_by_openpyxl(wkgj_file_path, all_laboratorys[2], value)  # 文库构建数据流转Excel
    write_excel_xlsx_by_openpyxl(hstq_file_path_dxk, all_laboratorys[10], value4)  # 核酸提取-迪讯康样本流转Excel
    write_excel_xlsx_by_openpyxl(wkfj_file_path, all_laboratorys[3], value)  # 文库富集样本数据流转Excel
    write_excel_xlsx_by_openpyxl(sj_file_path, all_laboratorys[4], value1)  # 上机数据流转Excel
    write_excel_xlsx_by_openpyxl(qpcr_mngs_file_path, all_laboratorys[5], value)  # QPCR-mNGS复检数据流转Excel
    write_excel_xlsx_by_openpyxl(qpcr_dxk_file_path, all_laboratorys[6], value)  # 迪讯康-QPCR数据流转Excel
    write_excel_xlsx_by_openpyxl(qpcr_other_file_path, all_laboratorys[7], value)  # 其他-QPCR数据流转Excel
    write_excel_xlsx_by_openpyxl(ybrk_file_path, all_laboratorys[8], value)  # 样本入库数据流转Excel
    write_excel_xlsx_by_openpyxl(report_basic_info_process_path, all_laboratorys[9], value)  # 写入报告样本数据流转Excel
    write_excel_xlsx_by_openpyxl(mpcr_file_path, all_laboratorys[-2], value)  # mPCR数据流转Excel
    write_excel_xlsx_by_openpyxl(wkdl_file_path, all_laboratorys[-1], value)  # 文库定量数据流转Excel
    write_excel_xlsx_by_openpyxl(wkfj_probe_file_path, all_laboratorys[-3], value)  # 文库富集有探针数据流转Excel

if __name__ == '__main__':
    create_lab_excel()