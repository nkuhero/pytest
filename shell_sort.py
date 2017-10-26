#coding=utf-8

def shell_sort(li):
    count = len(li)
    # 初始步长
    gap = int(count / 2)
    while gap > 0:
        for i in range(gap, count):
            # 每个步长进行插入排序
            key = li[i]
            j = i
            while j >= gap and li[j-gap] > key:
                li[j] = li[j-gap]
                li[j-gap] = key
                j -= gap
        # 得到新的步长
        gap = int(gap / 2)

    return li


if __name__ == "__main__":
    li = [6, 5, 4, 3, 2, 1]
    li = shell_sort(li)
    print(li)
