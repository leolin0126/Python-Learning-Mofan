# 效率对比
import multiprocessing as mp
import threading as td
import time

def normal():  # 既不使用多线程threading，也不使用多进程Multiprocessing
    res = 0
    for _ in range(2):  # 运行2次
        for i in range(10000000):
            res = res + i + i**2 + i**3
    return res

def job(q):  # 使用多进程Multiprocessing（多核运算multicore）
    res = 0
    for i in range(10000000):
        res = res + i + i**2 + i**3
    q.put(res)    

def multiprocessing():
    q = mp.Queue()
    p1 = mp.Process(target=job,args=(q,))
    p2 = mp.Process(target=job,args=(q,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    res1 = q.get()
    res2 = q.get()
    print('multiprocessing: ',res1+res2)

def multithread():  # 使用多线程threading
    q = mp.Queue()
    t1 = td.Thread(target=job,args=(q,))
    t2 = td.Thread(target=job,args=(q,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    res3 = q.get()
    res4 = q.get()
    print('multithread: ',res3+res4)

if __name__ =='__main__':
    print('normal: ',normal())  
    st = time.time()
    normal()
    st1 = time.time()
    print('normal time: ',st1-st)
    print("-"*20)
    multithread()
    st2 = time.time()
    print('multithread time: ',st2-st)
    print("-"*20)
    multiprocessing()
    print('multiprocessing time: ',time.time()-st2)

# 弹幕与评论：
# IO密集型、计算密集型这两种程序，得采用不同的策略
# 取决于你的任务到底是cpu密集还是IO密集。io密集是cpu已经闲下来等硬盘内存了，这时候多核优化可以快很多。
# python因为GIL的存在，仅在io密集场景中有较为客观的效果，
# 计算密集场景下要么考虑numpy，要么考虑换个语言编写底层逻辑，要么就用features或者多进程的方式来绕开GIL实现。
# 调大数据集，multithread或multiprocessing的优势就明显了


