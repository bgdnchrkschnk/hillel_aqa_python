import memory_profiler # pip install memory_profiler
import time


def check_even(numbers):
    even = []
    for num in numbers:
        if num % 2 == 0:
            even.append(num * num)
    return even


if __name__ == '__main__':
    m1 = memory_profiler.memory_usage()
    t1 = time.time()
    n2 = check_even(range(100_000_000))
    t2 = time.time()
    m2 = memory_profiler.memory_usage()
    time_diff = t2 - t1
    mem_diff = m2[0] - m1[0]
    print(f"It took {time_diff:.4f} secs and {mem_diff} Mb to execute this method")
    # print(n2)


import memory_profiler
import time


def check_even(numbers):
    for num in numbers:
        if num % 2 == 0:
            yield num * num


if __name__ == '__main__':
    m1 = memory_profiler.memory_usage()
    t1 = time.time()
    result = []
    for itm in check_even(range(100_000_000)):
        result.append(itm)
    t2 = time.time()
    m2 = memory_profiler.memory_usage()
    time_diff = t2 - t1
    mem_diff = m2[0] - m1[0]
    print(f"It took {time_diff:.4f} secs and {mem_diff} Mb to execute this method")
    print(result)