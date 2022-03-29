import time

from appium import webdriver
desire_cap = {
  "platformName": "Android",
  "deviceName": "127.0.0.1:7555",
  "platformVersion": "6.0.1",
  "appPackage": "com.android.settings",
  "appActivity": ".Settings",
  "automationName": "UiAutomator2",
  "noReSet": True,
  "skipDeviceInitialization":True,
}
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desire_cap)
driver.implicitly_wait(10)
# print(driver.current_package)
# print(driver.current_activity)
# time.sleep(5)
# driver.start_activity("me.hongdou.reader", "com.now.reader.activity.SplashActivity")
# print(driver.current_package)
# print(driver.current_activity)
# driver.close_app()
# driver.quit()
# print(driver.current_package)
# 判断是否安装
# if driver.is_app_installed("me.hongdou.reader"):
#   # 如果安装就卸载
#   driver.remove_app("me.hongdou.reader")
#   # 如果没有安装，就安装
# else:
#   driver.install_app(r"C:\Users\86183\Desktop\红豆336_测试2.apk")
#   time.sleep(5)
#   driver.quit()
print("准备进入后台")
driver.background_app(5)
print("5秒后回到前台")
time.sleep(5)
driver.quit()
