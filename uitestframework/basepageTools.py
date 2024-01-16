import re

import pyperclip, time
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from common.editYaml import read_yaml
from common.DataBaseConnection import executeSql
from common.xlsx_excel import add_write_excel_xlsx
from common.logs import log
from conf.all_path import testdata_path, hstq_file_path_mNGS, wkgj_file_path, qpcr_dxk_file_path, sj_file_path, \
    ybrk_file_path, wkfj_file_path, functionpageURL_path, mpcr_file_path, wkdl_file_path
from .exceptionsTools import ElementNotFound, ElementNotTextAttr
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    """基础页面类"""

    datas = read_yaml(testdata_path)  # 获取测试登录地址配置数据-test1环境

    def __init__(self, driver):
        self.driver = driver
        self.baseurl = self.datas['baseurl']

    def openbrower(self):
        """
        打开浏览器方法
        """
        self.driver.get(self.baseurl)
        self.sleep(1)

    def max(self):
        """
        最大化浏览器方法
        """
        self.driver.maximize_window()
        log.info('最大化浏览器')

    def quit(self):
        """
        退出浏览器驱动
        """
        self.driver.quit()
        log.info('关闭浏览器')

    @staticmethod
    def sleep(t):
        """
        浏览器强制等待方法
        :param t:强制等待时间
        """
        time.sleep(t)
        # logger.info('睡眠{}秒'.format(t))

    def close(self):
        """
        关闭窗口方法
        """
        self.driver.close()
        log.info('关闭页面')

    @staticmethod
    def impcait(t):
        """
        浏览器显性等待方法（需要等待界面渲染结束后再去定位元素）
        :param t:强制等待时间
        """
        time.sleep(t)
        log.info('显性等待{}秒钟'.format(t))

    def refresh(self):
        """
        浏览器页面刷新方法
        """
        self.driver.refresh()
        self.wait_loading()
        log.info('页面刷新')

    def capture_as_base64(self):
        """
        获取图片方法（以base64存储）
        :return:返回图片base64编码
        """
        return self.driver.get_screenshot_as_base64()

    def capture_as_png(self):
        """
        获取图片方法（以png存储）
        """
        return self.driver.get_screenshot_as_png()

    def capture_pic(self, name):
        """
        获取图片方法
        :param name:所保存图片的名称和位置
        """
        return self.driver.save_screenshot(name)

    def capture_as_file(self, filename):
        """
        获取图片方法
        :param filename: 所保存图片的名称和位置
        """
        return self.driver.get_screenshot_as_file(filename)

    def wait_loading(self):
        """
        设置等待页面loading结束再去操作,是结束，不是出现
        el-message el-message--success
        """
        loading = '//*[@class="el-loading-spinner"]/descendant::p[text()="Loading"]'  # 定义了loading
        # 等待60s超时，默认0.5s寻找一次
        WebDriverWait(self.driver, 60).until_not(lambda x: x.find_element(By.XPATH, loading))
        self.sleep(1)

    def is_not_visible(self, locator):
        try:
            isPresent = WebDriverWait(self.driver, 10).until_not(expected_conditions.visibility_of_element_located((
                By.XPATH, locator)))
            if isPresent:
                return self.driver.find_element_by_xpath(locator)
        except TimeoutException:
            return False

    @property
    def get_source(self):
        """获取页面源代码"""
        return self.driver.page_source

    def wait_pageinfo_end(self):
        """
        设置等待页面提示信息结束再去操作,是结束，不是出现
        el-message el-message--success
        """
        pageinfo = 'el-message el-message--success'  # 定义了页面提示信息的class
        # 等待60s超时，默认0.5s寻找一次
        WebDriverWait(self.driver, 120).until_not(lambda x: x.find_element(By.CLASS_NAME, pageinfo))

    def findelement(self, ele_type, element_loc):
        """
        查找单个唯一元素方法
        :param ele_type:
        :param element_loc:元素属性定位
        :return:对应元素对象
        """

        element = None
        try:
            if ele_type == "xpath":
                element = WebDriverWait(self.driver, 5).until(lambda x: x.find_element_by_xpath(element_loc))
            elif ele_type == "class_name":
                element = WebDriverWait(self.driver, 5).until(lambda x: x.find_element_by_class_name(element_loc))
            elif ele_type == "id":
                element = WebDriverWait(self.driver, 5).until(lambda x: x.find_element_by_id(element_loc))
            elif ele_type == "name":
                element = WebDriverWait(self.driver, 5).until(lambda x: x.find_element_by_name(element_loc))
            elif ele_type == "link_text":
                element = WebDriverWait(self.driver, 5).until(lambda x: x.find_element_by_link_text(element_loc))
            elif ele_type == "partial_link_text":
                element = WebDriverWait(self.driver, 5).until(
                    lambda x: x.find_element_by_partial_link_text(element_loc))
            elif ele_type == "css":
                element = WebDriverWait(self.driver, 5).until(lambda x: x.find_element_by_css_selector(element_loc))
        except Exception as e:
            raise ElementNotFound(e)
        return element

    # def findelement(self, ele_type,element_loc):
    #     '''
    #     查找单个唯一元素方法
    #     :param element_loc:元素属性定位
    #     :return:对应元素对象
    #     '''
    #     try:
    #         element = WebDriverWait(self.driver, 10).until(lambda x: x.find_element_by_xpath(element_loc))
    #         # element = self.driver.find_element(*element_loc)
    #     except Exception as e:
    #         raise ElementNotFound(e)
    #     return element

    def findelements(self, ele_type, element_loc):
        """
        查找多个元素方法
        :param ele_type:
        :param element_loc:元素属性定位
        :return:对应元素对象列表
        """
        elements = None
        try:
            if ele_type == "xpath":
                elements = WebDriverWait(self.driver, 10).until(lambda x: x.find_elements_by_xpath(element_loc))
            elif ele_type == "class_name":
                elements = WebDriverWait(self.driver, 10).until(lambda x: x.find_elements_by_class_name(element_loc))
            elif ele_type == "id":
                elements = WebDriverWait(self.driver, 10).until(lambda x: x.find_elements_by_id(element_loc))
            elif ele_type == "name":
                elements = WebDriverWait(self.driver, 10).until(lambda x: x.find_elements_by_name(element_loc))
            elif ele_type == "link_text":
                elements = WebDriverWait(self.driver, 10).until(lambda x: x.find_elements_by_link_text(element_loc))
            elif ele_type == "partial_link_text":
                elements = WebDriverWait(self.driver, 10).until(lambda x: x.find_elements_by_partial_link_text(
                    element_loc))
            elif ele_type == "css":
                elements = WebDriverWait(self.driver, 60).until(lambda x: x.find_elements_by_css_selector(element_loc))
        except Exception as e:
            raise ElementNotFound(e)
        return elements

    def isElementExists(self, ele_type, element_loc):
        """
        判断元素是否只存在，返回布尔值
        :param element_loc:
        :param ele_type:
        :return:flag
        """
        flag = True
        try:
            self.findelement(ele_type, element_loc)
            return flag
        except ElementNotFound:
            flag = False
            return flag

    def is_element_clickable(self, ele_type, locator):
        """
        判断页面元素是否可以点击。
        :param ele_type:
        :param locator: 用于定位元素的定位器，例如(By.ID, 'element_id')
        :return: 可点击返回True，否则返回False
        """
        try:
            # 等待元素变得可以点击
            element = self.findelement(ele_type, locator)
            WebDriverWait(self.driver, 1).until(
                EC.element_to_be_clickable(element)
            )
            return True
        except TimeoutException:
            # 超时说明元素无法点击
            return False

    def isDisplayed(self, ele_type, element_loc):
        """
        判断元素是否可见，返回布尔值
        :param ele_type:
        :param element_loc:
        :return:True or False
        """
        try:
            if self.isElementExists(ele_type, element_loc):
                element = self.findelement(ele_type, element_loc)
                return element.is_displayed()
        except Exception as e:
            raise ElementNotFound(e)

    def input(self, ele_type, element_loc, text):
        """
        输入文本方法
        :param ele_type:
        :param element_loc:对应输入框的元素定位
        :param text:需要输入的文本
        """
        try:
            element = self.findelement(ele_type, element_loc)
        except Exception as e:
            raise ElementNotFound(e)
        js = "arguments[0].value='';"
        self.executeJscript(js, element)
        element.send_keys(text)

    def clear_input(self, ele_type, element_loc):
        """
        清除文本框内容
        """
        try:
            element = self.findelement(ele_type, element_loc)
            js = "arguments[0].value='';"
        except Exception as e:
            raise ElementNotFound(e)
        self.executeJscript(js, element)

    @staticmethod
    def updata_sql(sqls):
        """
        调用sql方法,执行更新数据操作
        """
        executeSql.test_updateByParam(sqls)

    @staticmethod
    def select_sql(sqls):
        """
        调用sql方法,执行数据库操作，获取返回值
        :return:数据库返回值
        """
        sql_data = executeSql.test_select_limsdb(sqls)
        return sql_data

    def executeJscript(self, js, *args):
        """
        执行js语句方法
        :param js: js语句
        :param args:js语句其他的一些参数
        """
        self.driver.execute_script(js, *args)
        # logger.info("执行对应js脚本成功")

    def clicks(self, ele_type, element_loc):
        """
        元素点击方法
        test=driver.find_element_by_xpath('//*[@id="submit"]')
        driver.execute_script("arguments[0].click();", test)
        :param ele_type:
        :param element_loc:需要点击的元素定位
        """
        try:
            element = self.findelement(ele_type, element_loc)
        except Exception as e:
            raise ElementNotFound(e)
        element.click()

    def click_by_js(self, ele_type, element_loc):
        """
        元素点击方法,针对部分未知点击事假报错，用这个方法
        test=driver.find_element_by_xpath('//*[@id="submit"]')
        driver.execute_script("arguments[0].click();", test)
        :param ele_type:
        :param element_loc:需要点击的元素定位
        """
        try:
            element = self.findelement(ele_type, element_loc)
        except Exception as e:
            raise ElementNotFound(e)
        self.executeJscript("arguments[0].click();", element)

    def get_text(self, ele_type, element_loc):
        """
        获取到对应元素的text属性
        :param ele_type:
        :param element_loc:需要获取对应text属性的元素定位
        :return:返回对应的元素的text属性
        """
        try:
            element_text = self.findelement(ele_type, element_loc).text
            return element_text
        except Exception as e:
            raise ElementNotTextAttr(e)

    def switch_to_window(self, handle_window):
        """
        切换浏览器tab页方法
        :param handle_window:所需要切换窗口的句柄
        """
        self.driver.switch_to.window(handle_window)

    def get_current_window_handle(self):
        """
        获取当前浏览器当前窗口句柄方法
        :return: 返回当前窗口句柄
        """
        return self.driver.current_window_handle

    def get_all_windows(self):
        """
        获取当前浏览器所有窗口句柄的方法
        :return:返回当前浏览器所有窗口的句柄
        """
        return self.driver.window_handles

    def get_current_url(self):
        """
        获取当前的url
        :return:返回当前的url
        """
        return self.driver.current_url

    def switch_to_frame(self, frame):
        """
        切换iframe
        :param frame: iframe元素定位
        :return:
        """
        self.driver.switch_to.frame(frame)

    def switch_to_default_content(self):
        """
        切换iframe回主文档
        :return:
        """
        self.driver.switch_to.default_content()

    def get_cookies(self):
        """
        获取当前浏览器的cookies
        :return:返回当前浏览器的cookies
        """
        Cookie = {}
        for item in self.driver.get_cookies():
            Cookie[item["name"]] = item["value"]
        return Cookie

    def delete_cookies(self):
        """
        清除当前浏览器的所有cookies
        """
        self.driver.delete_all_cookies()

    def moved_to_element(self, ele_type, element_loc):
        """
        将鼠标移动到对应元素位置
        :param ele_type:
        :param element_loc:需要将鼠标移动到的元素定位
        """
        try:
            element = self.findelement(ele_type, element_loc)
        except Exception as e:
            raise ElementNotFound(e)
        ActionChains(self.driver).move_to_element(element).perform()

    def double_click(self, ele_type, element_loc):
        """鼠标双击元素事件
        :param ele_type:
        :param element_loc:需要鼠标双击的元素
        """
        try:
            element = self.findelement(ele_type, element_loc)
        except Exception as e:
            raise ElementNotFound(e)
        ActionChains(self.driver).double_click(element).perform()

    def scrollTo(self, width, height):
        """
        将浏览器内容滚动到指定的坐标方法
        :param width:要在窗口文档显示区左上角显示的文档的 x 坐标
        :param height:要在窗口文档显示区左上角显示的文档的 y 坐标
        """
        js = " window.scrollTo(%d,%d)" % (width, height)
        self.executeJscript(js)
        log.info("成功滑动到 %d,%d" % (width, height))

    def scrollIntoViews(self, ele_type, element_loc):
        """
        让指定的元素滚动到浏览器窗口的可视区域内方法
        :param ele_type:
        :param element_loc:指定元素定位
        """
        try:
            element = self.findelement(ele_type, element_loc)
        except Exception as e:
            raise ElementNotFound(e)
        self.executeJscript("arguments[0].scrollIntoView();", element)

    @staticmethod
    def get_clip():
        """
        获取剪切板内容方法
        :return:返回剪切板内容方法
        """
        return pyperclip.paste()

    @staticmethod
    def set_clip(text):
        """
        将给定字符串内容拷贝进剪贴板方法
        :param text:给定的字符串内容
        :return:
        """
        return pyperclip.copy(text)

    def getAttribute(self, ele_type, element_loc, attr):
        """
        获取给定元素中的某一属性方法
        :param ele_type:
        :param element_loc:给定的元素定位
        :param attr:元素的某一个属性
        :return:返回对应元素的对应属性值
        """
        try:
            element = self.findelement(ele_type, element_loc)
        except Exception as e:
            raise ElementNotFound(e)
        return element.get_attribute(attr)

    def add_excel_xlxs(self, sql, table_name, task_id):

        """
        根据核酸提取、超声破碎、文库构建流程结果表任务单号，在数据库中查询出样本对应下一步流程，以二维列表形式存入相对应的Excel中。最终存入lims号，下一步流向，和任务单号
        :param sql: 数据库sql
        :param table_name: 实验流程节点对应的结果表表名
        :param task_id: 实验流程对应的结果表任务号页面元素定位
        """
        # 获取任务单号
        taskidstr = self.get_text('css', task_id)
        taskid = re.findall(r'[a-zA-Z0-9]+', taskidstr)[0]

        # 执行SQL，获取二维列表，lims号和下一步流向
        dada = self.select_sql(sql.format(table_name, taskid))

        # 把任务单号添加进二维列表
        result = [list(dct.values()) + [taskid] for dct in dada]  # ID，next，task_id

        # 根据不同下一步，循环写入Excel
        for item in range(len(result)):
            data_list = []
            # 取出二维列表子元素的第三个值（下一步），进行判断
            next_step = result[item][2]

            if next_step == 'extraction':  # 核酸提取
                result[item][2] = '核酸提取'
                data_list.append(result[item])
                add_write_excel_xlsx(hstq_file_path_mNGS, data_list)

            elif next_step == 'libconstruction':  # 文库构建
                result[item][2] = '文库构建'
                data_list.append(result[item])
                add_write_excel_xlsx(wkgj_file_path, data_list)

            elif next_step == 'qpcr':  # 文库富集
                result[item][2] = '文库富集'
                data_list.append(result[item])
                add_write_excel_xlsx(qpcr_dxk_file_path, data_list)

            elif next_step == '上机':  # 上机
                data_list.append(result[item])
                add_write_excel_xlsx(sj_file_path, data_list)

            elif next_step == '样本入库':
                data_list.append(result[item])
                add_write_excel_xlsx(ybrk_file_path, data_list)

            elif next_step == '文库定量':
                data_list.append(result[item])
                add_write_excel_xlsx(wkdl_file_path, data_list)

            elif next_step == 'pooling':
                data_list.append(result[item])
                add_write_excel_xlsx(wkfj_file_path, data_list)

            elif next_step == 'mpcr':
                data_list.append(result[item])
                add_write_excel_xlsx(mpcr_file_path, data_list)
            else:
                print('这个样本下一步流程中没见过')

    def enter_func_page(self):
        """调用打开页面方法，直接保存的url页面"""
        datas = read_yaml(functionpageURL_path)  # 获取测试登录的账号/密码配置数据

        now_handle = self.get_current_window_handle()
        self.baseurl = datas['url']
        self.openbrower()
        print('打开的URL地址', datas['url'])
        all_handles = self.get_all_windows()
        for handle in all_handles:
            if handle != now_handle:
                # 切换到新窗口句柄，即新打开的页面
                self.close()
                self.switch_to_window(handle)
                self.wait_loading()
        self.sleep(1)

    # ===================================以下为dgq封装方法，亦可用==============================

    # 输入内容方法，输入
    def Input(self, ele_type, value, inputvalue):
        try:
            if ele_type == "xpath":
                self.driver.find_element_by_xpath(value).send_keys(inputvalue)
            elif ele_type == "class_name":
                self.driver.find_element_by_class_name(value).send_keys(inputvalue)
            elif ele_type == "id":
                self.driver.find_element_by_id(value).send_keys(inputvalue)
            elif ele_type == "name":
                self.driver.find_element_by_name(value).send_keys(inputvalue)
            elif ele_type == "link_text":
                self.driver.find_element_by_link_text(value).send_keys(inputvalue)
            elif ele_type == "partial_link_text":
                self.driver.find_element_by_partial_link_text(value).send_keys(inputvalue)
        except Exception as e:
            raise ElementNotFound(e)

    # 鼠标事件方法一,点击
    def Click(self, ele_type, value):
        try:
            if ele_type == "xpath":
                self.driver.find_element_by_xpath(value).click()
            elif ele_type == "class_name":
                self.driver.find_element_by_class_name(value).click()
            elif ele_type == "id":
                self.driver.find_element_by_id(value).click()
            elif ele_type == "name":
                self.driver.find_element_by_name(value).click()
            elif ele_type == "link_text":
                self.driver.find_element_by_link_text(value).click()
            elif ele_type == "partial_link_text":
                self.driver.find_element_by_partial_link_text(value).click()
        except Exception as e:
            raise ElementNotFound(e)

    # 鼠标事件方法二，清除
    def clear_value(self, ele_type, value):
        try:
            if ele_type == "xpath":
                self.driver.find_element_by_xpath(value).clear()
            elif ele_type == "id":
                self.driver.find_element_by_id(value).clear()
            elif ele_type == "name":
                self.driver.find_element_by_name(value).clear()
            elif ele_type == "link_text":
                self.driver.find_element_by_link_text(value).clear()
            elif ele_type == "partial_link_text":
                self.driver.find_element_by_partial_link_text(value).clear()
        except Exception as e:
            raise ElementNotFound(e)

    # 验证元素是否存在
    def Check_element(self, ele_type, value):
        try:
            if ele_type == "xpath":
                self.driver.find_element_by_xpath(value)
            elif ele_type == "id":
                self.driver.find_element_by_id(value)
            elif ele_type == "name":
                self.driver.find_element_by_name(value)
            elif ele_type == "link_text":
                self.driver.find_element_by_link_text(value)
            elif ele_type == "partial_link_text":
                self.driver.find_element_by_partial_link_text(value)
        except Exception as e:
            raise ElementNotFound(e)

    # 获取子元素
    def Select_child_elements(self, ele_type, value1, value2):
        try:
            if ele_type == "xpath":
                Select(self.driver.find_element_by_xpath(value1)).select_by_visible_text(value2)
            elif ele_type == "id":
                Select(self.driver.find_element_by_id(value1)).select_by_visible_text(value2)
            elif ele_type == "name":
                Select(self.driver.find_element_by_name(value1)).select_by_visible_text(value2)
            elif ele_type == "link_text":
                Select(self.driver.find_element_by_link_text(value1)).select_by_visible_text(value2)
            elif ele_type == "partial_link_text":
                Select(self.driver.find_element_by_partial_link_text(value1)).select_by_visible_text(value2)
        except Exception as e:
            raise ElementNotFound(e)

    # 获取输入框的值
    def Get_attribute(self, ele_type, value1, value2):
        try:
            if ele_type == "xpath":
                Value = self.driver.find_element_by_xpath(value1).get_attribute(value2)
                return Value
            elif ele_type == "name":
                Value = self.driver.find_element_by_name(value1).get_attribute(value2)
                return Value
            elif ele_type == "link_text":
                Value = self.driver.find_element_by_link_text(value1).get_attribute(value2)
                return Value
            elif ele_type == "class_name":
                Value = self.driver.find_element_by_class_name(value1).get_attribute(value2)
                return Value
            elif ele_type == "id":
                Value = self.driver.find_element_by_id(value1).get_attribute(value2)
                return Value
        except Exception as e:
            raise ElementNotFound(e)

    # 获取下拉框的文本的值
    def Get_text(self, ele_type, value):
        try:
            if ele_type == "xpath":
                text = self.driver.find_element_by_xpath(value).text
                return text
            elif ele_type == "name":
                text = self.driver.find_element_by_name(value).text
                return text
            elif ele_type == "link_text":
                text = self.driver.find_element_by_link_text(value).text
                return text
            elif ele_type == "class_name":
                text = self.driver.find_element_by_class_name(value).text
                return text
            elif ele_type == "id":
                text = self.driver.find_element_by_id(value).text
                return text
        except Exception as e:
            raise ElementNotFound(e)

    # 显性等待时间,注意这里用classname定位元素的，也可以用其他
    def WebDriverWait(self, MaxTime, Mimtime, value):
        # element = self.driver.find_element(By.XPATH, value)
        WebDriverWait(self.driver, MaxTime, Mimtime).until(lambda x: x.find_element_by_xpath(value).is_displayed())

    # # 鼠标移动点击机制
    def Move_action(self, ele_type, value):
        try:
            if ele_type == "xpath":
                xm = self.driver.find_element_by_xpath(value)
                webdriver.ActionChains(self.driver).click(xm).perform()
            elif ele_type == "id":
                xm = self.driver.find_element_by_id(value)
                webdriver.ActionChains(self.driver).click(xm).perform()
            elif ele_type == "name":
                xm = self.driver.find_element_by_name(value)
                webdriver.ActionChains(self.driver).click(xm).perform()
            elif ele_type == "link_text":
                xm = self.driver.find_element_by_link_text(value)
                webdriver.ActionChains(self.driver).click(xm).perform()
        except Exception as e:
            raise ElementNotFound(e)

    # 校验按钮是否为选中状态
    def Is_selected(self, ele_type, value):
        try:
            if ele_type == "id":
                self.driver.find_element_by_id(value).is_selected()
            elif ele_type == "xpath":
                self.driver.find_element_by_xpath(value).is_selected()
            elif ele_type == "class_name":
                self.driver.find_element_by_class_name(value).is_selected()
            elif ele_type == "name":
                self.driver.find_element_by_name(value).is_selected()
            elif ele_type == "link_text":
                self.driver.find_element_by_link_text(value).is_selected()
        except Exception as e:
            raise ElementNotFound(e)
