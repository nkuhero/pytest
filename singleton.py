class Singleton(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            cls._instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls._instance


class MySingleton(Singleton):
    pass


A = MySingleton()
B = MySingleton()

print(A is B)


class SingletonMetaClass(type):
    def __init__(cls, *args, **kwargs):
        cls._instance = None
        super(SingletonMetaClass, cls).__init__(*args, **kwargs)

    def __call__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(SingletonMetaClass, cls).__call__(*args, **kwargs)
        return cls._instance

class MyClass2(object):
    __metaclass__ = SingletonMetaClass
    pass


A = MySingleton()
B = MySingleton()

print(A is B)
