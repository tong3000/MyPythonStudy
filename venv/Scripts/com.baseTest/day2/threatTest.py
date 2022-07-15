"""
线程---锁
_thread
"""

import logging
from  time import sleep,ctime
import _thread

#将根记录器级别设置为INFO级别，低于INFO的不显示
#级别排序：CRITICAL > ERROR > WARNING > INFO > DEBUG
logging.basicConfig(level=logging.INFO)

# 停留时间秒数放到一个数组中
loops = [2,4]
#定义一个方法：主要功能为sleep
def loop(nloop,nsec,lock):
    #打印日志开始时间
    logging.info("start loop " + str(nloop) + " at " + ctime())
    #强制等待
    sleep(nsec)
    #打印日志结束时间
    logging.info("end loop " + str(nloop) + " at " + ctime())
    #释放锁
    lock.release()

#main方法
def main():
    #打印日志：开始时间
    logging.info("start all at " + ctime())
    #定义一个锁：空数组
    locks =[]
    #定义一个循环的数组：范围为[0,2）
    nloops = range(len(loops))
    #这上一步的这个数组进行循环
    for i in nloops:
        #返回一个新的锁对象，锁初始处于未锁状态
        lock = _thread.allocate_lock()
        #加锁操作：阻塞调用线程，直到当前使用它的线程将锁解锁
        lock.acquire()
        #将锁加入锁的数组中
        locks.append(lock)
    #再次做循环
    for i in nloops:
        #调用loop方法，开启子线程：
        _thread.start_new_thread(loop,(i,loops[i],locks[i]))
    #第三次循环
    for i in nloops:
        #判断是否已经解锁
        while locks[i].locked(): pass
    logging.info("end all at " + ctime())

#主线程，调用main方法
if __name__ =='__main__':
    #主线程
    main()