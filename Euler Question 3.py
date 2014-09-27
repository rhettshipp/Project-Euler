"""
Primality test
"""
def is_prime(num):
    if not num % 2 or not num % 3:
        return False
    for i in range(5, int(num ** 0.5) + 1, 6):
            if not num % i or not num % (i + 2):
                return False
    return True
"""
Create a list containing all factors of 600851475143
"""
list = []
for x in xrange(775147, -1, -2):
    if 600851475143 % x == 0 and is_prime(x) == True:
        list.append(x)
print list[0]
        
        
