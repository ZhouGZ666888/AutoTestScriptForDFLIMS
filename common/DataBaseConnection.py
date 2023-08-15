import pymysql
import psycopg2

from common.editYaml import get_order
from conf.execute_sql_action import ybjs_get_order_product_id,ybjs_set_product


class GetSqlHelper:
    def __init__(self):

        # 以下提供脚本需要的数据和变量(Test环境)
        # ==================27-mysql-basdb数据库信息==================
        self.base_ip = "172.16.18.27"
        self.base_user = "dba_user"
        self.base_password = "C25ARoFOYe5A"
        self.base_database = "basdb"
        self.base_port = 3306

        # ==================27-PG-lims数据库信息==================
        self.test_limsdb_ip = "172.16.18.27"
        self.test_limsdb_user = "lims_dfu"
        self.test_limsdb_password = "H5GEsiQifOn1"
        self.test_limsdb_database = "df_lims"
        self.test_limsdb_port = 5432

        self.con = None  # 初始化连接对象
        self.cur = None  # 初始化游标

    # 27MySQL base库连接，执行权限修改等操作
    def test_getCon_limsbasdb(self):
        """
        27MySQL base库连接，执行权限修改等操作
        :return: conn游标
        """
        try:
            self.con = pymysql.connect(
                database=self.base_database,
                user=self.base_user,
                password=self.base_password,
                host=self.base_ip,
                port=self.base_port)
        except pymysql.Error as e:
            print("建立数据库Connect对象失败:%s" % e)
        try:
            # 创建游标
            self.cur = self.con.cursor()
        except Exception as e:
            print('建立游标失败：', e)

    # 127PG库连接，执行基础增、删、改、查操作
    def test_getCon_limsPg(self):
        """
        127PG库连接，执行基础增、删、改、查操作
        :return: conn游标
        """
        try:
            self.con = psycopg2.connect(
                database=self.test_limsdb_database,
                user=self.test_limsdb_user,
                password=self.test_limsdb_password,
                host=self.test_limsdb_ip,
                port=self.test_limsdb_port)

        except pymysql.Error as e:
            print("建立数据库Connect对象失败:%s" % e)
        try:
            # 创建游标
            self.cur = self.con.cursor()
        except Exception as e:
            print('建立游标失败：', e)

    # 关闭游标，关闭链接
    def close_func(self):
        """关闭游标，关闭链接"""
        try:
            self.cur.close()
            print('关闭游标成功')
        except Exception as e:
            print('关闭游标失败：', e)

        try:
            self.con.close()
            print('关闭链接成功!')
        except Exception as e:
            print('关闭链接失败：', e)

    # 查询27basemysql数据库
    def test_select_limsbasdb(self, sql):
        """
        27base库查询方法封装
        :param sql: 查询语句
        :return: 获取查询结果
        """
        self.test_getCon_limsbasdb()
        try:
            self.cur.execute(sql)
            fc = self.cur.fetchall()
            self.close_func()
            return fc
        except pymysql.Error as e:
            print("pymysql Error:%s" % e)

    # 更新27base基础库方法
    def test_update_27mysql(self, sql):
        """27base基础库增，删，改 封装方法"""
        self.test_getCon_limsbasdb()
        try:
            self.cur.execute(sql)
            self.con.commit()
            self.close_func()
        except pymysql.Error as e:
            self.con.rollback()
            print("pymysql Error:%s" % e)

    # 查询迪飞27pg数据库
    def test_select_limsdb(self, sql):
        """27业务库查询
        :param sql: 查询语句
        :return: 返回列名加值组成的列表[{col1:data,col2:data},{col1:data,col2:data},...]
        """
        self.test_getCon_limsPg()
        try:
            self.cur.execute(sql)
            fc = self.cur.fetchall()
            desc = self.cur.description
            data_dict = [dict(zip([col[0] for col in desc], row)) for row in fc]
            self.close_func()
            return data_dict  # 返回列名组成的字典表，装进list里
        except pymysql.Error as e:
            print("pymysql Error:%s" % e)

    # 迪飞27业务库更新方法
    def __edit(self, sql):
        """27业务库增，删，改 封装方法"""
        self.test_getCon_limsPg()
        try:
            self.cur.execute(sql)
            self.con.commit()
        except pymysql.Error as e:
            self.con.rollback()
            print("pymysql Error:%s" % e)
        self.close_func()

    def test_updateByParam(self, sql):
        """修改"""
        self.__edit(sql)

    def test_deleteByParam(self, sql):
        """删除"""
        self.__edit(sql)

    def test_insertByParam(self, sql):
        """新增"""
        self.__edit(sql)


# 建立实例对象，由其它模块引用
executeSql = GetSqlHelper()


if __name__ == '__main__':
    check_sample_set = "UPDATE sample_info_t SET preinstall_throughput = 7.14 WHERE sample_id_lims IN ( SELECT " \
                       "sample_id_lims FROM sample_info_t WHERE previous_sample_id_lims IN ( SELECT sample_id_lims FROM sample_info_t WHERE previous_sample_id_lims in ( SELECT sample_id_lims FROM sample_info_t WHERE previous_sample_id_lims in ( SELECT sample_id_lims FROM exp_extraction_item_t WHERE sample_type_id = 'C2021051900026' AND task_id = '{}' ) ) ) ) AND current_step <> 'qpcr';"

    sqls="INSERT INTO order_product_t(order_product_id, order_code, product_id, remarks, is_valid, reason_of_invalid, created_by, created_by_name, creation_date, mod_by, mod_by_name, mod_date) VALUES ({}, '{}', 'G001', NULL, '1', NULL, 'dongguoqi', '董国奇', '2023-05-30 14:08:26', 'dongguoqi', '董国奇', '2023-05-30 14:08:26');"
    sd=ybjs_get_order_product_id
    executeSql.test_updateByParam(check_sample_set.format('HSTQ2023080300001'))
