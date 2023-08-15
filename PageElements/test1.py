import unittest
from selenium import webdriver
from ddt import data,ddt

from common import editYaml
from common.xlsx_excel import read_excel_xlsx_list_col
from conf import all_path
from conf.all_path import order_file_path

# datas = read_yaml.read_yaml(all_path.testdata_path)
# # print(datas["companies"])
#
# @ddt
# class Tets(unittest.TestCase):
#
#
#     @data(*datas["companies"])
#     def test_01(self,datas):
#         print(datas['name'])
#
#
#
# # if __name__ == '__main__':
# #     unittest.main()
#
# import re
# a = re.search('\d+','sadf')
# print(a.group())
#
# order_nub = read_excel_xlsx_list_col(order_file_path, 0, 'order_number')  # 订单Excel获取订单号
# print(order_nub)

def setUpModule() -> None:
    global driver
    driver = webdriver.Chrome()


def tearDownModule() -> None:
    driver.quit()


class MyTestCase3(unittest.TestCase):
    def test_baidu(self):
        print("a")
        driver.get("https://www.baidu.com/")

    def test_aengxun(self):
        print("b")
        driver.get("https://www.qq.com/")

    def test_puls(self):
        print("c")
        c = 1 + 3
        print(c)


class MyTestCase2(unittest.TestCase):
    def test_baidu(self):
        print("d")
        driver.get("https://www.baidu.com/")

    def test_tengxun(self):
        print("e")
        driver.get("https://www.qq.com/")

    def test_puls(self):
        print("f")
        c = 1 + 3
        print(c)

specimen_list = {'DNA': 30, '迪迅康-基础(8)': 10}
total = specimen_list.values()
print(total)