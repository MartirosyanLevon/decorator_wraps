import time
from functools import wraps


def testTime(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        start = time.time()
        res = fn(*args, **kwargs)
        duration = time.time() - start
        print(f'{duration=:.6f} sec')
        return res

    return wrapper


@testTime
def getNod(a, b):
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a


@testTime
def get_fastNod(a, b):
    if a < b:
        a, b = b, a
    while b:
        a, b = b, a % b
    return a


res1 = getNod(100000, 2)
print(res1)

res2 = get_fastNod(100000, 2)
print(res2)
