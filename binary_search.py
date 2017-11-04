#二分法查找
def search(li, key):
    if len(li) < 1:
        return False
    mid = len(li) // 2
    v = li[mid]
    if key == v:
        return True
    elif key < v:
        return search(li[:mid], key)
    else:
        return search(li[mid+1:], key)

li = [1,3,4,5,6]
print(search(li,6))
