from selenium import  webdriver
import time
driver = webdriver.Chrome()
driver.get("http://localhost:8080/HKR/")
driver.maximize_window()

#用户注册(第一步)
driver.find_element_by_xpath("/html/body/div/div/div[1]/div[2]/a[1]").click()
driver.find_element_by_id("loginname").send_keys("xiaoshuai")
driver.find_element_by_xpath("//*[@id='msform']/fieldset[1]/input[2]").send_keys("小帅")
driver.find_element_by_id("pwd").send_keys("123456")
driver.find_element_by_xpath("//*[@id='msform']/fieldset[1]/input[4]").send_keys("123456")
driver.find_element_by_xpath("//*[@id='msform']/fieldset[1]/input[5]").click()
# 第二步
driver.find_element_by_id("valid_age").send_keys("18")
driver.find_element_by_id("classname").send_keys("Python自动化")
time.sleep(3)
driver.find_element_by_xpath("//*[@id='msform']/fieldset[2]/input[3]").click()
# 第三步
driver.find_element_by_id("reg_mail").send_keys("958402855@qq.com")
driver.find_element_by_id("reg_phone").send_keys("18838900220")
driver.find_element_by_id("btn_reg").click()
driver.find_element_by_xpath("/html/body/div[2]/div[3]/a").click()

