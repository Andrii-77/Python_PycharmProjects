import threading
import time

# print("Hello world")
# print(threading.current_thread())

# def for_thread(a, b):
#     for i in range(100):
#         print("Hello", a, b)
#
#
# thread = threading.Thread(target=for_thread, args=(5, 6), name='for-thread')
# thread.start()
#
# for i in range(100):
#     print('Main')


# def show(n, t):
#     for i in range(n):
#         print(i, threading.current_thread().name)
#         time.sleep(t)
#
#
# thread1 = threading.Thread(target=show, args=(5, 1), name='thread1')
# thread2 = threading.Thread(target=show, args=(10, 0.5), name='thread2')
# thread1.start()
# thread2.start()
# thread1.join()
# thread2.join()
#
# print("Hello World!")


count = 0
lock = threading.Lock()


def inc():
    with lock:
        global count
        count += 1
        print(count)


threads = []

for _ in range(1000):
    thread = threading.Thread(target=inc)
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()
