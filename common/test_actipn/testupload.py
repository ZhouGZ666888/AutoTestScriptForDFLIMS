import os

import requests, time, re, random

from urllib.parse import quote

from common.xlsx_excel import get_lims_for_excel_by_rows
from conf.all_path import wkgj_file_path, wkfj_file_path, hstq_file_path_mNGS

req = {
    "url": "http://172.16.18.105:2016/ncov/lab/file/uploadNeusoftParticipantInfoForAutotest",
    "method": "POST",
    "headers": {},
    "files": {"file": ("", open("新冠普查20221108090319.xlsx", "rb"), "xlsx")},
    "data": {
        "Content-Type": "Content-Type: application/x-www-form-urlencoded",
        "fileType": "xlsx"
    }
}


def requests_http(req):

    result = requests.request(**req)
    return result.text

def test2():
    a=' 任务单  QPCRD2023080300004 '
    print(a.strip()[-18:])

def test3():
    otherNub = get_lims_for_excel_by_rows(wkfj_file_path, 0, 1, 'lims号')  # 其他类型样本号
    print(otherNub)
test3()

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def login(account, password):
    # 使用Chrome作为浏览器
    driver = webdriver.Chrome()

    # 打开登录页面
    driver.get("https://www.2-class.com/")
    driver.maximize_window()
    time.sleep(2)

    button = driver.find_element_by_css_selector('.login_home .padding-panel button')
    button.click()
    # 输入用户名和密码
    username_input = driver.find_element_by_id('account')
    username_input.send_keys(account)

    password_input = driver.find_element_by_id('password')
    password_input.send_keys(password)

    # 提交表单
    password_input.send_keys(Keys.ENTER)

    # 验证是否登录成功
    # if 'Welcome' in driver.title:
    # print('登录成功')
    # else:
    # print('登录失败')

    # 关闭浏览器
    driver.quit()


# 定义多个账号和密码
bccounts = [
    {'account': 'wangchangpin9', 'password': 'xcx123456'},
    {'account': 'zuozhixin223', 'password': 'xcx123456'}

]

# 循环登录多个账号
if __name__ == '__main__':
    for bccount in bccounts:
        login(bccount['account'], bccount['password'])
