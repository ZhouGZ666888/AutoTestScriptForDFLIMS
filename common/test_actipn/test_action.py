import time,os
import pandas as pd
from conf.all_path import excel_doc_file_path


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


if __name__ == '__main__':
    test02()