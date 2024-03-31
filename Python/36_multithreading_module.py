
# Multithreading in Python allows you to execute multiple threads concurrently within a single process. 
# Each thread represents an independent flow of execution, enabling your program to perform multiple 
# tasks simultaneously and take advantage of multi-core processors.
# Python provides a built-in threading module for working with threads.

# import threading
# import time

# def fun1(seconds):
#     print(f"sleeping for {seconds} seconds")
#     time.sleep(seconds)
# time1=time.perf_counter()
# # fun1(4)
# # fun1(2)
# # fun1(1)

# t1=threading.Thread(target=fun1,args=[4])
# t2=threading.Thread(target=fun1,args=[2])
# t3=threading.Thread(target=fun1,args=[1])
# t1.start()
# t2.start()
# t3.start()
# t1.join()
# t2.join()
# t3.join()
# time2=time.perf_counter()
# print(time2-time1)

from concurrent.futures import ThreadPoolExecutor
import time
# Function to be executed in parallel
def worker(seconds):
    print(f"sleeping for {seconds} seconds")
    time.sleep(seconds)
    return seconds

# Create a ThreadPoolExecutor
with ThreadPoolExecutor(max_workers=3) as executor:
    # Submit tasks to the executor
    # future1=executor.submit(worker,4)
    # future2=executor.submit(worker,2)
    # future3=executor.submit(worker,6)
    # print(future1.result())
    # print(future2.result())
    # print(future3.result())
    l=[3,5,2,1]
    results=executor.map(worker,l)
    for result in results:
        print(result)
