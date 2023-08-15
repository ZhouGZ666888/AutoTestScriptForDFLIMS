# -*- coding: utf-8 -*-
# @Time    : 2022/08/25
# @Author  : guanzhou.zhou
import time
import unittest
from conf.enter_tab import EnterTab
from pageobj.kwglPage import *
from common.setup_teardown import MyTest


class SampleStorageManagement(MyTest):
    def setUp(self) -> None:
        self.kwgl = SampleKwgl(self.driver)

    def user_enter_order(self):
        """
        调用进入模块功能
        """
        # 调用登录(单独调试case用，批量跑用例则需要注释)
        self.initialize()
        EnterTab.enter_storage_center(self.basepage)  # 点击样本库位管理的tab按钮
        EnterTab.enter_storage_user(self.basepage)  # 点击库位管理的tab按钮

    def test01_storage_add_temporary(self):
        """
        测试新增临时库功能
        """

        self.kwgl.kwgl_change_role('2535', '2001', '0')  # 使用数据库，将用户修改为非库管角色
        self.user_enter_order()  # 调用进入模块功能
        now = time.strftime("%Y-%m-%d-%H:%M:%S")
        storage_name = '测试专用-' + str(now)
        self.kwgl.kwgl_add_temporary_storage(storage_name, '董国奇')  # 增加库位
        self.kwgl.wait_loading()

    def test02_list_search_temporary(self):
        """
        测试库位管理列表页搜索功能
        """
        # self.user_enter_order()  # 调用进入模块功能

        self.kwgl.kwgl_list_search('测试专用-')
        self.kwgl.wait_loading()


if __name__ == '__main__':
    unittest.main()
