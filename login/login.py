import sys
sys.path.append("..")

import helper
import unittest
import HtmlTestRunner
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.touch_actions import TouchActions


class Login(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = helper.init_driver()
        cls.driver.implicitly_wait(5)

    def check(self):

        # https://discuss.appium.io/t/permission-to-start-activity-denied-while-launching-the-app/4874
        # self.driver.start_activity("com.jingxuansugou.app", ".business.login.activity.LoginActivity")

        print("check")

    def jump_to_login(self):
        el = self.driver.find_elements_by_id("tv_home_bottom_menu")
        print(len(el))
        self.assertIsNotNone(el[3])
        el[3].click()

    def test_login(self):
        self.jump_to_login()
        try:
            et_account = self.driver.find_element_by_id("et_account")
            et_account.send_keys("test5")
            et_password = self.driver.find_element_by_id("et_password")
            et_password.send_keys("Abc1234567")

            v_login = self.driver.find_element_by_id("v_login")
            v_login.click()
        except NoSuchElementException as ex:
            print("Element not found and test failed", ex.msg)
        finally:
            self.click_user_center()
            self.click_setting()

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
            self.click_logout()
        except NoSuchElementException as ex:
            print("Element not found and test failed", ex.msg)

    def click_logout(self):
        try:
            tv_logout = self.driver.find_element_by_id("tv_logout")
            tv_logout.click()
        except NoSuchElementException as ex:
            print("Element not found and test failed", ex.msg)

    def scroll(self, x_offset, y_offset):
        print("scroll_up")
        self.driver.swipe(0, 0, x_offset, y_offset)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def get_class_name(self):
        return self.__class__.__name__


if __name__ == '__main__':

    html_path = helper.init_html_folder()
    print(html_path)
    helper.say_hello()
    html_name = helper.get_html_name(Login().get_class_name())
    print(Login().get_class_name())
    print(html_name)

    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output=html_path, report_title='Test Title'))