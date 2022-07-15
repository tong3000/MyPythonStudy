import unittest


class TestClass(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print("setUpClass")

    @classmethod
    def tearDownClass(cls) -> None:
        print("tearDownClass")

    def setUp(self) -> None:
        print("setUp")

    def tearDown(self) -> None:
        print("teardown")

    def test_case01(self):
        print("testcase01")
        self.assertEqual(1, 1, "判断相等")
        self.assertIn('h', 'this')

    def test_case02(self):
        print("testcase02")
        self.assertEqual(1, 1, "判断相等")
        self.assertIn('h', 'this')

    # @unittest.skip("跳过该用例")
    @unittest.skipIf(1 + 1 == 2, "1+1等于2时，跳过该用例")
    def test_case03(self):
        print("testcase03")
        self.assertEqual(1, 1, "判断相等")
        self.assertIn('h', 'this')


class demo1(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print("setUpClass")

    @classmethod
    def tearDownClass(cls) -> None:
        print("tearDownClass")

    def setUp(self) -> None:
        print("setUp")

    def tearDown(self) -> None:
        print("teardown")

    def test_case01(self):
        print("testcase01")
        self.assertEqual(1, 1, "判断相等")
        self.assertIn('h', 'this')

    def test_case02(self):
        print("testcase02")
        self.assertEqual(1, 1, "判断相等")
        self.assertIn('h', 'this')

    def test_case03(self):
        print("testcase03")
        self.assertEqual(1, 1, "判断相等")
        self.assertIn('h', 'this')


# 入口函数：main
if __name__ == '__main__':
    #方式一：
    # unittest.main()
    #方式二：
    # suite = unittest.TestSuite()
    # suite.addTest(demo1("test_case01"))
    # suite.addTest(TestClass("test_case01"))
    #
    # unittest.TextTestRunner().run(suite)

    # 方式三：
    # suite1 = unittest.TestLoader().loadTestsFromTestCase(TestClass)
    # suite2 = unittest.TestLoader().loadTestsFromTestCase(demo1)
    # suiteall = unittest.TestSuite([suite1, suite2])
    # unittest.TextTestRunner(verbosity=2).run(suiteall)

    #方式四：
    discover = unittest.defaultTestLoader.discover("./", "test*.py")
    unittest.TextTestRunner().run(discover)