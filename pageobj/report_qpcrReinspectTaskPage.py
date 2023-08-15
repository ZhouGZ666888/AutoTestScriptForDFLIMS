# -*- coding: utf-8 -*-
# @Time    : 2022/09/20
# @Author  : guanzhong.zhou
# @File    : 报告-qpcr复检任务模块页面方法封装

from common.editYaml import read_yaml,save_yaml
from common.screenshot import Screenshot
from PageElements.report_qpcrReinspectTask_ele import *
from conf.all_path import mNGTaskSampleId,sjNubForQpcrFile
from uitestframework.basepageTools import BasePage
from common.logs import log


def getseqSampleId():
    """
    获取生成复检任务模块存的上机号
    """
    seqSampleId = read_yaml(sjNubForQpcrFile)['sj_nub']
    return seqSampleId


class QPCRReinspectTask(BasePage):
    """报告-qpcr复检任务模块页面基础方法封装"""

    def serach_sample_by_seqSampleId(self):
        """根据样本号查询待分配样本"""
        idNub = getseqSampleId()
        log.info("根据上机号查询复检任务样本：%s"%idNub)
        self.input('css', seqSampleIdLabs_input, idNub)
        self.clicks('css', search_btn)
        self.wait_loading()
        samples = self.findelements('css', all_orders.format(3))
        log.info("获取到的复检任务编号：%s" % samples)
        self.sleep(1)
        return len(samples)

    def qpcr_multiple_out(self):
        """复检任务批量出库"""
        log.info("复检任务批量出库")
        # 先提取复检任务样本号，在qpcr模块使用
        sample_id = self.get_text('css', all_orders.format(9))
        log.info("取出上机号：{}".format(sample_id))
        urldata = read_yaml(mNGTaskSampleId)
        urldata["mNGSinspectTaskSampleId"] = sample_id
        save_yaml(mNGTaskSampleId,urldata) # 写入模式获取的URL地址到yaml文件中

        self.clicks('css', all_orders.format(9))
        self.clicks('css', multiple_out)
        self.wait_loading()
        Screenshot(self.driver).get_img("复检任务批量出库")
        multiple_out_user = self.get_text('css', all_orders.format(12))
        print(multiple_out_user)
        return multiple_out_user



if __name__ == '__main__':
    sss=getseqSampleId()
    print(sss)