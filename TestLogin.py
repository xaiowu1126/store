from unittest import TestCase
from selenium import webdriver
from ddt import ddt  # ddt简单来说就是测试数据的参数化，测试类必须用@ddt修饰
from ddt import data  # 测试方法使用@data引入数据源
from ddt import unpack  # unpack用于将传入的数据进行拆分
from InitPage import InitPage  # InitPage ，LoginOperation为py文件名
from LoginOperation import LoginOpera
import time

@ddt
class TestLogin(TestCase):
    # setUp()方法 会在所有方法执行前执行
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.get(r"http://localhost:8080/HKR")
        self.driver.maximize_window()

    # tearDown（）在所有用例执行后执行
    def tearDown(self) -> None:
        self.driver.quit()  # 退出浏览器


    @data(*InitPage.login_success_data) #引入登录成功的数据源

    def testSuccessCase1(self,testdata):

        # 提取数据
        username = testdata["username"]
        password =  testdata["password"]
        expect =  testdata["expect"]

        # 调用被测操作类
        loginObj = LoginOpera(self.driver)
        time.sleep(3)
        loginObj.login(username,password)

        # 获取实际结果
        data = loginObj.getSuccessResult()
        #  断言
        self.assertEqual(data,expect)


    @data(*InitPage.login_error_data) #引入登录失败的数据源
    def testSuccessCase2(self,testdata):

        # 提取数据
        username = testdata["username"]
        password =  testdata["password"]
        expect =  testdata["expect"]

        # 调用被测操作类
        loginObj = LoginOpera(self.driver)
        time.sleep(2)
        loginObj.login(username,password)

        # 获取实际结果
        data = loginObj.getErrorResult()

        #  断言
        self.assertEqual(data,expect)






















