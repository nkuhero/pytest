#coding=utf-8
def insert_sort(li):
    for i in range(1, len(li)):
        # 如果需要插入的元素大于前面的元素，则保持不动
        if li[i] < li[i-1]:
            j = i - 1
            key = li[i]
            while key < li[j] and j >= 0:
                li[j+1] = li[j]
                j -= 1
            li[j+1] = key
    return li

if __name__ == "__main__":
    li = [5, 4, 3, 6, 7, 2, 9, 1, 2]
    li = insert_sort(li)
    print(li)
