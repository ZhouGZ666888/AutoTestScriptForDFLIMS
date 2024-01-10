import time,os

import openpyxl
import pandas as pd
from openpyxl import Workbook
from common.DataBaseConnection import executeSql
from common.xlsx_excel import pandas_write_excel
from conf.all_path import excel_doc_file_path, index_96_import
from conf.execute_sql_action import wkgj_detail_sql3


def test01():
    str_time = time.strftime("%m_%d")+'_samplesheet'
    print(str_time)
def test02():
    lists = os.listdir(excel_doc_file_path)
    lists.sort(key=lambda fn: os.path.getmtime(excel_doc_file_path + '\\' + fn))
    filepath = os.path.join(excel_doc_file_path, lists[-1])
    print(filepath)
    df = pd.read_csv(filepath, encoding='utf-8')
    df.loc[:, 'Description'] = 'samplesheetTest'  # 把读取的实验室号写入到突变模板中
    df.to_csv(filepath, index=False, encoding='utf-8')

def test03():
    lims_list = executeSql.test_select_limsdb(
        wkgj_detail_sql3.format("WKGJD2024010900006"))  # 从数据库获取当前任务单号下样本lims号
    values_list=[list(d.values()) for d in lims_list]
    new_list = [[i + 1] + item + [i + 1] for i, item in enumerate(values_list)]
    print(new_list)
    workbook = openpyxl.load_workbook(index_96_import)
    worksheet = workbook.active
    for row_index, row_data in enumerate(new_list, start=2):
        for column_index, cell_value in enumerate(row_data, start=1):
            worksheet.cell(row=row_index, column=column_index, value=cell_value)
    workbook.save(index_96_import)

if __name__ == '__main__':
    test03()