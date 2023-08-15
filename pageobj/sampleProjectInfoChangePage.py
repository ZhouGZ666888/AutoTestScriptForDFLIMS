# -*- coding: utf-8 -*-
# @Time    : 2022/09/26
# @Author  : guanzhong.zhou
# @File    : 样本项目信息修改模块页面功能封装
import os
import pandas as pd
from PageElements.sampleProjectInfoChange_ele import *
from common.screenshot import Screenshot
from common.xlsx_excel import read_excel_col
from conf.all_path import sampleprocessing_file_path, excel_doc_file_path
from conf.execute_sql_action import project_id, sampleProId
from uitestframework.basepageTools import BasePage
from common.logs import log


class SampleProInfoChangePage(BasePage):
    """
    样本项目信息修改模块页面功能封装
    """

    # 打开指定页面
    def enter_function_page(self, url):
        """
        进入指定url页面
        """
        js = 'window.open("{}");'
        self.executeJscript(js.format(url))
        self.wait_loading()
        self.sleep(1)

    # 新增任务单
    def add_task(self, colName, search_by_tab, input_tab):
        """
        新建样本项目信息修改任务单
        """
        log.info("样本项目信息修改首页，点击新建按钮，新增项目信息修改任务")
        self.clicks('css', add_task)
        self.sleep(1)

        log.info("录入修改理由")
        self.input('css', change_reason, '测试-样本项目信息修改')
        self.sleep(0.5)
        self.clicks('css', next_step)
        self.sleep(0.5)

        log.info("根据{}检索，选择待修改样本".format(colName))

        sample_info_nub = read_excel_col(sampleprocessing_file_path, colName)

        # 点击选择待修改样本-按lims号或实验室号检索tab页
        self.clicks('css', search_by_tab)
        # 选择待修改样本-按lims号检索文本录入框录入lims号
        self.input('css', input_tab, sample_info_nub[0])
        self.sleep(0.5)
        self.clicks('css', search_sample_comfirm)
        self.wait_loading()
        self.sleep(0.5)

        log.info("导出样本-项目信息")
        self.clicks('css', download_sampleInfo_btn)
        self.wait_loading()
        self.sleep(0.5)
        # 这里调用自定义截图方法
        Screenshot(self.driver).get_img("样本项目信息修改，导出样本-项目信息")
        self.clicks('css', download_sampleInfo_comfirm)

    def edit_download_info(self):
        """
        编辑导出的样本-项目信息，修改项目号
        """
        log.info('在设置的下载文件夹下，获取最新导出的样本——项目信息文件')
        lists = os.listdir(excel_doc_file_path)
        print(lists)
        lists.sort(key=lambda fn: os.path.getmtime(excel_doc_file_path + '\\' + fn))
        filepath = os.path.join(excel_doc_file_path, lists[-1])
        print(filepath)

        log.info('从数据库获取符合条件的项目信息')
        projectIdList = self.select_sql(project_id)
        projectid = [i[item] for i in projectIdList for item in i]

        # 把符合条件的项目信息写入导出的样本项目信息修改文件
        data = pd.read_excel(filepath, engine='xlrd')
        print(projectid[3])
        data.iloc[1, 8] = projectid[4]
        data.to_excel(filepath, header=True, index=False)

    def upload_sampleinfo(self):
        """
        导入修改后样本-项目信息
        """
        # 设置页面导入按钮为可见
        self.executeJscript(
            "document.querySelector('.dialog-closeStep3 .upload-project input').style.setProperty('display','block','important');")
        # 获取导入文件
        lists = os.listdir(excel_doc_file_path)
        print(lists)
        lists.sort(key=lambda fn: os.path.getmtime(excel_doc_file_path + '\\' + fn))
        filepath = os.path.join(excel_doc_file_path, lists[-1])
        print(filepath)

        log.info('上传导入文件')
        self.input('css', upload_sampleInfo_btn, filepath)
        self.sleep(1)
        Screenshot(self.driver).get_img("样本项目信息修改，导入修改后样本-项目信息")
        pageinfo = self.get_pageinfo()
        self.sleep(0.5)

        log.info('提交修改任务单')
        self.clicks('css', sampleProjectInfo_submit)
        self.wait_loading()

        # 这里调用自定义截图方法
        Screenshot(self.driver).get_img("样本项目信息修改，提交修改任务单")

        self.sleep(1)
        return pageinfo

    def get_sampleProId_by_changeAfter(self):
        """
        数据库获取修改后样本项目信息，并校验是否修改正确
        """
        log.info('从数据库获取修改后样本项目信息')
        # 读取样本号
        sample_info_nub = read_excel_col(sampleprocessing_file_path, 'lims号')

        # 获取用做修改的样本项目号
        projectIdList = self.select_sql(project_id)
        projectid = [i[item] for i in projectIdList for item in i]

        # 获取修改后的样本项目号
        projectIdafter = self.select_sql(sampleProId.format(sample_info_nub[0]))
        projectids = [list(dct.values()) for dct in projectIdafter]
        print(projectids)

        # 判断修改后的样本项目号是否包含修改的样本项目号且原项目号置为无效
        try:
            for i in projectids:
                if i[0] == projectid[4] and i[1] == '1':
                    print("修改样本项目信息成功")
                    print(i[0], projectid[4])
                    return i[0], projectid[4]

                else:
                    print("原样本信息已置为无效")
        except Exception as info:
            print(info)

    def get_pageinfo(self):
        """
        获取页面操作提示信息
        Task list saved successfully---保存样本到任务单成功
        Submit successfully---提交成功
        sample in storage successfully---入库成功
        """
        if self.isElementExists('xpath', page_success_info):
            return self.get_text('xpath', page_success_info)
        else:
            return None
