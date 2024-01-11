# -*- coding: utf-8 -*-
# @File    : 系统中各模块执行SQL语句汇总


# 病历模块查询数据库是否存在相同身份证
bl_sql = "SELECT count(*) from crm_patient_t where identification_no ='{}';"

# 订单模块查询订单表是否存在新建订单号
order_isexists_sql = "select count(*) from order_info_t where order_code='{}'; "
# 接样写入备注
ybjs_sql = "UPDATE sample_receive_item_t set remarks='自动化测试数据' where order_code='{}';"

# j接样表，获取样本lims号、实验室号和样本报告类型
ybjs_sql2 = "SELECT t1.sample_id_lims,t3.sample_main_lab_code,t2.dt_name_cn FROM sample_receive_item_t t1,bas_dictionary_t t2,sample_id_lab_v t3 WHERE t1.order_code = '{}' AND t1.product_id = t2.dt_code and t1.sample_id_lims=t3.sample_id_lims AND t2.dt_type = 'report_type';"

#接样获取订单产品表最新的order_product_id编号
ybjs_get_order_product_id="SELECT order_product_id from order_product_t ORDER BY order_product_id desc LIMIT 1;"

#接样获取订单项目表最新的order_project_id编号
ybjs_get_order_project_id="	SELECT order_project_id from order_project_t ORDER BY order_project_id desc LIMIT 1;"

#接样设置订单检测产品
ybjs_set_product="INSERT INTO order_product_t(order_product_id, order_code, product_id, remarks, is_valid, reason_of_invalid, created_by, created_by_name, creation_date, mod_by, mod_by_name, mod_date) VALUES ({}, '{}', 'G001', NULL, '1', NULL, 'dongguoqi', '董国奇', now(), 'dongguoqi', '董国奇', now());"

#接样设置订单检测项目
ybjs_set_project="INSERT INTO order_project_t(order_project_id, order_code, project_id, remarks, is_valid, reason_of_invalid, created_by, created_by_name, creation_date, mod_by, mod_by_name, mod_date) VALUES ({}, '{}', 'J019', NULL, '1', NULL, 'zhouguanzhong', '周官钟', now(), 'wangchao83198', '周官钟', now());"

# 获取一条sr样本lims号
get_sr_sample_lims = "select sample_id_lims from sample_receive_item_t where order_code='{}' and sample_type='C2016120700002' limit 1;"

# 修改获取sr样本的外部样本编号
set_sr_sample_id_external = "update sample_receive_item_t set sample_id_external='{}' where sample_id_lims='{}';"

# 样本处理明细表,更新盒内位置
ybcl_detail_sql = "UPDATE exp_preparation_item_t set position_in_box=1 where task_id='{}';"

# 样本处理结果表，获取样本lims号和实验室号
ybcl_detail_sql2 = "SELECT t1.sample_id_lims,t1.sample_main_lab_code from sample_id_lab_v t1 WHERE t1.sample_id_lims in (SELECT t2.sample_id_lims from exp_preparation_result_t t2 where t2.task_id ='{}');"

# 样本处理结果表，更新血浆样本评级为A
ybcl_detail_sql3 = "UPDATE exp_preparation_result_t set sample_qc_level ='1' where task_id ='{}';"

# 核酸提取明细表,计量余量、包装量
hstq_detail_sql = "UPDATE exp_extraction_item_t set remaining_sample_amt=19,actual_sample_pkg_amt=1 where task_id='{}';"

# 核酸提取明细表,样本计量（实测）
hstq_detail_sql3 = "UPDATE exp_extraction_item_t set actual_sample_amt=20 where task_id='{}';"

# 查询提取明细表样本lims号
hstq_detail_sql2 = "SELECT sample_id_lims from exp_extraction_item_t where task_id='{}' AND deposit_type='01';"

# 核酸提取结果表,产物Qubit浓度、产物Nanodrop浓度、OD260/280、OD260/230
hstq_result_sql = "UPDATE exp_extraction_result_t set consistence_amt=20 where task_id='{}';"

#提取模块对生成的对照样本在数据库中设置预期通量
check_sample_set="UPDATE sample_info_t SET preinstall_throughput = 7.14 WHERE sample_id_lims IN ( SELECT sample_id_lims FROM sample_info_t WHERE previous_sample_id_lims IN ( SELECT sample_id_lims FROM sample_info_t WHERE previous_sample_id_lims in ( SELECT sample_id_lims FROM sample_info_t WHERE previous_sample_id_lims in ( SELECT sample_id_lims FROM exp_extraction_item_t WHERE sample_type_id = 'C2021051900026' AND task_id = '{}' ) ) ) ) AND current_step <> 'qpcr';"


