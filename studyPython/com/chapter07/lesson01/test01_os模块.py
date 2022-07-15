#!user/bin/env python
# -*- coding: utf-8 -*-

import os
os.mkdir("testdir")
print(os.listdir("../"))
os.removedirs("testdir")
print(os.getcwd())
print(os.path.exists("b"))
if not os.path.exists("b"):
    os.mkdir("b")
if not os.path.exists("b/test.txt"):
    f = open("b/text.txt", "w")
    f.write("hello,os using")
    f.close()