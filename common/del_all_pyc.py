from conf.all_path import file_path
import os

def del_pyc(filePath):
    """
    删除工程指定目录下的所有的编译文件(.pyc)
    """
    for prefix, dirs, files in os.walk(filePath):
        for name in files:
            if name.endswith('.pyc'):
                filename = os.path.join(prefix, name)
                os.remove(filename)

def del_xls(filePath):
    """
    删除工程指定目录下的所有的xls（.xls）
    """
    for prefix, dirs, files in os.walk(filePath):
        for name in files:
            if name.endswith('.xls'):
                filename = os.path.join(prefix, name)
                print(filename)
                os.remove(filename)

def del_xlsx(filePath):
    """
    删除工程指定目录下的所有的xls（.xlsx）
    """
    for prefix, dirs, files in os.walk(filePath):
        for name in files:
            if name.endswith('.xlsx'):
                filename = os.path.join(prefix, name)
                print(filename)
                os.remove(filename)


if __name__ == "__main__":
    # path = os.path.abspath('../')  # 将selenium目录通过os引用
    path = file_path
    # print(path)
    del_xls(path)
