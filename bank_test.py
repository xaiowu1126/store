info='''
        *********************************************
        *            中国工商银行账户管理系统V1.0        *
        *********************************************
        *                   1、开户                  *
        *                   2、存钱                  *
        *                   3、取钱                  *
        *                   4、转账                  *
        *                   5、查询                  *
        *                   6、退出                  *
        *********************************************
'''
print(info)
import random
import pymysql
UserID=[]
bank_name="工商银行起码路分行"

def con_mysql():
    con=pymysql.connect(host="localhost",user='root',password='123456',database='bank')
    cursor = con.cursor()
    return con,cursor
def get_UserID(cursor):
    sql="select username from person"
    cursor.execute(sql)
    data=cursor.fetchall()
    for i in data:
        UserID.append(i[0])
def close(con,cursor):
    cursor.close()
    con.close()

def bank_adduser(add_info):
    con,cursor=con_mysql()
    get_UserID(cursor)
    if  len(UserID) >100 :return 3
    if add_info['username'] in UserID:return 2
    sql="insert into person values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    param=[add_info['account'],add_info['username'],add_info['password'],add_info['country'],
           add_info['province'],add_info['street'],add_info['door'],add_info['money'],bank_name]
    cursor.execute(sql,param)
    con.commit()
    close(con,cursor)
    return 1
def adduser():
    username=input("请输入您的用户名：")
    password = input("请输入您的密码：")
    print("请输入您的地址：")
    country = input("\t\t请输入您的国家：")
    province = input("\t\t请输入您的省份：")
    street = input("\t\t请输入您的街道：")
    door = input("\t\t请输入您的门牌号：")
    account=random.randint(10000000,99999999)
    add_info={'account':account,'username':username,'password':password,'country':country,'province':province,
              'street':street,'door':door,'money':0}
    status=bank_adduser(add_info)
    if status == 1:
        print("恭喜你开户成功下面是你的信息：")
        info = '''
                    ------------个人信息------------
                    用户名:%s
                    账号：%s
                    密码：********
                    国籍：%s
                    省份：%s
                    街道：%s
                    门牌号：%s
                    余额：%s
                    开户行名称：%s
                '''
        print(info % (username, account, country, province, street, door, add_info["money"], bank_name))
    elif status==2:
        print("开户失败，用户已存在，请重新输入！")
    else:
        print("开户失败，数据库已满！")

def IN_account():
    username=input("请输入您的用户名：")
    IN_money=int(input("请输入您的存入金额："))
    status=deposit(username,IN_money)
    if status==True:
        print("存款成功！")
    else:
        print("输入有误，请重新输入！")
def deposit(username,IN_money):
    con, cursor = con_mysql()
    get_UserID(cursor)
    if username not in UserID or IN_money<0:return False
    sql = "select money from person where username=%s"
    param = [username]
    cursor.execute(sql, param)
    money=cursor.fetchall()
    sql1="update person set money=%s where username=%s"
    param1=[money[0][0]+IN_money,username]
    cursor.execute(sql1,param1)
    con.commit()
    close(con, cursor)
    return True

def OUT_account():
    username=input("请输入您的用户名：")
    password=input("请输入您的密码：")
    OUT_money=int(input("请输入您的取款金额："))
    status=withdraw(username,password,OUT_money)
    if status==1:
        print("账户不存在，请重新输入！")
    elif status==2:
        print("密码错误，请重新输入！")
    elif status==3:
        print("取款金额输入有误，请重新输入取款金额！")
    else:
        print("取款成功！")
def withdraw(username,password,OUT_money):
    con,cursor=con_mysql()
    get_UserID(cursor)
    if username not in UserID:
        return 1
    else:
        sql="select password,money from person where username=%s"
        param=[username]
        cursor.execute(sql,param)
        data=cursor.fetchall()
        if password!=data[0][0]:
            return 2
        else:
            if OUT_money>data[0][1] or OUT_money<=0:
                return 3
            else:
                sql1="update person set money=%s where username=%s"
                param1=[data[0][1]-OUT_money,username]
                cursor.execute(sql1,param1)
                con.commit()
                close(con,cursor)
                return 0

def IO_transfer():
    OUT_username=input("请输入转出账户：")
    OUT_password=input("请输入转出账户的密码：")
    IN_username=input("请输入转入账户：")
    OUT_money=int(input("请输入转出的金额："))
    status=tranfer(OUT_username,IN_username,OUT_password,OUT_money)
    if status == 1:
        print("账户输入有误，请重新输入！")
    elif status==2:
        print("密码错误，请重新输入！")
    elif status==3:
        print("转账金额输入有误，请重新输入转账额度！")
    else:
        print("转账成功！")
def tranfer(OUT_username,IN_username,OUT_password,OUT_money):
    con,cursor=con_mysql()
    get_UserID(cursor)
    sql="select password,money from person where username=%s"
    param=[OUT_username]
    cursor.execute(sql,param)
    OUT_data=cursor.fetchall()
    sql1="select money from person where username=%s"
    param1=[IN_username]
    cursor.execute(sql1,param1)
    IN_data=cursor.fetchall()
    if OUT_username not in UserID or IN_username not in UserID or OUT_username==IN_username:
        return 1
    else:
        if OUT_password!=OUT_data[0][0]:
            return 2
        else:
            if OUT_money>OUT_data[0][1] or OUT_money<=0:
                return 3
            else:
                sql2="update person set money=%s where username=%s"
                param2=[OUT_data[0][1]-OUT_money,OUT_username]
                cursor.execute(sql2,param2)
                sql3="update person set money=%s where username=%s"
                param3=[IN_data[0][0]+OUT_money,IN_username]
                cursor.execute(sql3,param3)
                con.commit()
                close(con,cursor)
                return 0

def re_inquiry():
    username=input("请输入要查询的账户名：")
    password=input("请输入账户密码：")
    inquiry(username, password)

def inquiry(username,password):
    con, cursor = con_mysql()
    get_UserID(cursor)
    if username not in UserID:
        print("该用户不存在，请重新输入！")
    else:
        sql="select * from person where username=%s"
        param=[username]
        cursor.execute(sql,param)
        data=cursor.fetchall()
        if password != data[0][2]:
            print("密码错误，请重新输入！")
        else:
            print("查询成功，下面是您的账户信息：")
            info = '''
                        ------------个人信息------------
                        用户名:%s
                        账号：%s
                        密码：********
                        国籍：%s
                        省份：%s
                        街道：%s
                        门牌号：%s
                        余额：%s
                        开户行名称：%s
                    '''
            print(info % (username, data[0][0],data[0][3],data[0][4],data[0][5],data[0][6],data[0][7],data[0][8]))
            close(con,cursor)

while True:
    begin=input("请输入业务号：")
    if begin == "1":
        print("1、开户")
        adduser()
    elif  begin == "2":
        print("2、存钱")
        IN_account()
    elif  begin == "3":
        print("3、取钱")
        OUT_account()
    elif  begin == "4":
        print("4、转账")
        IO_transfer()
    elif  begin == "5":
        print("5、查询 ")
        re_inquiry()
    elif  begin == "6":
        print("6、退出")
        break