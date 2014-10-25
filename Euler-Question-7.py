"""
Primality test
"""
def is_prime(num):
    if num <=3:
        if num <=1:
            return False
        return True
    if not num % 2 or not num % 3:
        return False
    for i in range(5, int(num ** 0.5) + 1, 6):
            if not num % i or not num % (i + 2):
                return False
    return True
"""
find the 10001st prime number
"""
num = 1
count = 0
value = 0
while count < 10001:
    if is_prime(num) == True:
        count += 1
        value = num
    num += 1
print value