import _thread
import logging
from time import sleep,ctime
logging.basicConfig(level=logging.INFO)


"""
多线程》》》_thread演示，引入锁:

"""
loops=[2,4]
def loop(nloop,nsec,lock):
    logging.info("start loop"+str(nloop)+" at "+ctime())
    sleep(nsec)
    logging.info("end loop"+str(nloop)+" at "+ ctime())
    lock.release()

def main():
    logging.info("start all at " + ctime())
    locks = []
    #第几个线程
    nloops=range(len(loops))
    for i in nloops:
        lock = _thread.allocate_lock()
        #加锁
        lock.acquire()
        locks.append(lock)
    #为什么下面的循环不放到上面的循环中一起执行？
    #因为获取锁的操作时需要时间的，很有可能会出现正在获取锁的时候，开启了一个新的子线程，当获取第二个锁的时候，线程1已经执行完毕了，然后它就完成第三个循环解锁的操作，所有的主线程就退出了
    for i in nloops:
        _thread.start_new_thread(loop,(i,loops[i],locks[i]))
    for i in nloops:
        while locks[i].locked():pass
    logging.info("end all at " + ctime())

if __name__ == '__main__':
    main()
