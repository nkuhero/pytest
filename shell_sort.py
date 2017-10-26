#coding=utf-8
def shell_sort(li):
    n = len(li)
    # 初始步长
    gap = int(round(n / 2))
    while gap > 0:
        for i in range(gap, n):
            # 每个步长进行插入排序
            key = li[i]
            j = i
            # 插入排序
            while j >= gap and li[j - gap] > key:
                li[j] = li[j - gap]
                j -= gap
                li[j] = key
        # 得到新的步长
        gap = int(round(gap / 2))

    return li

if __name__ == "__main__":
    li = [6, 5, 4, 3, 2, 1]
    li = shell_sort(li)
    print(li)
