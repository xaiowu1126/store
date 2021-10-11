from selenium import  webdriver

import  time
# 打开谷歌浏览器
driver = webdriver.Chrome()
# 进入京东网站,并实现窗口最大化
driver.get(r"https://www.jd.com/")
driver.maximize_window()
#定位
driver.find_element_by_id("key").send_keys("苹果13")
driver.find_element_by_xpath("//*[@class='button']").click()

time.sleep(3)
# 下移滚动条
js = "window.scrollTo(0,600)"
driver.execute_script(js)
driver.find_element_by_xpath("//*[@id='J_goodsList']/ul/li[1]/div/div[1]/a/img").click()
#切换窗口
data = driver.window_handles
driver.switch_to_window(data[1])
#添加购物车
driver.find_element_by_id("InitCartUrl").click()
#用户登录
driver.find_element_by_xpath("//*[@id='content']/div[2]/div[1]/div/div[3]/a").click()
driver.find_element_by_id("loginname").send_keys("18838900230")
driver.find_element_by_id("nloginpwd").send_keys("hui18838900230")
driver.find_element_by_id("loginsubmit").click()

