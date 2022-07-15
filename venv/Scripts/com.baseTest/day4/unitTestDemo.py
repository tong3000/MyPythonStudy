"""
Unittest：单元测试框架
单元测试：是开发者编写的一小段代码，用于检测被测代码的一个很小的、很明确的功能是否正确。
通常而言，一个单元测试是用于判断某个特定条件（或者场景）下某个特定函数的行为。

python单元测试框架：
1、Unittest
2、Pytest  可与allure组合生成测试报告，主流
3、Nose：Unittest的扩展
4、Mock：unittest.mock可以用来测试python的库

单元覆盖类型：
    语句覆盖
    条件覆盖
    判断覆盖
    路径覆盖

相关组件
    test case
    test suites
    test fixtures
    test runnner
"""
import unittest
class demo(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        print("setUpClass")

    @classmethod
    def tearDownClass(cls) -> None:
        print("tearDownClass")

    def setUp(self) -> None:
        print("setup")

    def tearDown(self) -> None:
        print("teardown")

    def test_case01(self):
        print("test01")
        self.assertEqual(1,1,"判断相等")
        #self.assertIn('h', 'this')
        #self.assertNotIn('h','this')

    def test_case02(self):
        print("test02")
        self.assertEqual(1,1,"判断相等")
        #self.assertIn('h', 'this')
        #self.assertNotIn('h','this')


    @unittest.skip#跳过test03  skip 、skipIf
    def test_case03(self):
        print("test03")
        self.assertEqual(1,1,"判断相等")
        #self.assertIn('h', 'this')
        #self.assertNotIn('h','this')

    def test_case04(self):
        print("test04")
        self.assertEqual(1,1,"判断相等")
        #self.assertIn('h', 'this')
        #self.assertNotIn('h','this')

class demo1(unittest.TestCase):
    def test_demo1_case0(self):
        print("test_demo1_case0")

    def test_demo1_case1(self):
        print("test_demo1_case1")

class demo2(unittest.TestCase):
    def test_demo2_case0(self):
        print("test_demo2_case0")

    def test_demo2_case1(self):
        print("test_demo2_case1")

if __name__=='__main__':
    # #当前py文件中所有的test_开头的用例都执行
    # unittest.main()
    # print("---------------------------------------")
    # #如果只想执行某些用例，需要用到测试套件
    # suit = unittest.TestSuite()
    # suit.addTest(demo("test_case01"))
    # suit.addTest(demo1("test_demo1_case1"))
    # unittest.TextTestRunner().run(suit)
    # print("---------------------------------------")
    # suite1 = unittest.TestLoader().loadTestsFromTestCase(demo)
    # suite2 = unittest.TestLoader().loadTestsFromTestCase(demo1)
    # suiteall = unittest.TestSuite([suite1,suite2])
    # unittest.TextTestRunner().run(suiteall)
    # print("---------------------------------------")
    #匹配某个目录下所有以test开头的py文件，执行这些文件下的所有测试用例
    discover = unittest.defaultTestLoader.discover("./",'unitTest*.py')
    unittest.TextTestRunner().run(discover)

    """
    步骤
    1、首先是要写好TestCase
    2、然后友TestLoader加载TestCase到TestSuite
    3、然后由TextTestRunner来运行TestSuite
    4、运行的记过保存在TextTestResult中
    5、整个过程继承在unittest.main模块中
    6、TestCase可以是多个，TestSuit也可以是多个
    """