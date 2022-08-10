from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains
import time

# def log(msg):
#     now = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
#     with open('/home/libary/log1.txt', 'a') as f:
#         f.write('{}--{}\n'.format(now, msg))
#         f.close()

if __name__ == "__main__":

    print("开始抢座位")
    msg = "---------------------抢座位开始--------------------------"
# //    log(msg)

    # 为Chrome配置无头模式
    ch_options = webdriver.ChromeOptions()
    ch_options.add_argument("--headless") # 无头模式，可不启用界面显示运行
    ch_options.add_argument('--no-sandbox') # 参数是让Chrome在root权限下跑
    ch_options.add_argument('--disable-gpu')# 禁用GPU加速
    ch_options.add_argument('--disable-dev-shm-usage')
    ch_options.add_argument('--disable-infobars')# 禁用浏览器正在被自动化程序控制的提示
    ch_options.add_argument('--window-size=1920,1080') # 设置窗口大小
    driver = webdriver.Chrome(options=ch_options)


    driver.get("http://zwyy.lib.ctgu.edu.cn/home/web/seat/area/1")
    print("进入网页")
    msg = "                     成功进入网页"
    # log(msg)


    WebDriverWait(driver, 100).until(lambda browser: browser.find_element_by_xpath('/html/body/div[8]/div/a[2]')).click()


    WebDriverWait(driver, 100).until(lambda browser: browser.find_element_by_xpath('/html/body/div[2]/div[1]/ul/li[4]/a')).click()
    print("点击登录")
    msg = "                     准备登录"
    # log(msg)


    WebDriverWait(driver, 100).until(lambda browser: browser.find_element_by_xpath('/html/body/div[2]/div/div[1]/form/div[2]/input')).send_keys("2019111408")
    print("输入学号")
    msg = "                     输入学号"
    # log(msg)

    WebDriverWait(driver, 100).until(lambda browser: browser.find_element_by_xpath('/html/body/div[2]/div/div[1]/form/div[3]/input')).send_keys("28867X")
    print("输入密码")
    msg = "                     输入密码"
    # log(msg)

    hold = WebDriverWait(driver, 100).until(lambda browser: browser.find_element_by_xpath('/html/body/div[2]/div/div[1]/form/div[4]/div/div/div'))
    action = ActionChains(driver)
    action.click_and_hold(hold).perform() # 点击不松手
    action.move_by_offset(290,0) # 向右移动290像素
    action.release().perform() # 松开
    print("过验证码")
    msg = "                     过验证码"
    # log(msg)


    WebDriverWait(driver, 100).until(lambda browser: browser.find_element_by_xpath('/html/body/div[2]/div/div[1]/form/div[6]/button')).click()
    print("点击登录")
    msg = "                     账号登录成功"
    # log(msg)


    WebDriverWait(driver, 100).until(lambda browser: browser.find_element_by_xpath('/html/body/div[8]/div/a[2]')).click()
    # 等待第二天被选中
    day2_button = WebDriverWait(driver, 100).until(lambda browser: browser.find_element_by_xpath('/html/body/div[8]/div/a[2]') and (driver.find_element_by_xpath('/html/body/div[8]/div/a[2]').get_attribute("class") == "btn btn-default active area_day"))
    print("进入第二天")
    msg = "                     进入第二天"
    # log(msg)


    action = ActionChains(driver) # 重新获取，不然action会过期，我也不知道为什么，linux会报错，windows不会
    F2 = WebDriverWait(driver, 100).until(lambda browser: browser.find_element_by_xpath('/html/body/div[6]/div[1]/div[1]/div'))
    action.move_to_element_with_offset(F2, F2.size['width']/697*250, F2.size['height']/392*290).click().perform()
    print("选中F2")
    msg = "                     选中F2"
    # log(msg)

    # 1728 973 796 242
    WebDriverWait(driver, 100).until(lambda browser: browser.find_element_by_xpath('/html/body/div[6]/div[1]/div[1]/div/a')) # 等待返回键出现
    action = ActionChains(driver)
    F2 = WebDriverWait(driver, 100).until(lambda browser: browser.find_element_by_id('floor'))
    # action.move_to_element_with_offset(F2, F2.size['width']/1544*370,F2.size['height']/867*370).click().perform()  # 选中B
    # action.move_to_element_with_offset(F2, F2.size['width']/1728*796,F2.size['height']/973*242).click().perform()  # 选中C
    action.move_to_element_with_offset(F2, F2.size['width']/1153*789,F2.size['height']/649*245).click().perform()  # 选中A
    print("选中A区")
    msg = "                     选中A区"
    # log(msg)



    # WebDriverWait(driver, 100).until(lambda browser: browser.find_element_by_xpath('/html/body/div[6]/div[1]/div[1]/div/ul/li[81]')).click() # 选座位81
    WebDriverWait(driver, 100).until(lambda browser: browser.find_element_by_xpath('/html/body/div[6]/div[1]/div[1]/div/ul/li[129]')).click() # 选座位129
    print("选座位129")
    msg = "                     选座位129"
    # log(msg)

    time.sleep(0.5)
    WebDriverWait(driver, 100).until(lambda browser: browser.find_element_by_xpath('/html/body/div[11]/div/table/tbody/tr[3]/td/div[2]/button[2]')).click()
    print("确定选座")
    msg = "                     确定选座"
    # log(msg)


    WebDriverWait(driver, 100).until(lambda browser: browser.find_element_by_xpath('/html/body/div[11]/div/table/tbody/tr[3]/td/div[2]/button')).click()
    print("选座成功")
    msg = "                     选座成功"
    # log(msg)

    driver.quit()
    print("退出页面")
    msg = "---------------------抢座位成功--------------------------"
    # log(msg)
