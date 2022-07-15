"""
线程---锁
threading里自带锁
"""

import logging
import threading
from  time import sleep,ctime
import _thread

#将根记录器级别设置为INFO级别，低于INFO的不显示
#级别排序：CRITICAL > ERROR > WARNING > INFO > DEBUG
logging.basicConfig(level=logging.INFO)

# 停留时间秒数放到一个数组中
loops = [2,4]
#定义一个方法：主要功能为sleep
def loop(nloop,nsec):
    #打印日志开始时间
    logging.info("start loop " + str(nloop) + " at " + ctime())
    #强制等待
    sleep(nsec)
    #打印日志结束时间
    logging.info("end loop " + str(nloop) + " at " + ctime())

#main方法
def main():
    #打印日志：开始时间
    logging.info("start all at " + ctime())
    threads = []
    #定义一个循环的数组：范围为[0,2）
    nloops = range(len(loops))
    #做循环
    for i in nloops:
        #调用loop方法，开启子线程：
        t = threading.Thread(target=loop,args = (i,loops[i]))
        threads.append(t)

    for i in nloops:
        threads[i].start()

    for i in nloops:
        threads[i].join()
    logging.info("end all at " + ctime())

#主线程，调用main方法
if __name__ =='__main__':
    #主线程
    main()