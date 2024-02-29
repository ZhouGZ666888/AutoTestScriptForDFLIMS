import re
import unittest
from common.setup_teardown import MyTest
from common import editYaml
from ddt import ddt, data
from common.logs import log
from conf.all_path import testdata_path
from uitestframework.exceptionsTools import ElementNotFound


@ddt
class LimsLogin(MyTest):
    """
    迪飞Lims登录功能点
    """
    datas = editYaml.read_yaml(testdata_path)  # 获取测试登录的账号/密码配置数据

    def setUp(self):

        log.info("------开始登录!------")
        log.info('打开浏览器,窗口最大化')
        self.basepage.max()
        log.info('访问地址')
        self.basepage.openbrower()
        log.info('切换登录方式为账号密码登录')
        self.lg.execute_login_js()
    def tearDown(self):
        log.info("------登录用例结束！------")


    def test01_Check_record_information(self):
        """测试网站备案信息是否正确"""
        result = re.search(r'Copyright © 2020 迪飞医学科技（南京）有限公司 版权所有 苏ICP备20046744号-2', self.lg.get_source)
        self.lg.sleep(1)
        self.assertIsNotNone(result)

    def test02_error_username_login(self):
        """用戶名错误，登录失败"""
        try:
            log.info('输入错误账号/密码登录：error/error')
            self.lg.input_username("error")
            self.lg.input_password("error")
            self.basepage.sleep(1)
            log.info('点击登录按钮')
            self.lg.click_login_btn()

            # 获取登录失败后的提示语tips
            login_error = self.basepage.get_text('xpath',
                                                 "//div[@class='el-message el-message--error']/p[text()='请填写正确的用户名、密码']")
            # 断言提示语
            self.assertIn("请填写正确的", login_error)
            # print(login_error)
            log.info('获取登录失败的提示语：{}'.format(login_error))

        except Exception as r:
            print('错误信息： %s' % r)

    @data(*datas["companies"])
    def test03_login_data(self, datas):
        """数据驱动测试多个账号登录LIMS系统"""
        try:

            log.info("清空输入框信息")
            self.lg.clear_username_by_js()
            self.lg.clear_password_by_js()

            log.info('输入账号：{}'.format(datas['name']))
            self.lg.input_username(datas['name'])

            log.info('输入密码：{}'.format(datas['password']))
            self.lg.input_password(datas['password'])

            log.info('点击登录')
            self.lg.click_login_btn()
            self.basepage.wait_loading()

            log.info('登录后选择城市')
            self.lg.select_city_btn()
            self.basepage.wait_loading()

            log.info('登录成功后校验当前地址正确')
            current_url = self.basepage.get_current_url()
            self.assertIn("homePage", current_url)

        except ElementNotFound as r:
            log.error(str(r))
            print('错误信息： %s' % r)


if __name__ == '__main__':
    unittest.main()
