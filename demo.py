# 导入unittest 单元测试库
import unittest


# 用例继承unittest.TestCase
class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        print("test_upper")
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        print("test_isupper")
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        print("test_split")
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)


def suite():
    # 通过suite增加的方式可以进行测试的顺序排序处理
    suite = unittest.TestSuite()
    suite.addTest(TestStringMethods('test_upper'))
    suite.addTest(TestStringMethods('test_isupper'))
    suite.addTest(TestStringMethods('test_split'))
    return suite


if __name__ == '__main__':
    # 通过suite增加的方式可以进行测试的顺序排序处理
    runner = unittest.TextTestRunner()
    result = unittest.TextTestRunner(verbosity=2).run(suite())

    # 生成测试报告
    print("testsRun:%s"%result.testsRun)
    print("failures:%s"%len(result.failures))
    print("errors:%s"%len(result.errors))
    print("skipped:%s"%len(result.skipped))
    # runner = unittest.TextTestRunner()
    # runner.run(suite())
    # 这种方式执行，是安装用例方法名称的排序来执行用例
    # unittest.main()