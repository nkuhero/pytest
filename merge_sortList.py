def merge_sort(l1, l2, tmp):
    if len(l1) == 0 or len(l2) == 0:
        tmp.extend(l1)
        tmp.extend(l2)
        return tmp
    else:
        if l1[0] < l2[0]:
            tmp.append(l1[0])
            del l1[0]
        else:
            tmp.append(l2[0])
            del l2[0]
        return merge_sort(l1, l2, tmp)

l1 = [1,3,4,7,9,10]

l2 = [1,2,5,6,8,11]

result = merge_sort(l1, l2, [])

print(result)
