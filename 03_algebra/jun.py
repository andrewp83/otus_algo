#!/usr/bin/python3

def power(x, p):
    result = 1
    for i in range(p):
        result *= x
    return result

def fib(n):
    if n == 1 or n == 2:
        return 1
    return fib(n - 1) + fib(n - 2)

def fib_it(n):
    fib_prev = fib_cur = 1
    for _ in range(2, n):
        new_cur = fib_cur + fib_prev
        fib_prev = fib_cur
        fib_cur = new_cur
    return fib_cur

def is_prime(n):
    for i in range(2, n/2 + 1):
        if n % i == 0:
            return False
    return True

def prime_count(n):
    return sum(1 for i in range(n) if is_prime(i + 1))
