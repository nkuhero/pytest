#最大公约数和最小公倍数

def max(a, b):
    v = a if a > b else b
    while v > 0:
        if a % v == 0 and b % v == 0:
            return v
        v -= 1

print(max(10, 15))

def min(a, b):
    h = a * b
    l = a if a > b else b
    for i in range(l, h+1):
        if i % a == 0 and i % b == 0:
            return i

print(min(15,20))
