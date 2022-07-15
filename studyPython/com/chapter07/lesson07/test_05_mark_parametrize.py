import pytest


# 参数化，前两个变量，后面是对应的数据；
#  3+5->test_input    8->expected
@pytest.mark.parametrize("test_input,expected", [("3+5", 8), ("2+5", 7), ("7*5", 30)])
def test_eval(test_input, expected):
    # eval 将字符串str当成有效的表达式来求值，并返回结果
    assert eval(test_input) == expected


# 参数组合，各种组合场景数据都跑一次
@pytest.mark.parametrize("x", [1, 2])
@pytest.mark.parametrize("y", [8, 10, 11])
def test_foo(x, y):
    print(f"测试数据组合x：{x}，y：{y}")



#方法名作为参数
test_user_data = ['Tom','Jerry']
@pytest.fixture(scope="module")
def login_r(request):
    # 这是接收兵传入的参数
    user = request.param
    print(f"\n打开首页准备登录，登录用户{user}")
    return user

#indirect = True，可以把传过来的参数当函数来运行
@pytest.mark.parametrize("login_r",test_user_data,indirect=True)
def test_login(login_r):
    a=login_r
    print(f"测试用例中login的返回值：{a}")
    assert a!=""
