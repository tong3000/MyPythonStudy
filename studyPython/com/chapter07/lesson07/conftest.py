import pytest


# 不带参数的fixture默认参数为scop = function
@pytest.fixture()
def login():
    print("这是个登录方法")


# 加用例自定义标签清单，防止出现警告信息
def pytest_configure(config):
    marker_list = ["search", "login"]  # 标签名集合
    for markers in marker_list:
        config.addinivalue_line("markers", markers)
