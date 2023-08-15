import re

from selenium import webdriver
import time
from PIL import Image
import ddddocr

driver = webdriver.Chrome()
driver.get("https://testzgzncov.dinfectome.com/dflimsf/welcome")
driver.maximize_window()
time.sleep(2)
file_name1 = "test1.png"
file_name2 = "test2.png"


def readIdentification():
    # 1.登录页面先截图并保存在test1.png
    driver.save_screenshot(file_name1)
    # 2.获取图片验证码坐标和尺寸
    time.sleep(1)
    code_element = driver.find_element_by_id(".el-card__body .el-form .form-coat:nth-child(3) img")  # 验证码定位
    # 获取验证码坐标
    left = code_element.location['x']
    # print(left)
    top = code_element.location['y']
    # print(top)
    right = code_element.size['width'] + left
    height = code_element.size['height'] + top
    im = Image.open(file_name1)
    # 3.截取图片验证码
    img = im.crop((left, top, right, height))
    # 4.截取的验证码图片保存为新的文件
    img.save(file_name2)

    h = ddddocr.DdddOcr()
    with open(file_name2, 'rb') as f:
        imgs = f.read()
    result = h.classification(imgs)
    print(result)
    result = re.search(r'验证码错误，请重新输入', driver.page_source)
    if result:
        driver.refresh()
        return readIdentification()
    #
    # driver.close()
    # driver.quit()


readIdentification()
# driver.find_element_by_css_selector('.el-card__body .el-form .form-coat:nth-child(1) input').clear()
# driver.find_element_by_css_selector('.el-card__body .el-form .form-coat:nth-child(1) input').send_keys('zhougaunzhong')
# driver.find_element_by_css_selector('.el-card__body .el-form .form-coat:nth-child(2) input').clear()
# driver.find_element_by_css_selector('.el-card__body .el-form .form-coat:nth-child(2) input').send_keys('Aa123456')
# driver.find_element_by_css_selector('.el-card__body .el-form .form-coat:nth-child(3) input').clear()
# driver.find_element_by_css_selector('.el-card__body .el-form .form-coat:nth-child(3) input').send_keys(result)
#
# driver.find_element_by_css_selector('.el-card__body .el-form .login-btn').click()
