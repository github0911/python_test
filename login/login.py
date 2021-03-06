import sys
sys.path.append("..")

import helper
import unittest
import HtmlTestRunner
from selenium.common.exceptions import NoSuchElementException
import HTMLTestReportCN
from HTMLTestRunner_PY3 import HTMLTestRunner

user_name = "test5"
password = "Abc1234567"


class Login(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = helper.init_driver()
        cls.driver.implicitly_wait(5)

    def check(self):
        # https://discuss.appium.io/t/permission-to-start-activity-denied-while-launching-the-app/4874
        # self.driver.start_activity("com.jingxuansugou.app", ".business.login.activity.LoginActivity")
        print("check")
        pass

    def jump_to_login(self):
        el = self.driver.find_elements_by_id("tv_home_bottom_menu")
        print(len(el))
        self.assertIsNotNone(el[3])
        el[3].click()

    def test_login(self):
        self.jump_to_login()
        try:
            print(self.driver.current_activity)
            et_account = self.driver.find_element_by_id("et_account")
            et_account.send_keys(user_name)
            et_password = self.driver.find_element_by_id("et_password")
            et_password.send_keys(password)

            v_login = self.driver.find_element_by_id("v_login")
            v_login.click()
        except NoSuchElementException as ex:
            print("Element not found and test failed", ex.msg)
            self.click_user_home()

    def click_user_home(self):
        el = self.driver.find_elements_by_id("tv_home_bottom_menu")
        print(len(el))
        self.assertIsNotNone(el[-5])
        el[-5].click()

    def click_user_center(self):
        el = self.driver.find_elements_by_id("tv_home_bottom_menu")
        print(len(el))
        self.assertIsNotNone(el[4])
        el[4].click()

    def click_setting(self):
        try:
            iv_set = self.driver.find_element_by_id("iv_set")
            iv_set.click()
            self.scroll(0, 200)
        except NoSuchElementException as ex:
            print("Element not found and test failed", ex.msg)

    def test_logout(self):
        self.click_user_center()
        self.click_setting()
        try:
            tv_logout = self.driver.find_element_by_id("tv_logout")
            tv_logout.click()
        except NoSuchElementException as ex:
            print("Element not found and test failed", ex.msg)

    def scroll(self, x_offset, y_offset):
        print("scroll_up")
        # https://www.cnblogs.com/yoyoketang/p/7766878.html
        self.driver.swipe(0, 0, x_offset, y_offset)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def get_class_name(self):
        return self.__class__.__name__


def suite():
    suite = unittest.TestSuite()
    suite.addTest(Login("test_login"))
    suite.addTest(Login("test_logout"))
    return suite


if __name__ == '__main__':

    # 简单的测试报告
    # html_path = helper.init_html_folder()
    # print(html_path)
    # helper.say_hello()
    # html_name = helper.get_html_name(Login().get_class_name())
    # print(Login().get_class_name())
    # print(html_name)
    #
    # unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output=html_path, report_title='Test Title'))

    # 美化后的测试报告
    report_title = '测试报告'
    desc = '用于展示修改样式后的HTMLTestRunner'
    report_file = helper.get_html_name("selector")
    fp = open(report_file, 'wb')

    # 带有饼图的测试报告
    runner = HTMLTestRunner(
        stream=fp,
        title=report_title,
        description=desc
    )
    runner.run(suite())