from selenium import  webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
driver = webdriver.Chrome()
driver.get("http://localhost:8080/HKR/")
driver.maximize_window()

# 用户模块
driver.find_element_by_id("loginname").send_keys("xiaoshuai")
driver.find_element_by_id("password").send_keys("123456")
driver.find_element_by_id("submit").click()
# # --修改头像、上传头像
# driver.find_element_by_id("img").click()
# time.sleep(3)
# driver.find_element_by_xpath("//*[@id='ul_pic']/li[3]/img").click()
#
# time.sleep(6)
# driver.find_element_by_xpath("//*[@id='file1']").send_keys(r"D:\1.jpg")
# driver.find_element_by_id("pic_btn").click()

# 提交今日评价
# driver.find_element_by_xpath("//*[@id='form_table']/tbody/tr[2]/td[2]/select").send_keys("9(上晚自习)")
# driver.find_element_by_xpath("//*[@id='tea_td']/select").send_keys("贾生")
# driver.find_element_by_id("textarea").send_keys("窗帘坏了，刺眼睛啊！！")

#修改个人信息
# driver.find_element_by_xpath("//*[@id='_easyui_tree_8']/span[4]/a").click()
#方法一
# ac = ActionChains(driver) # 创建时间链
# age = driver.find_element_by_xpath("//*[@id='_easyui_textbox_input1']")
# ac.double_click(age).send_keys("20").perform()  # 对年龄所在输入框双击后，并赋值18
# ac.release()
# driver.find_element_by_id("btn_modify").click()
#方法二
# driver.find_element_by_id("_easyui_textbox_input1").clear()
# driver.find_element_by_id("_easyui_textbox_input1").send_keys("18")
# driver.find_element_by_id("btn_modify").click()

#查询所有好友
driver.find_element_by_xpath("//*[@id='_easyui_tree_10']/span[4]/a").click()

# 退出
driver.find_element_by_xpath("//*[@id='top']/div/a[2]/img").click()