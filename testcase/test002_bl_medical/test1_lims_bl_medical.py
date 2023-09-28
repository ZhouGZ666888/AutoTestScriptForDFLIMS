import re, unittest, ddt
from common.logs import log
from conf.all_path import order_medical_info_path
from conf.enter_tab import EnterTab
from common.screenshot import Screenshot
from pageobj.medicalPage import MedicalPage
from common.editYaml import read_yaml, save_yaml
from common.setup_teardown import MyTest


@ddt.ddt
class LimsMedical(MyTest):
    """病历模块测试用例"""

    datas = read_yaml(order_medical_info_path)

    def setUp(self) -> None:
        self.mp = MedicalPage(self.driver)

    def test01_add_medical(self):
        """
        测试新建病历并保存
        """
        self.initialize()
        EnterTab.enter_crmorder(self.basepage)
        EnterTab.enter_crm(self.basepage)
        log.info('进入新增模块')
        self.mp.click_add_medical()

        log.info('读取新的身份证')
        add_identificationNo = self.mp.get_identificationNo()
        log.info('录入患者姓名:%s，身份证信息:%s' % (add_identificationNo[1], add_identificationNo[0]))
        self.mp.input_patientinfo(name=add_identificationNo[1], identityNo=add_identificationNo[0])

        log.info('保存病历')
        self.mp.save_medical()
        self.mp.continue_save()
        Screenshot(self.driver).get_img("新增病例，录入患者信息，点击保存按钮","保存病历成功")
        self.mp.wait_loading()
        self.mp.sleep(0.5)
        self.mp.wait_loading()

        # 获取新建病历号
        medicalnum_No = self.driver.execute_script(
            'return document.getElementsByClassName("medicalDetail-form-patientId")[0].getElementsByClassName("el-input__inner")[0].value')
        result = re.search('\d+', medicalnum_No)
        print('获取新建病历号', medicalnum_No)

        # 将获取的患者姓名、身份证号和新建病历号更新到yaml文件中
        self.datas['identificationNo'] = add_identificationNo[0]
        self.datas['username'] = add_identificationNo[1]
        self.datas["medicalnum_no"] = medicalnum_No

        save_yaml(order_medical_info_path, self.datas)  # 保存修改后的yaml文件

        self.mp.sleep(1)
        self.assertIsNotNone(result)

    def test02_add_medical_missInfo(self):
        """
        测试新增病历，校验必填项未填，保存提示信息
        """

        log.info('登录系统，进入病历页面')

        EnterTab.enter_crmorder(self.basepage)
        EnterTab.enter_crm(self.basepage)

        log.info('进入新增模块')
        self.mp.click_add_medical()

        log.info('输入患者性别')
        self.mp.get_sex()

        log.info('保存病历')
        self.mp.save_medical()


        result = re.search(r'请输入正确的姓名、证件号码', self.mp.get_source)
        self.mp.sleep(1)
        self.assertIsNotNone(result)


    def test03_already_medical(self):
        """
        测试新建病历，身份证重复时，系统做出校验
        """
        EnterTab.enter_crmorder(self.basepage)
        EnterTab.enter_crm(self.basepage)
        log.info('进入新增模块')
        self.mp.click_add_medical()

        log.info('录入患者姓名:%s，身份证信息:%s' % (self.datas['username'], self.datas['identificationNo']))
        self.mp.input_patientinfo(name=self.datas['username'], identityNo=self.datas['identificationNo'])

        log.info('保存病历')
        self.mp.save_medical()
        self.mp.continue_save()

        result = re.search(r'系统内已存在相同身份证号的病历', self.mp.get_source)
        self.mp.wait_loading()
        self.mp.sleep(1)
        self.assertIsNotNone(result)

    def test04_search_medical(self):
        """
        测试根据病历号检索功能
        """

        EnterTab.enter_crmorder(self.basepage)
        EnterTab.enter_crm(self.basepage)

        log.info('点击搜索')
        self.mp.search_medical()

        log.info('搜索病历号')
        self.mp.search_by_param(self.datas['medicalnum_no'])

        log.info('点击确定')
        self.mp.click_search_btn()
        self.mp.wait_loading()

        log.info('获取查询结果，进行断言')
        self.mp.sleep(0.5)
        result = re.search(self.datas['medicalnum_no'], self.mp.get_source)
        self.assertIsNotNone(result)


if __name__ == "__main__":
    unittest.main()
