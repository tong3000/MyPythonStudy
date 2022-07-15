# content of test_sample.py

"""
运行test_sample
终端：进入当前目录，并执行文件
cd D:\Environment\MyPythonStudy\venv\Scripts\com.baseTest\day5_pytest
pytest test_sample.py
"""
def func(x):
    return x + 1

def test_answer():
    assert func(3) == 5