# 自定义一个 python 函数，实现 map() 函数的功能。

from typing import Callable, Sequence, Iterator


def my_map(func, seq) -> Iterator:
    for e in seq:
        yield func(e)


def test_func(num):
    return num * num

if __name__ == '__main__':
    a = my_map(lambda x: x ** 2, {1,2,3,4})
    print(next(a))
    print(next(a))
    print(next(a))
    print(next(a))
    # print(next(a))
    # print(list(a))