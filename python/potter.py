#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import math

N = 25

def spell1(x, y):
    return x < y

def spell2(x, y):
    return x == y

def spell3(x, y):
    return x == N - 1 - y

def spell4(x, y):
    return y < N - x + 5

def spell12(x, y):
    return x**2 + y**2 <= 20**2

def spell5(x, y):
    return y == 2*x or y == 2*x+1

def spell9(x, y):
    return N - y - 1 >= x + 11 or N - y - 1 <= x - 11

def spell14(x, y):
    return (N - x - 1)**2 + (N - y - 1)**2 > 19.1**2

def spell17(x, y):
    return (N - x - 1 - 8) < 8*(math.sin((N - y - 1 - 4)*6.0/19.0))

def spell20(x, y):
    return (x + y) % 2 == 0

def spell22(x, y):
	return y%3 == (3-x)%3

def spell25(x, y):
	return x%6 == 0 or y%6 == 0


spells = [spell22]#[spell1, spell2, spell3, spell4, spell5, spell12, spell14, spell9, spell20]

def print_board(func):
	print()
	for x in range(N):
		for y in range(N):
			if func(x, y):
				print('# ', end='')
			else:
				print('. ', end='')
		print()
	print()

for spell in spells:
	print_board(spell)
	#input()
