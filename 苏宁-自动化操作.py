from selenium import  webdriver
import  time
driver = webdriver.Chrome()
driver.get("https://www.suning.com/?utm_source=baidu&utm_medium=brand&utm_campaign=title&utm_term=brand")
driver.maximize_window()
#定位
driver.find_element_by_id("searchKeywords").send_keys("苹果11")
driver.find_element_by_id("searchSubmit").click()
time.sleep(4)
driver.find_element_by_xpath("//*[@id='ssdsn_search_pro_baoguang-1-0-1_1_01:0070094634_12182753074']/img").click()

#切换选项卡
data=driver.window_handles #获取不同选项卡的唯一标识，并保存在列表中
driver.switch_to_window(data[1])

#加入购物车
driver.find_element_by_id("addCart").click()
# 购物车结算
driver.find_element_by_xpath("/html/body/div[38]/div/div[2]/div/div[1]/a").click()
