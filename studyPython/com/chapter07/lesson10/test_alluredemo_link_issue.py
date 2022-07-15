#!user/bin/env python
# -*- coding: utf-8 -*-
import allure


@allure.link("http://www.baidu.com", name="链接")
def test_with_link():
    print("这是一条加了链接的测试")
    pass

#测试用例链接到管理测试用例的网站上
TEST_CASE_LINK='https://leetcode-cn.com/problemset/all/?utm_source=LCUS&utm_medium=new_banner_click&utm_campaign=transfer2china&utm_content=title_main'
@allure.testcase(TEST_CASE_LINK, '登录用例')
def test_with_link():
    print("这是一条加了链接的测试，链接到测试用例管理页面")
    pass

#bug地址
@allure.issue('140', '这是一个issue')
def test_with_link():
    print("这是一条加了链接的测试，链接到测试用例管理页面")
    pass
