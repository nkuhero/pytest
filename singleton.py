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
