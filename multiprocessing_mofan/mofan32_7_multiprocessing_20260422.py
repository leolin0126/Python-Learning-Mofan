# 锁 Lock（与共享内存Shared memories搭配使用,使用方法与threading的类似）

import multiprocessing as mp
import time

def job(v,num,l):
    l.acquire()
    for _ in range(10):
        time.sleep(0.1)
        v.value += num  # 简便写法，等同于：v.value = v.value + num
        print(v.value)
    l.release()

def multicore():
    l =mp.Lock()
    v = mp.Value('i',0)
    p1 = mp.Process(target=job,args=(v,1,l))  # 小写l表示将代表锁的变量l传到进程中
    p2 = mp.Process(target=job,args=(v,3,l))  # 小写l表示将代表锁的变量l传到进程中
    p1.start()
    p2.start()
    p1.join()
    p2.join()

if __name__ == '__main__' :
    multicore()

# 弹幕与评论：
# 可以给共享同一块内存的各进程加锁，但是其他不冲突的进程就不需要加错，首先保障数据安全，其次保证并行执行。
# 在涉及到共享内存的时候 为了避免数据发生错误 加锁保持单线程是最好的办法
