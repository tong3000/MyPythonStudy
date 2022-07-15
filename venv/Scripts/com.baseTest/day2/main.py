import logging
from time import sleep,ctime
import _thread

logging.basicConfig(level=logging.INFO)

def loop0():
    logging.info("start loop0 at " + ctime())
    sleep(4)
    logging.info("end loop0 at " + ctime())

def loop1():
    logging.info("start loop1 at " + ctime())
    sleep(2)
    logging.info("end loop1 at " + ctime())

def main():
    logging.info("start all at " + ctime())
    #子线程
    _thread.start_new_thread(loop0,())
    _thread.start_new_thread(loop1, ())
    # 规定：主线程退出时，子线程会直接结束
    # 因此需要在主线程停留几秒以观察效果
    sleep(6)
    logging.info("end all at " + ctime())
    #为了解决这个问题，引入了锁的概念


if __name__ =='__main__':
    #主线程
    main()