import unittest
import HtmlTestRunner
import sys, os, time
from appium import webdriver
import helper

# from helper import ensure_dir
# from helper import take_screenshot_and_logcat

# https://bop.mol.uno/
# https://github.com/appium/appium/tree/master/sample-code/python/test
###############################
# unittest 方法执行顺序
# 1、按照方法名称来执行
# 2、通过添加测试
# suite = unittest.TestSuite()
# suite.addTest(Start("test_a_find"))
# suite.addTest(Start("test_find_element"))
# suite.addTest(Start("test_click_user_info"))
class Start(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # desired_caps = {}
        # desired_caps['platformName'] = 'Android'
        # # 红米note 5.1.1 三星galaxy s6 7.0
        # desired_caps['platformVersion'] = '5.1.1'
        # # 红米note eaad2f74 三星galaxy s6 1015fa656dcf1605
        # desired_caps['deviceName'] = 'eaad2f74'
        # desired_caps['noReset'] = 'True'
        # # desired_caps['udid'] = 'eaad2f74'
        # desired_caps['appPackage'] = 'com.jingxuansugou.app'
        # desired_caps['appActivity'] = 'com.jingxuansugou.app.business.guide.StartActivity'
        # cls.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        cls.driver = helper.init_driver()

        time.sleep(2)

    def test_a_find(self):
        # activity = self.driver.current_activity
        # pkg = self.driver.current_package

        # self.assertEquals('com.jingxuansugou.app.business.guide.StartActivity',
        #                   '{}{}'.format(pkg, activity))
        # helper.take_screenshot(self.driver)
        el = helper.find_element_by_id(self.driver, "tv_jump")
        self.assertIsNotNone(el)
        el.click()
        # self.test_failed()

    @unittest.skip
    def test_find_element(self):
        # driver.find_element_by_name('跳过').click()
        el = self.driver.find_element_by_name("个人中心")
        self.assertTrue(el.__sizeof__() != 2, "未找到个人中心")

        self.assertEqual(el.__sizeof__(), 2)
        """el.size  """ + el.__sizeof__()
        self.assertIsNotNone(el, "未找到个人中心")
        el.click()

    def test_home_share(self):
        helper.take_screenshot(self.driver)

        el = self.driver.find_element_by_id("iv_home_top_share")
        self.assertIsNotNone(el, "首页分享按钮存在")
        el.click()

        el = self.driver.find_element_by_id("tv_dialog_title")
        self.assertIsNotNone(el)

        # 返回操作
        self.driver.back()
        # el = self.driver.find_elements_by_id("share_dialog_name_tv")
        # self.assertIsNone(el, "微信按钮不存在")
        # self.assertEqual(el[0].text, "微信", "微信按钮存在")
        # el[0].click()

        el = self.driver.find_element_by_id("iv_top_message_center")
        self.assertIsNotNone(el)
        el.click()

    @unittest.skip
    def test_click_user_info(self):

        time.sleep(2)
        el = self.driver.find_elements_by_id("tv_home_bottom_menu")
        self.assertIsNotNone(el[4])

        el[4].click()
        self.assertEqual(el[4].text, "个人中心")

        el[0].click()

    @unittest.skip
    def test_success(self):
        time.sleep(3)
        self.assertEqual(1, 1)

    @unittest.skip
    def test_failed(self):
        time.sleep(6)
        self.assertFalse('Failed'.isupper())

    @staticmethod
    def driver_quit(cls):
        cls.driver.quit()

    @classmethod
    def tearDownClass(cls):
        cls.driver_quit(cls)

if __name__ == '__main__':
    # 获取文件目录
    html_path = helper.init_html_folder()
    print(html_path)
    helper.say_hello()
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output=html_path, report_title='Test Title', descriptions='des'))

    # 生成测试报告
    tests = unittest.TestLoader().loadTestsFromTestCase(Start)
    # 使用测试套件并打包测试用例（addTests()等价于addTest()）
    suite = unittest.TestSuite()
    suite.addTest(tests)
    # 保存unittest的测试输出日志
    # log_folder = os.path.abspath(os.path.join(os.path.dirname(__file__))) + '\\log\\'
    # helper.ensure_dir(log_folder)
    # log_time = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
    # log_save_name = log_folder + log_time + '.txt'

    with open(helper.get_log_name(), 'w+') as f:
        result = unittest.TextTestRunner(stream=f, verbosity=2).run(suite)
    # 若不保存测试输出结果，执行如下命令
    # result = unittest.TextTestRunner(verbosity=2).run(suite)

    # 生成测试报告
    # print("testsRun:%s"%result.testsRun)
    # print("failures:%s"%len(result.failures))
    # print("errors:%s"%len(result.errors))
    # print("skipped:%s"%len(result.skipped))
    '''
    unittest.main()
    
    # suite = unittest.TestSuite()
    # suite.addTest(Start("test_find_element"))
    # # unittest.TextTestRunner(verbosity=2).run(suite)
    # # unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='example_dir'))
    # filename = 'E:\\' + time.strftime("_%Y%m%d_%H%M%S", time.localtime(time.time())) + '.html'
    # fp = open('filename', 'wb')
    # runner = HtmlTestRunner.HTMLTestRunner(stream=fp, report_title='测试报告', descriptions='测试执行情况')
    # runner.run(suite)
    # fp.close()
    '''