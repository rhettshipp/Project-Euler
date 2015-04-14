"""
2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?
"""

num = 2 ** 1000

str_num = str(num)
tot = 0
for x in str_num:
    tot += int(x)
print tot