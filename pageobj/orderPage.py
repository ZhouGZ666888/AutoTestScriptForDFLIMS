# -*- coding: utf-8 -*-
# @Time    : 2021/11/01
# @Author  : guanzhong.zhou
# @File    : 订单模块页面功能封装

from common import editYaml
from common.screenshot import Screenshot
from PageElements.orderlist_ele import *
from conf.all_path import order_medical_info_path
from conf.execute_sql_action import order_isexists_sql
from uitestframework.basepageTools import BasePage
from common.logs import log


class OrderPage(BasePage):
    """订单页面基础功能封装"""

    def check_order_isExists(self, order):
        """
        新建订单前，先到数据库查询是否已存在相同订单号，若存在则返回递归方法，将订单号+1再次验证
        :param order: Excel读取的订单号
        :return: 返回验证后数据库不存在的订单号
        """
        # 数据库获取订单号，判断查询结果是否有值
        result = self.select_sql(order_isexists_sql.format(order))
        result1 = [dct[item] for dct in result for item in dct]
        # 查询订单号数为0，则说明该订单号不在数据库，则可用，返回该号
        if result1[0] == 0:
            return order
        # 订单号不为0，说明数据库已有该订单号，订单号不可用，在原订单号基础上+1后，传给方法，再次递归验证
        elif result1[0] != 0:
            new_order = str(int(order) + 1)
            return self.check_order_isExists(new_order)

    def add_order(self):
        """新建订单,录入订单号和参检人姓名"""
        log.info('新增订单，录入订单号、患者姓名')
        self.click_by_js("css", add_order)
        self.sleep(0.5)
        # 判断是否存在存储订单号的yaml文件，如果不存在则新建yaml文件，并把新的订单号存入，如果存在，则取里面的已有订单号，并+1，作为新的订单号
        order = editYaml.read_yaml(order_medical_info_path)
        try:
            if 'ordernumb' not in order:
                first_order_num = '88880000'
                # 验证订单号是否可用
                order_nub = self.check_order_isExists(first_order_num)
                log.info('新建的订单号%s'%order_nub)

                self.input('css', order_num_input, order_nub)
                self.sleep(0.5)
                self.input('css', patient_name_input, str(order['username']).strip())
                self.sleep(0.5)

                # 调用自定义截图方法
                Screenshot(self.driver).get_img("点击新建订单按钮，弹框中录入订单号、用户名点击确认","新建订单成功")

                self.clicks('css', add_confirm)
                self.wait_loading()

                # 把订单号写入文件
                order['ordernumb']=str(order_nub)
                editYaml.save_yaml(order_medical_info_path, order)  # 订单号写入临时文件

            else:
                old_ordernum = order['ordernumb']
                # 验证订单号是否可用
                new_ordernum = self.check_order_isExists(str(int(old_ordernum) + 1))

                self.input('css', order_num_input, new_ordernum)
                self.sleep(0.5)
                self.input('css', patient_name_input, str(order['username']).strip())
                self.sleep(0.5)

                # 调用自定义截图方法
                Screenshot(self.driver).get_img("点击新建订单按钮，弹框中录入订单号、用户名点击确认","新建订单成功")
                self.clicks('css', add_confirm)
                self.wait_loading()
                order['ordernumb'] = str(new_ordernum)
                editYaml.save_yaml(order_medical_info_path, order)  # 订单号写入临时文件
                self.sleep(1)
        except Exception as e:
            print(e)

    def enter_edit(self):
        """搜索出新建订单，选中并编辑"""
        self.click_by_js('css', search_order)
        order_nub = editYaml.read_yaml(order_medical_info_path)  # 从yaml文件中获取订单号
        self.sleep(0.5)
        self.input('css', search_order_input, order_nub['ordernumb'])
        self.clicks('css', search_order_comfirm)
        self.wait_loading()

        self.click_by_js('css', first_order)
        self.sleep(0.2)
        self.clicks('css', edit_order)
        self.wait_loading()

    def edit_order(self):
        """编辑订单信息"""
        medicalnumInfo = editYaml.read_yaml(order_medical_info_path)

        log.info('选择电子病历')
        self.clicks('css', ele_patient_number)
        self.wait_loading()

        self.input('css', identification_numb, str(medicalnumInfo['identificationNo']).strip())
        self.input('css', patient_name, str(medicalnumInfo['username']).strip())
        self.sleep(0.5)
        self.clicks('css', search_num_button)
        self.wait_loading()
        self.clicks('css', similar_case)  # 查询结果，选中第一条
        self.sleep(0.5)
        self.clicks('css', ele_chioce_confirm)
        self.clicks('css', chioce_and_confirm)
        self.wait_loading()

        log.info('录入临床诊断信息')
        self.input('css', crmPatientDiagnosisHistory, '临床诊断信息')
        self.sleep(0.2)
        self.input('css', crmPatientTreatmentHistory, '用药史信息')
        self.sleep(1)
        log.info('新增联系人信息,录入姓名、联系方式、地址')
        self.clicks('css', add_new_contact)

        self.clicks('css', contact_name)
        self.input('css', contact_name_input, '测试人员')
        self.sleep(0.5)
        self.clicks('css', contact_tel_numb)
        self.input('css', contact_tel_numb_input, '15252415241')
        self.sleep(0.5)

        log.info('新增医生信息')
        self.clicks('css', chioce_physician)
        self.wait_loading()
        self.input('css', search_by_department, '肺')
        self.clicks('css', physician_search_button)
        self.wait_loading()
        self.clicks('css', chioce_department)
        self.sleep(1)
        self.clicks('css', chioce_physician_confirm)
        self.sleep(1)
        log.info('录入销售代表和款项信息')
        self.clicks('css', sales_information)
        self.input('css', sales_information, '董国奇')
        self.sleep(0.5)
        self.clicks('css', chioce_sale)
        self.sleep(0.5)

        self.clicks('css', payment_due)
        self.sleep(0.5)
        self.input('css', fee_after_amendment, '10000')
        self.sleep(0.5)
        self.input('css', amendment_reason, '无理由')
        self.sleep(0.5)
        self.clicks('css', change_fee_confirm)
        self.sleep(1)

        log.info('选择结算方式为进院')
        self.clicks('css', pay_style)
        self.clicks('xpath', pay_style_choice)


    def save_add_order(self):
        """保存订单"""
        log.info('保存订单')
        self.click_by_js('css', save_button)
        # 调用自定义截图方法
        Screenshot(self.driver).get_img("录入订单信息后，点击保存订单","保存订单成功")
