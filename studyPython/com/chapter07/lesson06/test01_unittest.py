# 被测代码块
import unittest


def demo_method(a, b, x):
    if (a > 1) and (b == 0):
        x = x / a
    if (a == 2) or (x > 1):
        x = x + 1
    return x


if __name__ == '__main__':
    x = demo_method(3, 0, 3)
    print(x)


class TestClass(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("这是测试整个类前要执行的方法setUpClass")

    def setUp(self):
        print("这是每个测试方法前面运行的方法")

    def tearDownClass(cls):
        print("这是每个测试方法后面运行的方法")

    def test_first(self):
        print("这是测试方法1")

    @unittest.skip("这次不想执行这个测试")
    def test_second(self):
        print("这是测试方法2")

    @classmethod
    def tearDownClass(self):
        print("这是测试整个类后要执行的方法")
