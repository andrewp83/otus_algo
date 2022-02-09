#!/usr/bin/python3

lucky_count = 1
for num in range(1001, 1000000):
	digits = [int(d) for d in str(num)]
	if sum(digits[-3:]) == sum(digits[:-3]):
		lucky_count += 1

print(lucky_count)
