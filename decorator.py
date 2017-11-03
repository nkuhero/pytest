import datetime
from functools import wraps


def log(func):  
    @wraps(func)
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper


def log2(text):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator


@log
def now():
    print( datetime.datetime.now())


@log2("execute")
def now2():
    print(datetime.datetime.now())

if __name__ == "__main__":
    print now2.__name__
    print now.__name__
    now()
    now2()
