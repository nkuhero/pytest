def quicksort(li):
    smaller = []
    bigger = []
    if len(li) < 1:
        return li
    k = li.pop()
    for i in li:
        if i > k:
            bigger.append(i)
        else: 
            smaller.append(i)
    return quicksort(smaller) + [k] + quicksort(bigger)


li = [5,4,3,6,7,2,9,1,2,9]

print(quicksort(li))
