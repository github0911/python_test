import unittest
import helper
import time
import HTMLTestReportCN
from HTMLTestRunner_PY3 import HTMLTestRunner


class Selectors(unittest.TestCase):
    __doc__ = "选择"

    @classmethod
    def setUpClass(cls):
        print("test starting")
        print(__doc__)
        cls.driver = helper.init_driver()
        time.sleep(4)

    def test_find_elements_by_accessibility_id(self):
        print("test_find_elements_by_accessibility_id")
        accessibility = self.driver.find_elements_by_accessibility_id('Content')
        self.assertTrue(1 == len(accessibility), len(accessibility))

    def test_find_elements_by_id(self):
        # android:id/iv_top_message_center 不能找到elements
        element_id = self.driver.find_elements_by_id('iv_top_message_center')
        print("test_find_elements_by_id")
        self.assertTrue(1 == len(element_id), len(element_id))

    def test_find_elements_by_class_name(self):
        print("test_find_elements_by_class_name")
        class_name = self.driver.find_elements_by_class_name('android.widget.ImageView')
        class_name[0].click()
        self.assertTrue(3 == len(class_name), len(class_name))

    def test_find_elements_by_xpath(self):
        print("test_find_elements_by_xpath")
        # https://discuss.appium.io/t/selenium-common-exceptions-nosuchelementexception-message-an-element-could-not-be-located-on-the-page-using-the-given-search-parameters/19120
        xpath = self.driver.find_elements_by_xpath('//*[@class="android.widget.ImageView"]')
        self.assertTrue(len(xpath) == 2, len(xpath))

    @classmethod
    def tearDownClass(cls):
        print("test end")
        cls.driver.quit()


def suite():
    suite = unittest.TestSuite()
    suite.addTest(Selectors("test_find_elements_by_accessibility_id"))
    suite.addTest(Selectors("test_find_elements_by_id"))
    suite.addTest(Selectors("test_find_elements_by_class_name"))
    suite.addTest(Selectors("test_find_elements_by_xpath"))
    return suite


if __name__ == '__main__':

    # html_folder = helper.init_html_folder()
    # unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output=html_folder, report_title='Test_Selector'))

    report_title = '测试报告'
    desc = '用于展示修改样式后的HTMLTestRunner'
    report_file = helper.get_html_name("selector")
    fp = open(report_file, 'wb')

    # 没有饼图的测试报告
    # runner = HTMLTestReportCN.HTMLTestRunner(
    #             stream=fp,
    #             title=report_title,
    #             description=desc
    #             )

    # 带有饼图的测试报告
    runner = HTMLTestRunner(
                stream=fp,
                title=report_title,
                description=desc
                )
    runner.run(suite())
