# -*- coding: utf-8 -*-
from conf.all_path import identificationNo_file_path
from PageElements.medical_ele import *
from conf.execute_sql_action import bl_sql
from uitestframework.basepageTools import BasePage
import pandas as pd
from common.logs import log


class MedicalPage(BasePage):
    """病历页面基础功能封装"""

    def search_medical(self):
        """点击搜索按钮方法 """
        log.info("点击搜索按钮")
        self.clicks('css', search_btn)
        self.sleep(0.5)

    def search_by_param(self, text):
        """
        按病历号搜索方法
        :param text: 病历号
        """
        log.info("输入病历号进行搜索")
        self.input('css', search_medicalNum, text)

    def click_edit_btn(self):
        """点击编辑按钮方法"""
        log.info("点击编辑按钮")
        self.clicks('class_name', edit_btn)

    def click_search_btn(self):
        """点击搜索确认方法"""
        self.clicks('css', search_sure_btn)
        self.sleep(1)

    def click_add_medical(self):
        """点击新增病历方法"""
        log.info("点击新增按钮")
        self.clicks('css', add_btn)
        self.wait_loading()

    def save_medical(self):
        """保存病历"""
        log.info("点击保存按钮")
        self.clicks('css', save_btn)

    def continue_save(self):
        """判断是否存在保存过程中出现身份证重复或其他提示弹框"""
        if self.isDisplayed('css', continue_save):
            self.clicks('css', continue_save)
        if self.isDisplayed('css', continue_save_for_repeat):
            self.clicks('css', continue_save_for_repeat)

    def input_patientinfo(self, name, identityNo):
        """
        病历中输入患者姓名,身份证信息方法
        :param name: 患者姓名
        :param identityNo: 身份证
        """
        log.info("病历中输入患者姓名,身份证信息")
        self.input('css', Participants_name, name)
        self.sleep(0.5)
        self.input('css', identificationNo, identityNo)
        self.sleep(0.5)

    def get_sex(self):
        """获取患者性别方法"""
        log.info("病历中输入患者性别")
        self.click_by_js('css', sex)
        self.sleep(1)
        self.clicks('xpath', man_sex)
        self.sleep(0.5)

    def get_identificationNo(self):
        """
        身份证Excel中读取身份证信息
        :return: 返回身份证号
        """
        df = pd.read_excel(identificationNo_file_path)
        # 获取总行数
        rowsNum = df.shape[0]

        if rowsNum > 1:

            # 获取第一行身份证号码'''
            identificationNos = df.iloc[0].values
            print("读取的身份证信息", identificationNos)
            # 从Excel中取第一行的身份证，去数据库查询是否已存在'''
            reslt = self.select_sql(bl_sql.format(identificationNos[0]))
            used_identificationNo = [i[item] for i in reslt for item in i]
            # 查询结果如果为0 ，则表示该身份证信息未被使用，则满足条件，返回该身份证'''
            if used_identificationNo[0] == 0:
                # 取出该身份证号使用，并在Excel中删除该条身份证
                df.drop(index=[0], axis=0, inplace=True)
                print("Excel中还剩", df.shape[0], "条身份证")
                df.to_excel(identificationNo_file_path, index=None)
                return identificationNos
            else:
                # 若该身份证查询出已有结果，则删除该身份证，程序进入递归查询'''
                df.drop(index=[0], axis=0, inplace=True)
                print("Excel中还剩", df.shape[0], "条身份证")
                df.to_excel(identificationNo_file_path, index=None)
                return self.get_identificationNo()


if __name__ == '__main__':
    s = MedicalPage
    # s.enter_medical()#driver
