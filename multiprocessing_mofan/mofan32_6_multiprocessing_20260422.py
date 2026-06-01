# 共享内存 Shared Memories
import multiprocessing as mp

value = mp.Value('d',1)
array = mp.Array('i',[1,2,3,4]) # Array只是一个一维的列表，与numpy中的Array不同










