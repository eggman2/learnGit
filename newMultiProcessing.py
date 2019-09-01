import multiprocessing as mp
import threading as td
import time
from queue import Queue

# def thread_job():
#     print("t1 start")
#     time.sleep(2)
#     print('t1 end')
#
# def t2():
#     print('t2 start')
#     print('t2 end')
#
# def main():
#     added_thread = threading.Thread(target=thread_job,name = 'T1')
#     th2 = threading.Thread(target=t2,name='T2')
#
#
#     added_thread.start()
#     th2.start()
#     added_thread.join()
#     th2.join()
#
#     print('finish')
#

# def job(l,q):
#     for i in range(len(l)):
#         l[i] = l[i] **2
#     q.put(l)
#     # print(q.get())
#
# def multithreading():
#     q = Queue()
#     threads=[]
#     data=[[1,2],[3,4],[5,6],[7,8]]
#     for i in range(4):
#         t = threading.Thread(target=job,args=(data[i],q),name='t'+str(i))
#         t.start()
#         threads.append(t)
#
#     for thread in threads:
#         thread.join()
#
#     results =[]
#
#     for j in range(4):
#         results.append(q.get())
#     print(results)

# def job1():
#     global A,lock
#     for i in range(10):
#         A+=1
#         print('job1 : ',A)
#
# def job2():
#     global A,lock
#     lock.acquire()
#     for i in range(10):
#         A +=10
#         print('job2',A)
#     lock.release()
#
# if __name__ == '__main__':
#     lock=threading.Lock()
#     A =0
#     t1=threading.Thread(target=job1())
#     t2=threading.Thread(target=job2())
#     t1.start()
#     t2.start()
#
#     t1.join()
#     t2.join()

# ---------------------------------------------------------------line break
# def job(q):
#     res=0
#     for i in range(1000000):
#         res+=i+i**2+i**3
#     q.put(res)
#
# def multicore():
#     q    = mp.Queue()
#     p1 = mp.Process(target=job, args=(q,))
#     p2 = mp.Process(target=job, args=(q,))
#     p1.start()
#     p2.start()
#     p1.join()
#     p2.join()
#
#     res1 = q.get()
#     res2 = q.get()
#     print(res2+res1)
#
# def multithread():
#     q = mp.Queue()
#     t1 = td.Thread(target=job, args=(q,))
#     t2 = td.Thread(target=job, args=(q,))
#
#     t1.start()
#     t2.start()
#     t1.join()
#     t2.join()
#
#     res1 = q.get()
#     res2 = q.get()
#     print(res2 + res1)
#
# def nor():
#     res = 0
#     for j in range(2):
#         for i in range(1000000):
#             res += i + i ** 2 + i ** 3
#     print(res)
#     return res
#
#
# if __name__ == '__main__':
#     s1=time.time()
#     nor()
#     print(+ time.time()-s1)
#
#     s1 = time.time()
#     multicore()
#     print( + time.time() - s1)
#
#     s1 = time.time()
#     multithread()
#     print( + time.time() - s1)


# import multiprocessing as mp
#
# def job(q):
#     res = 0
#     for i in range(1000000):
#         res += i + i**2 + i**3
#     q.put(res) # queue
#
# def multicore():
#     q = mp.Queue()
#     p1 = mp.Process(target=job, args=(q,))
#     p2 = mp.Process(target=job, args=(q,))
#     p1.start()
#     p2.start()
#     p1.join()
#     p2.join()
#     res1 = q.get()
#     res2 = q.get()
#     print('multicore:',res1 + res2)
#
# import threading as td
#
# def multithread():
#     q = mp.Queue() # thread可放入process同样的queue中
#     t1 = td.Thread(target=job, args=(q,))
#     t2 = td.Thread(target=job, args=(q,))
#     t1.start()
#     t2.start()
#     t1.join()
#     t2.join()
#     res1 = q.get()
#     res2 = q.get()
#     print('multithread:', res1 + res2)
#
# def normal():
#     res = 0
#     for _ in range(2):
#         for i in range(1000000):
#             res += i + i ** 2 + i ** 3
#     print('normal:', res)
#
# import time
#
# if __name__ == '__main__':
#     st = time.time()
#     normal()
#     st1 = time.time()
#     print('normal time:', st1 - st)
#     multithread()
#     st2 = time.time()
#     print('multithread time:', st2 - st1)
#     multicore()
#     print('multicore time:', time.time() - st2)
#

"""join()的位置会影响多进程的效率"""


# Pool进程池

# def job(x):
#     return  x*x
#
# def mt():
#     pool=mp.Pool()
#     res = pool.map(job,(2,))
#     print(res)
#     res = pool.apply_async(job,(2,))
#     print(res.get())
#
# if __name__=='__main__':
#     mt()

# MAP中第二个参数必须是可以迭代的


def job(v, num, l):
    l.acquire()  # 锁住
    for _ in range(5):
        time.sleep(0.1)
        v.value += num  # 获取共享内存
        print(v.value)
    l.release()  # 释放


def multicore():
    l = mp.Lock()  # 定义一个进程锁
    v = mp.Value('i', 0)  # 定义共享内存
    p1 = mp.Process(target=job, args=(v, 1, l))  # 需要将lock传入
    p2 = mp.Process(target=job, args=(v, 3, l))
    p1.start()
    p2.start()
    p1.join()
    p2.join()


if __name__ == '__main__':
    multicore()
