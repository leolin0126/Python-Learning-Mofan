# 多线程 Threading
# 添加线程
import threading  # 载入threading模块
import time

def thread_job():  # 为添加的线程thread配置工作，工作是Python的一个具体功能
    print('T1 start\n')  # 输出所添加的线程的名字
    for i in range(10):  # range函数为range(0,10,1)，区间为[0,10)，步长为1
        time.sleep(0.2)  # 每一步暂停0.1秒然后继续后续步骤
    print('T1 finish\n')

def T2_job():  # 添加另一个任务，此任务的完成时间比前一个任务短
    print('T2 start\n')
    print('T2 finish\n')

def main():  # 定义主功能
    added_thread = threading.Thread(target=thread_job, name='T1')  # 添加了一个线程，以及为这个线程指定具体做的工作
    thread2 = threading.Thread(target=T2_job,name='T2')
    added_thread.start()  # 添加后的线程要运行时添加start命令
    thread2.start()  # 添加后的线程要运行时添加start命令
    added_thread.join()  # 等待added_thread完成工作
    thread2.join()  # 等待thread2完成工作
    print('all done\n')  # 输出all done

    # print(threading.active_count( ))  # 计算有多少个已激活的线程
    # print(threading.enumerate())  # 显示当前已激活的线程的状态
    # print(threading.current_thread())   # 显示当前正在运行哪个线程

if __name__=='__main__':
    main()

# 输出的顺序：T1 start → T2 start → T2 finish → T1 finish → all done










