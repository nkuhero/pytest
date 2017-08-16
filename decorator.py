import datetime



def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper


def log2(text):
    def decorator(func):
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
    now()
    now2()
