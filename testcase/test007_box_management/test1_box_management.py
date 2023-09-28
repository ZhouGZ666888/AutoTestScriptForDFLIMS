# -*- coding: utf-8 -*-
# @Time    : 2022/08/15
# @Author  : guanzhou.zhou

import time
import unittest
from conf.enter_tab import EnterTab
from pageobj.hwglPage import *
from common.setup_teardown import MyTest


class SampleBoxManagement(MyTest):

    def setUp(self) -> None:
        self.hwgl = SampleHwgl(self.driver)

    def user_enter_order(self):
        """调用进入模块功能"""
        # 调用登录(单独调试case用，批量跑用例则需要注释)
        self.initialize()
        EnterTab.enter_storage_center(self.basepage)  # 点击样本库位管理的tab按钮
        EnterTab.enter_box_user(self.basepage)  # 点击盒位管理的tab按钮

    def test01_box_list_search(self):
        """测试样本盒管理列表页搜索功能"""
        self.user_enter_order()  # 调用进入模块功能
        self.hwgl.hwgl_list_search()  # 列表搜索

    def test02_box_list_delete(self):
        """测试样本盒管理列表页删除功能"""
        # 列表删除盒位
        self.hwgl.hwgl_list_delete()

    def test03_box_list_add(self):
        """测试样本盒管理列表页新增盒子功能"""
        now = time.strftime("%Y-%m-%d-%H:%M:%S")
        print(now)
        box_name = '盒子_' + str(now)
        # self.user_enter_order()  # 调用进入模块功能
        self.hwgl.hwgl_list_add(box_name)  # 每次新建一个盒子


if __name__ == '__main__':
    unittest.main()
