def bubble_sort(li):
    count = len(li)
    for i in range(0, count):
        for j in range(i+1, count):
            if li[i] > li[j]:
                li[i], li[j] = li[j], li[i]
        print li
    return li

if __name__ == "__main__":
    li = [6, 5, 4, 3, 2, 1]
    li = bubble_sort(li)
    print(li)
