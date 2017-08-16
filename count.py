#coding=utf-8
def count():
    fs = []
    for i in range(1, 6, 2):
        def f():
            return i * i
        fs.append(f)
    return fs


f1, f2, f3 = count()
print(f1())
print(f2())
print(f3())



def count2():
    fs = []
    def f(i):
        def g():
            return i * i
        return g
    for i in range(1, 6, 2):
        fs.append(f(i))
    return fs



f1, f2, f3 = count2()
print(f1())
print(f2())
print(f3())
