from selenium import  webdriver
# 打开谷歌浏览器
driver = webdriver.Chrome()
# 进入百度,并实现窗口最大化
driver.get(r"https://www.baidu.com/")
driver.maximize_window()
#定位
driver.find_element_by_id("kw").send_keys("河南人为什么这么帅！！！！")
driver.find_element_by_id("su").click()