
"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""
from math import sqrt
print "Begun!"
val = 0
#iterate from 1 to 1000
for a in xrange(1000):
#since a<b, iterate over a+1 to 1000    
    for b in xrange(a + 1, 1000):
#since a**2 + b **2 = c**2, c will always be the square root of a**2 + b**2
        c = sqrt(a**2 + b**2)
#report every 100 iterations        
        if a%100 == 0 and a + 1 == b:
            print "finished %d iterations"  %a
#2- find when the sum of a, b, c equals 1000 and find the product, then break.
        if (a + b + c == 1000):
            val = a * b * c
            break
#break the outer loop also
    if val != 0: 
        break
print val
print "Finished!"