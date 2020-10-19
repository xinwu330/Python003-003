# 实现一个 @timer 装饰器，记录函数的运行时间，注意需要考虑函数可能会接收不定长参数。

import time
from functools import wraps

def timer(func):
    @wraps(func)
    def get_excution_time(*args, **kwargs):
        start_time = time.time()
        v = func(*args, **kwargs)
        end_time = time.time()
        print(f'Excuted {func.__name__} takes: {end_time - start_time} seconds')
        return v
    return get_excution_time 