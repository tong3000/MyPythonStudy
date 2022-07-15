import _thread
import logging
from time import sleep,ctime
logging.basicConfig(level=logging.INFO)


"""
多线程》》》_thread演示:

"""

def loop0():
    logging.info("start loop0 at "+ctime())
    sleep(4)
    logging.info("end loop0 at " + ctime())

def loop1():
    logging.info("start loop1 at " + ctime())
    sleep(2)
    logging.info("end loop1 at " + ctime())

def main():
    logging.info("start all at " + ctime())
    #调用loop0，loop1时使用子线程
    _thread.start_new_thread(loop0,())
    _thread.start_new_thread(loop1, ())
    #这里需要加6s是因为，主线程结束的时候，所有的子线程都会被杀掉
    #这是_thread的缺点，没有守护主线程的概念
    #直接用sleep是不明智的，如果不知道loop0和loop1要执行多久，name这个sleep就会无法使用，所以这里引入了锁的概念
    sleep(6)
    logging.info("end all at " + ctime())

if __name__ == '__main__':
    main()
