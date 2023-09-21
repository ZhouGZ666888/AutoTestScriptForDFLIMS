# -*- coding: utf-8 -*-
# @Time    : 2023/09/21
# @Author  : guanzhong.zhou
# @File    : samplesheet方法封装
import pandas as pd
from common.editYaml import *
from common.screenshot import Screenshot
from PageElements.samplesheet_ele import *
from conf.all_path import sampledata_path, excel_doc_file_path
from uitestframework.basepageTools import BasePage
from common.logs import log
from common.editYaml import read_yaml


class SampleSheetPage(BasePage):
    """samplesheet模块页面基础方法封装"""

    def search_by_taskid(self):
        """通过上机任务单号搜索samplesheet"""

        taskid = read_yaml(sampledata_path)
        log.info("点击搜索按钮，录入上机任务单号")
        self.clicks('css', search)
        self.sleep(0.5)
        self.input('css', sj_taskid, taskid["sj_taskid"])
        self.clicks('css', search_confirn)
        self.wait_loading()
        Screenshot(self.driver).get_img("根据任务单号搜索ss数据，实际结果如下图：")
        log.info("选中搜索出的samplesheet，点击编辑按钮")
        self.clicks('css', search_result)
        self.clicks('css', edit_btn)
        self.wait_loading()

    def samplesheet_detail_download(self):
        """samplesheet详情页面,导出samplesheet"""
        Screenshot(self.driver).get_img("根据搜索结果，进入samplesheet详情，实际结果如下图：")
        self.clicks('css', download_csv_btn)
        self.sleep(1)

    def samplesheet_detail_import(self):
        """samplesheet导入CSV"""
        log.info('在设置的下载文件夹下，获取最新导出的samplesheet文件')
        lists = os.listdir(excel_doc_file_path)
        lists.sort(key=lambda fn: os.path.getmtime(excel_doc_file_path + '\\' + fn))
        filepath = os.path.join(excel_doc_file_path, lists[-1])
        # 修改导出的samplesheet文件，之后导入
        df = pd.read_csv(filepath, encoding='utf-8')
        df.loc[:, 'Description'] = 'samplesheetTest'
        df.to_csv(filepath, index=False, encoding='utf-8')

        self.clicks('css', import_csv_btn)
        self.sleep(1)
        self.executeJscript(
            "document.querySelector('.dialog-upload-visible1 .el-upload--text input').style.setProperty('display','block','important');")
        self.sleep(0.5)
        log.info('把修改后的samplesheet文件导入')
        self.input('css', samples_upload, filepath)
        self.sleep(1)
        self.clicks('css', download_csv_confirm)
        return self.get_save_info()

    def detail_save_generate_new_version(self):
        """保存&生成新版本"""
        log.info("samplesheet生成新版本")
        self.clicks('css', save_generate_new_version)
        self.sleep(1)
        self.input('css', reason_for_modification, 'new_version')
        self.sleep(1)
        Screenshot(self.driver).get_img("预期结果：打开samplesheet生成新版本弹框，实际结果如下图：")
        self.clicks('css', reason_for_modification_confirn)
        info = self.get_save_info()
        self.wait_loading()
        return info

    def detail_modify_record(self):
        """查看修改记录"""
        self.refresh()
        log.info("查看samplesheet修改记录")
        self.clicks('css', modify_record)
        Screenshot(self.driver).get_img("预期结果：samplesheet修改记录弹框包含新版本，实际结果如下图：")

        datas = self.findelements('css', modify_record_data)
        return len(datas)

    def get_save_info(self):
        """
        获取数据操作后，页面给出的提示信息语
        Submit successfully
        review successfully
        """
        log.info('获取页面提示信息')
        if self.isElementExists('xpath', page_info):
            return self.get_text('xpath', page_info)
        else:
            return None
