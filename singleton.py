class Singleton(type):
    def __new__(cls, name, bases, attrs):
        if not hasattr(cls, "_instace"):
            cls._instance = super(Singleton, cls)
