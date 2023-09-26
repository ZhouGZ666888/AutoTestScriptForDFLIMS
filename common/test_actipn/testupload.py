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
    otherNub = get_lims_for_excel_by_rows(hstq_file_path_mNGS, 0, 1, 'lims号')  # 其他类型样本号
    print(otherNub)


test3()