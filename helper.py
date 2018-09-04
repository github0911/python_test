import os
import time
from appium import webdriver


# 确定路径是否存在，不存在新建路径
def ensure_dir(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)


# 获取截屏
def take_screenshot(driver):
    print("take_screenshot start")
    img_folder = os.path.abspath(os.path.join(os.path.dirname(__file__))) + '\\screenshots\\'
    ensure_dir(img_folder)
    screen_time = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
    screen_save_path = img_folder + screen_time + '.png'
    print(screen_save_path)
    driver.get_screenshot_as_file(screen_save_path)
    print("take_screenshot end")


def say_hello():
    print("say hello")


# 初始化webdriver
def init_driver():

    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    # 红米note 5.1.1 三星galaxy s6 7.0
    desired_caps['platformVersion'] = '5.1.1'
    # 红米note eaad2f74 三星galaxy s6 1015fa656dcf1605
    desired_caps['deviceName'] = 'eaad2f74'
    desired_caps['noReset'] = 'True'
    # desired_caps['udid'] = 'eaad2f74'
    desired_caps['appPackage'] = 'com.jingxuansugou.app'
    desired_caps['appActivity'] = 'com.jingxuansugou.app.business.guide.StartActivity'
    return webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)


def find_element_by_id(driver, find_id):
    return driver.find_element_by_id(find_id)


# 初始化报告保存文件夹
def init_html_folder():
    html_path = os.path.abspath(os.path.join(os.path.dirname(__file__))) + '\\html\\'
    ensure_dir(html_path)
    return html_path


# 获取保存日志文件名称
def get_log_name():
    log_folder = os.path.abspath(os.path.join(os.path.dirname(__file__))) + '\\log\\'
    ensure_dir(log_folder)
    log_time = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
    return log_folder + log_time + '.txt'