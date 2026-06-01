# 进程池 pool
import multiprocessing as mp

def job(x):
    return x*x  # pool中有返回值

def multicore():
    pool = mp.Pool()  # 把池子对应上所需的功能，往池子中丢数据
#   pool = mp.Pool(processes=3)  # 只用3核跑程序，默认状态是全部的核
    res = pool.map(job,range(10))  # 把方程和值用map功能绑定到一起
    print(res)
    res = pool.apply_async(job,(2,))  # 只能给job一个值，程序只会把它放入一个核运行一次
    print(res.get())  # 从池子pool中拿出这个值并输出结果
    # 为async赋予可迭代的多个值  
    multi_res=[pool.apply_async(job,(i,))for i in range(10)]
    print([res.get()for res in multi_res])

if __name__=='__main__':
    multicore()