# 文库构建明细表
# 是否选大小、使用体积、建库进入量、补水体积、余样体积、余样总量
wkgj_detail_sql1 = "UPDATE exp_libconstruction_item_t set selected_bigness=0 where task_id='{}';"

# 构建明细表查询样本lims号
wkgj_detail_sql2 = "SELECT sample_id_lims from exp_libconstruction_item_t where task_id='{}';"

#构建明细表查询样本lims号和实验室号
wkgj_detail_sql3="SELECT t1.sample_id_lims,t1.sample_id_lab from  sample_id_lab_v t1 JOIN exp_libconstruction_item_t t2  on t1.sample_id_lims =t2.sample_id_lims where t2.task_id='{}';"






# 文库构建结果表
# 文库浓度1ng/μL*、文库浓度2ng/μL*、平均文库浓度ng/μL*、index_id录入
wkgj_result_sql1 = "UPDATE exp_libconstruction_result_t set consistence_amt=5,consistence_amt_one=5,consistence_amt_two=5 where task_id='{}';"

wkgj_result_sql2 ="UPDATE sample_info_t SET preinstall_throughput = 7.14 WHERE sample_id_lims IN ( SELECT " \
                  "sample_id_lims FROM sample_info_t WHERE previous_sample_id_lims IN ( SELECT sample_id_lims FROM " \
                  "sample_info_t WHERE previous_sample_id_lims in ( SELECT sample_id_lims FROM sample_info_t WHERE previous_sample_id_lims in ( 	SELECT t.original_sample_id_lims FROM	 exp_libconstruction_item_t t JOIN sample_info_t t1  on t.original_sample_id_lims =t1.sample_id_lims WHERE   t1.sample_type = 'C2021051900026'and t.task_id='{}') ) ) ) AND current_step <> 'qpcr';"

# 查询一条最新的样本盒，作为96孔板编号写入数据库
wkgj_result_sql5 = "UPDATE exp_libconstruction_result_t set well_plates_code=(SELECT  box_name from  sample_box_info_t ORDER BY creation_date DESC LIMIT 1) WHERE task_id='{}';"
# 构建设置Adapter(index_id )
wkgj_result_sql6 = "UPDATE  exp_libconstruction_result_t set index_id ='1' WHERE task_id='{}';"

# 文库富集明细表,获取lims号
wkfj_detail_sql1 = "SELECT sample_id_lims from exp_pooling_item_t WHERE task_id = '{}';"
wkfj_detail_sql2 = "UPDATE sample_info_t SET preinstall_throughput = 7.14 WHERE sample_id_lims in (SELECT sample_id_lims from sample_info_t WHERE original_sample_id_lims in (SELECT sample_id_lims from sample_receive_item_t WHERE order_code ='{}') and previous_step='libconstruction');"
wkfj_detail_sql3 = "SELECT sit.previous_sample_id_lims FROM sample_info_t sit INNER JOIN ( SELECT sample_id_lims FROM sample_info_t WHERE preinstall_probe IS NOT NULL AND order_code = '{}' ) AS subquery ON sit.sample_id_lims = subquery.sample_id_lims WHERE sit.module_task_id IS NULL ORDER BY sit.sample_id_lims asc limit 1;"



# 文库富集结果表

# mpcr明细表
mpcr_96_well_plate = "UPDATE exp_mpcr_item_t SET position_in_orifice={}  where task_id='{}' and sample_id_lims='{}';"

# 查询mpcr明细表样本lims号
mpcr_detail_lims_sql = "SELECT sample_id_lims from exp_mpcr_item_t where task_id='{}';"

# 查询mpcr结果表样本lims号
mpcr_result_lims_sql = "SELECT sample_id_lims from exp_mpcr_result_t where task_id='{}';"

# 文库定量明细表
# 获取样本总数
wkdl_detail_sql1 = "SELECT count(*) from exp_libquant_item_t WHERE task_id = '{}';"

# 设置明细表余样本包装量
wkdl_detail_sql2 = "UPDATE exp_libquant_item_t set remaining_sample_pkg_amt=1 WHERE task_id = '{}';"

# 数据库获取定量明细表lims号
wkdl_detail_sql3 = "SELECT sample_id_lims from exp_libquant_item_t WHERE task_id = '{}';"

# 文库定量结果表
# 获取样本总数
wkdl_result_sql1 = "SELECT count(*) from exp_libquant_result_t WHERE task_id ='{}';"

