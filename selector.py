import unittest
import helper
import time
import HtmlTestRunner


class Selectors(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("test starting")
        cls.driver = helper.init_driver()
        time.sleep(4)

    def test_find_elements_by_accessibility_id(self):
        accessibility = self.driver.find_elements_by_accessibility_id('Content')
        self.assertTrue(1 == len(accessibility), len(accessibility))

    def test_find_elements_by_id(self):
        # android:id/iv_top_message_center 不能找到elements
        element_id = self.driver.find_elements_by_id('iv_top_message_center')
        self.assertTrue(1 == len(element_id), len(element_id))

    def test_find_elements_by_class_name(self):
        class_name = self.driver.find_elements_by_class_name('android.widget.ImageView')
        class_name[0].click()
        self.assertTrue(3 == len(class_name), len(class_name))

    def test_find_elements_by_xpath(self):
        xpath = self.driver.find_elements_by_xpath('//*[@class="android.widget.ImageView"]')
        self.assertTrue(len(xpath) == 2, len(xpath))

    @classmethod
    def tearDownClass(cls):
        print("test end")
        cls.driver.quit()


if __name__ == '__main__':

    html_folder = helper.init_html_folder()
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output=html_folder, report_title='Test_Selector'))