# -*- coding:utf-8 -*-

"""
python 语言技术与框架
"""

#导入os模块(操作系统)
import os

#创建文件夹(不写路径在当前python文件的平级建立)
os.mkdir("testdir")
#展示当前python文件所在目录下的文件与文件夹
print(os.listdir("./"))
#删除当前python文件所在目录下的指定文件夹
os.removedirs("testdir")
#打印当前完整的绝对全路径
print(os.getcwd())
#判断当前文件夹下是否存在文件夹/文件
print(os.path.exists("b"))
#如果文件夹不存在，就创建
if not os.path.exists("b"):
    os.mkdir("b")
#如果文件夹和文件下的目录不存在，就创建文件，并写入数据
if not os.path.exists("b/b.txt"):
    f=open("b/b.txt","w")
    f.write("李易峰")
    f.close()
#open()总结
"""
    --------- ---------------------------------------------------------------
    'r'       open for reading (default)
    'w'       open for writing, truncating the file first
    'x'       create a new file and open it for writing
    'a'       open for writing, appending to the end of the file if it exists
    'b'       binary mode
    't'       text mode (default)
    '+'       open a disk file for updating (reading and writing)
    'U'       universal newline mode (deprecated)
    ========= ===============================================================
"""