# 上机
# 浓度调整前样本明细
# 更新浓度调整前样本明细【取样】值
sj_detail_before_concentration_sql1 = "UPDATE exp_sequencing_item_t SET used_volume_amt =1,preinstall_lane_num=3 WHERE task_id='{}';"

# 获取lims样本号
sj_detail_before_concentration_sql2 = "SELECT sample_id_lims from exp_sequencing_item_t WHERE task_id='{}';"

# 浓度调整后样本明细
# 设置调整后摩尔浓度,余样包装量
sj_detail_after_concentration_sql1 = "UPDATE exp_sequencing_item_adjusted_t SET volume_amt=20 WHERE task_id='{}';"
# 设置余样包装量
sj_detail_after_concentration_sql3 = "UPDATE exp_sequencing_item_adjusted_t SET remaining_sample_pkg_amt=1 WHERE task_id='{}';"

# 获取样本lims号
sj_detail_after_concentration_sql2 = "SELECT sample_id_lims from exp_sequencing_item_adjusted_t WHERE task_id='{}';"

# QPCR
qpcr_sql = "SELECT sample_id_lims from exp_qpcr_item_t where deposit_type ='01' and task_id='{}';"

# 到数据库中查询需要条件的原始样本号：按照FFPE白片，接样直接到提取的流转表来搜索数据库满足条件的原始样本号，即满足提取待选表的sql。
# 如果需要检索具体的样本，在本sql最后面加上该条件即可：---AND t.previous_sample_id_lims = 'GS2110200044'
lzb_get_sql1 = """SELECT DISTINCT t.previous_sample_id_lims AS sampleIdLims, t3.sample_id_lab AS sampleIdLab FROM 
sample_info_t t 
INNER JOIN sample_receive_item_t t2 ON (t.original_sample_id_lims = t2.sample_id_lims AND t.is_valid = '1') 
INNER JOIN sample_info_t tp ON (t.previous_sample_id_lims = tp.sample_id_lims) LEFT JOIN sample_id_lab_v t3 ON 
(t.previous_sample_id_lims = t3.sample_id_lims) LEFT JOIN bas_sample_type_t t4 ON (tp.sample_type = t4.sample_type_id) 
WHERE t.is_valid = '1' AND t.current_step = '{}' AND t.workflow_status = '04' AND t.sample_status IS NULL """

# 通过系统检索出，F，T大类的样本，在流转表设置病理任务，否则无法设置,('C2012120800006','C2012120800003')分别代表F,T大类,且当前还没有设置过病理任务的
lzb_get_sql2 = """SELECT DISTINCT t.previous_sample_id_lims AS sampleIdLims, t3.sample_id_lab AS sampleIdLab FROM 
sample_info_t t 
INNER JOIN sample_receive_item_t t2 ON (t.original_sample_id_lims = t2.sample_id_lims AND t.is_valid = '1') 
INNER JOIN sample_info_t tp ON (t.previous_sample_id_lims = tp.sample_id_lims) LEFT JOIN sample_id_lab_v t3 ON 
(t.previous_sample_id_lims = t3.sample_id_lims) LEFT JOIN bas_sample_type_t t4 ON (tp.sample_type = t4.sample_type_id)
WHERE t.is_valid = '1' AND t.current_step = '{}' AND t.workflow_status = '04' AND t.sample_status IS NULL AND 
tp.sample_type IN ('C2012120800006','C2012120800003') AND t.previous_sample_id_lims NOT IN (SELECT tpa.sample_id_lims 
FROM pathology_sample_task tpa WHERE tpa.is_valid='1')
"""

# 通过系统检索出，接样节点样本是库内的，用于接样出库(样本类型是FF白片的)
lzb_get_sql3 = """SELECT sample_id_lims,order_code FROM sample_info_t  WHERE previous_sample_id_lims IS NULL 
AND sample_status='01' AND workflow_status= '01' AND current_step ='reception'  AND sample_type='C2021051900001'"""

# 通过系统检索出，可以在流转表修改建库信息的样本，修改建库信息就可以修改富集信息。
lzb_get_sql4 = """SELECT t.original_sample_id_lims FROM sample_info_t t WHERE t.sample_id_lims LIKE '%D00%' AND 
t.sample_status IS NULL AND workflow_status ='02'"""

