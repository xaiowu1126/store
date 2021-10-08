from selenium import webdriver
import  time
driver = webdriver.Chrome()

# 弹框验证

# 打开一个网站
driver.get(r"D:/python自动化测试资料/python/python自动化测试/day01/资料/弹框的验证/dialogs.html")
# 窗口最大化操作
driver.maximize_window()

# # 定位到alert 并点击
# driver.find_element_by_id("alert").click()
# #切换至弹框里，并点击确定
# driver.switch_to.alert.accept()

# 定位到confirm 并点击
driver.find_element_by_id("confirm").click()
#切换至弹框里，并点击确定或取消
driver.switch_to.alert.accept()
time.sleep(3)

driver.find_element_by_id("confirm").click()
driver.switch_to.alert.dismiss()



# 文件上传和表单提交

# driver.get(r"D:/python自动化测试资料/python/python自动化测试/day01/资料/上传文件和下拉列表/autotest.html")
# driver.maximize_window()

# # 定位
# driver.find_element_by_id("accountID").send_keys("小吴")
# driver.find_element_by_id("passwordID").send_keys("123456")
# driver.find_element_by_id("areaID").send_keys("北京市")
# driver.find_element_by_id("sexID1").click()
# driver.find_element_by_xpath("//*[@value='Auterm']").click()
# driver.find_element_by_xpath("//*[@name='file' and @type='file']").send_keys(r"C:\Users\86188\Pictures\Saved Pictures\鬼刀之刃.jpg")
#
# driver.find_element_by_id("buttonID").click()
# # 切换至弹框并点击确定
# driver.switch_to.alert.accept()
#
# # 关闭浏览器
# driver.quit()





# # 跳转页面
# driver.get(r"file:///D:/python%E8%87%AA%E5%8A%A8%E5%8C%96%E6%B5%8B%E8%AF%95%E8%B5%84%E6%96%99/python/python%E8%87%AA%E5%8A%A8%E5%8C%96%E6%B5%8B%E8%AF%95/day01/%E8%B5%84%E6%96%99/%E8%B7%B3%E8%BD%AC%E9%A1%B5%E9%9D%A2/pop.html")
# driver.maximize_window()
# # 定位
# driver.find_element_by_id("goo").click()



