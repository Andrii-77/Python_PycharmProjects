import multiprocessing
import time
import math


def time_decorator(func):
    def wrapper(*args, **kwargs):
        time_start = time.time()
        func(*args, **kwargs)
        time_end = time.time()
        print(time_end - time_start)

    return wrapper


def work(num):
    return str(math.sqrt(math.sqrt(math.sqrt(math.sqrt(num) / 2) / 20 ** 10))) + "I"


@time_decorator
def main_process():
    print('main_process')
    r = range(10000000)
    try:
        with open('file.txt', 'w') as f:
            for i in r:
                res = work(i)
                print(res, file=f)
    except Exception as e:
        print(e)


# main_process()

@time_decorator
def mp():
    print('multi_process')
    count = multiprocessing.cpu_count()
    print(count, 'CPUs')
    with multiprocessing.Pool(count) as p:
        r = range(10000000)
        try:
            with open('file2.txt', 'w') as f:
                tasks = p.map(work, r)
                for res in tasks:
                    print(res, file=f)
        except Exception as e:
            print(e)


if __name__ == '__main__':
    mp()
