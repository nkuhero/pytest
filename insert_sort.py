#coding=utf-8
def insert_sort(li):
    # 插入排序
    count = len(li)
    for i in range(1, count):
        key = li[i]
        j = i - 1
        while j >= 0:
            if li[j] > key:
                li[j + 1] = li[j]
                li[j] = key
            j -= 1
    return li



if __name__ == "__main__":
    li = [5, 4, 3, 6, 7, 2, 9, 1, 2]
    li = insert_sort(li)
    print(li)
