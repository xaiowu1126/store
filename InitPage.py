'''
    1.数据类：
        只准备数据部分：不参与任何操作。
    任务1：
        将这个框架的数据源集中写到excel表里，使用xlrd读取
        xlrd参数化，mysql的参数化。
'''
import  xlrd
import pymysql

class  InitPage():
    # excell 表格导入操作

    # 打开工作簿
    # wd = xlrd.open_workbook(filename=r"D:\python自动化测试资料\python\python自动化测试\day03\任务\HKR.xlsx", encoding_override=True)
    # # 打开相对应的选项卡
    # st1 = wd.sheet_by_name("成功数据")
    # #获取所有行数
    # nrows = st1.nrows
    # # 写入所需数据
    # login_success_data = []
    # dict = {}
    #
    # for i in range(1, nrows):
    #     data = st1.row_values(i)
    #     dict = {"username": data[0], "password": data[1], "expect": data[2]}
    #     login_success_data.append(dict)
    #
    # # 生成的列表格式
    # # login_success_data = [
    # #     {"username": "jason", "password": "1234567", "expect": "Student Login"},
    # #     {"username": "不再爱了", "password": "1234567", "expect": "Student Login"}
    # # ]
    #
    #
    # st2 = wd.sheet_by_name("失败数据")
    # # 获取所有行数
    # nrows = st2.nrows
    # login_error_data = []
    #
    # for i in range(1, nrows):
    #     data = st2.row_values(i)
    #     dict = {"username": data[0], "password": data[1], "expect": data[2]}
    #     login_error_data.append(dict)


    # 数据库导入操作
    # 1、连接数据库
    con = pymysql.connect(host="localhost",user="root",password="root",database="汉科软")
    # 2、创建控制台
    cursor = con.cursor()
    # 3、创建SQL语句
    sql1 = "select * from login_c "
    sql2 = "select * from login_s "
    # 4、执行sql 语句
    cursor.execute(sql1)
    list =cursor.fetchall()
    login_success_data = []
    for i in range(len(list)):
        dict = {"username": list[i][0], "password": list[i][1], "expect": list[i][2]}
        login_success_data.append(dict)

    cursor.execute(sql2)
    list2 = cursor.fetchall()
    login_error_data = []
    for i in range(len(list2)):
        dict = {"username": list2[i][0], "password": list2[i][1], "expect": list2[i][2]}
        login_error_data.append(dict)

    #6. 关闭资源
    cursor.close()
    con.close()




























