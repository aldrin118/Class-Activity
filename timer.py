from functools import wraps
from time import time

def timer(f):
    @wraps(f)
    def wrap(*args, **kw):
        ts = time()
        result = f(*args, **kw)
        te = time()
        print('func:%r args:[%r, %r] took: %2.4f sec' % \
          (f.__name__, args, kw, te-ts))
        return result
    return wrap
    
@timer
def f(a):
    for _ in range(a):
        i = 0
    return -1

f(10000000) 
