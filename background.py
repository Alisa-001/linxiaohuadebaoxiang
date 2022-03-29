import time

from appium.webdriver import webdriver

desire_cap = {
  "platformName": "Android",
  "deviceName": "127.0.0.1:7555",
  "platformVersion": "6.0.1",
  "appPackage": "me.hongdou.reader",
  "appActivity": "com.now.reader.activity.SplashActivity",
  "automationName": "UiAutomator2",
  "noReSet": True,
}
#获取driver
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desire_cap)
print("准备进入后台")
# 进入后台5秒再回前台
driver.background_app(5)
time.sleep(5)
driver.quit()
