from conf.all_path import excel_doc_file_path
from pageobj.loginPage import LoginPage
from uitestframework.basepageTools import BasePage
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from common.logs import log

import unittest
import warnings


class MyTest(unittest.TestCase):
    """
    将启动项和结束项单独提取，检索代码重复
    """
    driver = None
    basepage = None
    lg = None
    chrome_options = Options()
    warnings.simplefilter("ignore", ResourceWarning)  # 忽略警告信息
    options = webdriver.ChromeOptions()

    prefs = {"profile.default_content_settings.popups": 0,
        "download.default_directory": excel_doc_file_path}# 0禁止弹出下载窗口， download.default_directory设置下载路径
    options.add_experimental_option("prefs", prefs)
    dr = webdriver.Chrome(chrome_options=options)

    @classmethod
    def setUpClass(cls, driver=dr):
        cls.driver = driver
        log.info("------TestCase Start!------")
        cls.driver.implicitly_wait(1.5)
        cls.basepage = BasePage(cls.driver)
        cls.lg = LoginPage(cls.driver)

    # 登录功能封装，调试用
    def initialize(self):
        # self.lg.login_console('guoqi.dong')
        # self.lg.login_console('guanzhong.zhou')
        pass

    # 单个登录功能,接样审批切换用户时调用
    def login_action(self, loginUser):
        self.lg.witchUsers(loginUser)  # 常用，正式运行时打开

    @classmethod
    def tearDownClass(cls, driver=dr):
        cls.driver = driver
        cls.driver.refresh()
        cls.basepage.wait_loading()

        # 调试用
        # cls.driver.close()
        # cls.driver.quit()
