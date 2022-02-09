#!/usr/bin/python3

from functools import reduce

def lucky_count(n):
    digits_sum_count = [1] * 10
    for _ in range(n - 1):
        current_digits_sum_count = [0] * (len(digits_sum_count) + 9)
        for i in range(10):
            for k in range(len(digits_sum_count)):
                current_digits_sum_count[i + k] += digits_sum_count[k]
        digits_sum_count = current_digits_sum_count
    return reduce(lambda total, current: total + current**2, digits_sum_count)

n = int(input())
print(lucky_count(n))