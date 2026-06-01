# 多线程 Threading
# 添加线程
import threading  # 载入threading模块

def thread_job():  # 为添加的线程thread配置工作，工作是Python的一个具体功能
    print('This is an added Thread, number is %s' % threading.current_thread())  # 输出所添加的线程的名字

def main():  # 定义主功能
    added_thread = threading.Thread(target=thread_job)  # 添加了一个线程，以及为这个线程指定具体做的工作
    added_thread.start()  # 添加后的线程要运行时添加start命令

    # print(threading.active_count( ))  # 计算有多少个已激活的线程
    # print(threading.enumerate())  # 显示当前已激活的线程的状态
    # print(threading.current_thread())   # 显示当前正在运行哪个线程

if __name__=='__main__':
    main()












