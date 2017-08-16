#!/usr/bin/env python3
#coding=utf-8
def lazy_sum(*args):
    def sum():
        total = 0
        for i in args:
            total = total + i
        return total

    return sum


sum = lazy_sum(1,2,3,4,5)
print(sum())
