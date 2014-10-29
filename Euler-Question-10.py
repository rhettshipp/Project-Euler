"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

#First - import the primality test used previously.

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

#Test each number from 1-1,999,999 for primality. If prime add to sum.

prime_total = 2
# Skip evens because no even number (other than 2) is prime.
# Since we skip evens, we need to start our prime_total at 2.
for x in xrange(1,2000000,2):
    if is_prime(x) == True:
        prime_total += x
print prime_total