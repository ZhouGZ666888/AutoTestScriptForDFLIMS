# coding:utf-8
from selenium import webdriver
from common.logs import log
import os, time

from conf.all_path import img_path


# class Screenshot:
#     """截图功能的装饰器"""
#
#     def __init__(self, drivers):
#         self.driver = drivers
#
#     def get_img(self, desc):
#         """截图方法"""
#
#         screen_name = os.path.join(os.path.join(img_path),
#                                    time.strftime('%Y%m%d%H%M%S', time.localtime(time.time())) + '_' + str(
#                                        desc + '预期结果见下图：') + '.png')  # #每个图片的路径
#         log.info("<div><img src='" + screen_name + "' width=600 /></div>")  # 这行代码必须加，如果不加，截图正常，但是无法正常加到报告中，
#         # 所以这里我们加上新增页签，beautifulreport方法就是无脑读print日志的,<div>是换行作用
#         log.info("此步骤的描述信息为：" + str(desc))
#         self.driver.get_screenshot_as_file(screen_name)
#         log.info("截图保存成功")


class Screenshot:
    """截图功能的装饰器"""

    def __init__(self, driver):
        self.driver = driver

    def get_img(self, stepdesc, predesc):
        """截图方法"""
        screen_name = os.path.join(os.path.join(img_path),
                                   time.strftime('%Y%m%d%H%M%S', time.localtime(time.time())) + '_' + '操作步骤：' + str(
                                       stepdesc) + '。预期结果：' + str(predesc) + '，实际结果见下图' + '.png')  # #每个图片的路径

        log.info("<div><img src='" + screen_name + "' width=600 /></div>")  # 这行代码必须加，如果不加，截图正常，但是无法正常加到报告中，
        # 所以这里我们加上新增页签，beautifulreport方法就是无脑读print日志的,<div>是换行用
        log.info('操作步骤：' + str(stepdesc) + '预期结果：' + str(predesc))
        self.driver.get_screenshot_as_file(screen_name)
        log.info("截图保存成功")


if __name__ == '__main__':
    def t_case():
        print("test!")


    dr = webdriver.Chrome()
    dr.get('https:www.baidu.com')
    driver = Screenshot(dr)
    driver.get_img('123')
    dr.quit()
