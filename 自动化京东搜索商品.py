from selenium import  webdriver
# 打开谷歌浏览器
driver = webdriver.Chrome()
# 进入京东网站,并实现窗口最大化
driver.get(r"https://www.jd.com/")
driver.maximize_window()
#定位
driver.find_element_by_id("key").send_keys("苹果13")
driver.find_element_by_xpath("//*[@class='button']").click()