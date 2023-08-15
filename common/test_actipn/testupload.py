import os

import requests, time, re, random
from fake_useragent import UserAgent

from urllib.parse import quote

from common.xlsx_excel import get_lims_for_excel_by_rows
from conf.all_path import wkgj_file_path

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
if __name__ == '__main__':

    otherNub = get_lims_for_excel_by_rows(wkgj_file_path, 0, -4, 'lims号')  # 其他类型样本号
    print(otherNub)
    # test2()