# 通过系统检索出，在库内的富集/定量实体样本
lzb_get_sql5 = """SELECT t.sample_id_lims FROM sample_info_t t WHERE t.sample_id_lims LIKE 'FJ%' AND t.sample_status ='01' AND workflow_status ='01'"""
lzb_get_sql6 = """SELECT t.sample_id_lims FROM sample_info_t t WHERE t.sample_id_lims LIKE 'ZC%' AND t.sample_status ='01' AND workflow_status ='01'"""
lzb_get_sql7="SELECT original_sample_id_lims as sampleidlims from  sample_info_t WHERE current_step = '{}' AND " \
             "workflow_status = '04'AND sample_status IS NULL order by creation_date desc;"
# 通过系统检索出，库内的样本
ybck_get_sql5 = """SELECT t.sample_id_lims FROM sample_info_t t WHERE t.sample_id_lims LIKE 'GS%' AND t.sample_status ='01' AND workflow_status ='01'"""

# 数据库获取实验流程结果表下一步流向
next_step_sql = "SELECT  DISTINCT previous_sample_id_lims,sample_id_lab_core,current_step FROM sample_info_t WHERE (" \
                "previous_sample_id_lims IN ( SELECT sample_id_lims FROM {} WHERE task_id = '{}') AND is_valid = '1')"

# 数据库获取富集结果表下一步流向
fj_next_step = "SELECT sample_id_lims, pooling_name, next_step_name FROM {}  WHERE task_id = '{}';"

# 数据库获取定量结果表下一步流向
dl_next_step = "SELECT sample_id_lims,sqc_group_num,next_step_name FROM {}  WHERE task_id='{}';"

# 样本项目信息修改筛选符合条件项目信息
project_id = "SELECT project_id FROM bas_project_info_t WHERE  ( project_id like 'P%' OR project_id like 'M%' or project_id like 'Y%')and is_valid='1';"

# 样本项目信息修改后，数据库获取修改后的样本项目信息
sampleProId = "SELECT project_id,is_valid from exp_result_sample_project_t  WHERE sample_id_lims ='{}';"

# 样本消息通知，获取待选表样本，此处以核酸提取待选表为例
sampleMsgNotice = "SELECT DISTINCT t.previous_sample_id_lims,t.estimated_generated_time FROM sample_info_t t INNER JOIN sample_receive_item_t t2 ON (t.original_sample_id_lims = t2.sample_id_lims AND t.is_valid = '1') INNER JOIN sample_info_t tp ON (t.previous_sample_id_lims = tp.sample_id_lims) LEFT JOIN sample_id_lab_v t3 ON (t.previous_sample_id_lims = t3.sample_id_lims) LEFT JOIN bas_sample_type_t t4 ON (tp.sample_type = t4.sample_type_id) WHERE t.is_valid = '1' AND t.current_step = 'extraction' AND t.workflow_status = '04' AND t.sample_status IS NULL  ORDER BY t.estimated_generated_time DESC limit 1;"

# 在出库列表中，搜索库内样本
ybck_get_sql1 = """SELECT t.sample_id_lims FROM sample_info_t t WHERE t.sample_id_lims LIKE 'GS%' AND t.sample_status ='01' 
AND workflow_status ='01' ORDER BY t.creation_date DESC"""

# 接样样本出库的sql
ybck_get_sql2 = """SELECT t.sample_id_lims FROM sample_info_t t
LEFT JOIN exp_result_sample_project_t t2 ON (t.sample_id_lims=t2.sample_id_lims)
WHERE t.sample_id_lims LIKE 'GS%' AND t.sample_status ='01' 
AND t2.project_id IS NOT NULL
AND workflow_status ='01' AND t.original_sample_id_lims=t.sample_id_lims AND sample_type='C2012120800006'"""

# 查询提取节点可出库的样本
ybck_get_sql3 = """SELECT t.sample_id_lims FROM sample_info_t t
LEFT JOIN exp_result_sample_project_t t2 ON (t.sample_id_lims=t2.sample_id_lims)
WHERE t.sample_id_lims LIKE 'GS%' AND t.sample_status ='01' 
AND workflow_status ='01' AND t.current_step='extraction' 
AND t2.project_id IS NOT NULL"""

# 查询富集节点可出库的样本
ybck_get_sql4 = """SELECT t.libquant_lims_id FROM sample_info_t t 
LEFT JOIN exp_result_sample_project_t t2 ON (t.sample_id_lims=t2.sample_id_lims)
WHERE t.sample_id_lims LIKE 'GS%' AND t.sample_status ='01' 
AND workflow_status ='01' AND t.current_step='libquant' 
AND t2.project_id IS NOT NULL"""
