def perfect_number(num):
    total = 0
    for i in range(1, num):
        if num % i == 0:
            total += i
    if total == num:
        return True
    else:
        return False


for i in range(1, 100):
    if perfect_number(i):
        print(i)
    
