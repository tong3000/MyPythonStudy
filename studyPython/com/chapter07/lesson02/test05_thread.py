import _thread
import logging
import threading
from time import sleep,ctime
logging.basicConfig(level=logging.INFO)


"""
多线程》》》
新建class类继承Thread类
主动调init方法
重写run函数，进行重写之后实现多线程操作
--建议此方式
"""
loops=[2,4]

class MyThread(threading.Thread):
    def __init__(self,func,args,name=''):
        threading.Thread.__init__(self)
        self.func = func
        self.args = args
        self.name = name

    def run(self):
        self.func(*self.args)

def loop(nloop,nsec):
    logging.info("start loop"+str(nloop)+" at "+ctime())
    sleep(nsec)
    logging.info("end loop"+str(nloop)+" at "+ ctime())

def main():
    logging.info("start all at " + ctime())
    threads = []
    #第几个线程
    nloops=range(len(loops))
    for i in nloops:
        t = MyThread(loop,(i,loops[i]),loop.__name__)
        threads.append(t)
    for i in nloops:
        threads[i].start()
    for i in nloops:
        threads[i].join()
    logging.info("end all at " + ctime())

if __name__ == '__main__':
    main()

# 多线程进阶
# 原语
## 锁
## 信号量