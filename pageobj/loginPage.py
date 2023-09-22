from common.editYaml import read_yaml
from conf.all_path import testdata_path
from uitestframework.basepageTools import BasePage
from PageElements.loginPage_ele import *
from common.logs import log


class LoginPage(BasePage):
    """LIMS登陆页面"""

    def execute_login_js(self):
        """LIMS登陆页面切换登录方式"""
        js = "document.getElementById('enterpriseUser1').style.display = 'none';document.getElementById('enterpriseUser2').style.display = '';"
        self.executeJscript(js)

    def input_username(self, text):
        """lims登陆页面输入用户名方法
        :param text:用户名"""
        self.input('css', username_loc, text)

    def input_password(self, text):
        """LIMS登陆页面输入密码方法
        :param text:密码"""
        self.input('css', password_loc, text)

    def click_login_btn(self):
        """LIMS登陆页面点击登陆按钮方法"""
        self.clicks('css', login_btn_loc)

    def clear_username_by_js(self):
        """清空用户名输入框方法"""
        username_input = self.findelement('css', username_loc)
        js = "arguments[0].value=''"
        self.executeJscript(js, username_input)

    def clear_password_by_js(self):
        """清空用户名输入框方法"""
        password_input = self.findelement('css', password_loc)
        js = "arguments[0].value=''"
        self.executeJscript(js, password_input)

    def select_city_btn(self):
        """LIMS登陆成功点击选择登录城市下拉框"""
        self.clicks('css', selection_lab)
        self.sleep(0.5)
        self.clicks('xpath', select_login_city)
        self.clicks('css', select_login_city_confirm)

    def explorer_console(self):
        """
        操作浏览器

        """
        log.info('打开浏览器')
        self.max()
        log.info('访问地址')
        self.openbrower()

    def login_single(self, name):
        """
        单独测试正确的账号密码登录
        """

        datas = read_yaml(testdata_path)  # 获取测试登录的账号/密码配置数据
        try:
            # log.info("------TestCase Start!------")

            log.info('切换登录方式为账号密码登录')
            self.execute_login_js()

            log.info("清空输入框信息")
            self.clear_username_by_js()
            self.clear_password_by_js()

            if name == 'guanzhong.zhou':
                sort = 0
            elif name == 'guoqi.dong':
                sort = 1
            elif name == 'wei.sun':
                sort = 2
            else:
                sort = 1
            select_name = datas["companies"][sort]['name']
            select_password = datas["companies"][sort]['password']

            log.info('输入账号：{}'.format(select_name))
            self.input_username(select_name)
            self.sleep(0.5)
            log.info('输入密码：{}'.format(select_password))
            self.sleep(0.5)
            self.input_password(select_password)

            log.info('点击登录按钮')
            self.click_login_btn()
            self.wait_loading()

            log.info('登录后选择城市')
            self.select_city_btn()
            self.wait_loading()

        except Exception as r:
            raise r

    def login_console(self, name):
        """
        登录功能
        :param name: 登录用户名
        """
        self.explorer_console()
        self.login_single(name)

    def witchUsers(self, name):
        """
        登录功能
        :param name: 登录用户名
        """
        self.login_single(name)


lg = LoginPage(BasePage)

if __name__ == '__main__':
    LoginPage(BasePage)
