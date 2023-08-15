# -*- coding: utf-8 -*-
# @Time    : 2022/07/01
# @Author  : guanzhong.zhou
# @File    : 登录页面元素定位
# -*-*************************************************************************************-*-

# js = "document.getElementById('enterpriseUser1').style.display = 'block';document.getElementById('enterpriseUser').style.display = 'none'"
#切换登录方式
choice_login_style = '#wechatLogin .login-type-tip-text'

# 账号登录页，用户名输入框
username_loc = '.main_right .el-card__body div:nth-child(3) form div:nth-child(1)  div div input'

# 账号登录页，密码输入框
password_loc = '.main_right .el-card__body div:nth-child(3) form div:nth-child(2)  div div input'

# 登录按钮
login_btn_loc = '.main_right .el-card__body div:nth-child(3) form div:nth-child(3)  button'

#登录成功后首页面，选择城市
selection_lab='.el-select input'

#选择登录城市：南京
select_login_city='//*[@class="el-select-dropdown el-popper"]/descendant::li[child::span[text()="南京"]]'

# 选择城市确认按钮
select_login_city_confirm='.el-dialog--center button'