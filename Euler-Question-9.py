
"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""
#1 - iterate 3 lists together (each from 1-1000)
for a in xrange(1000):
    for b in xrange(1000):
        for c in xrange(1000):
#2- if the 3 conditions are met, return the 3 values
            if (a < b < c) and (a**2 + b**2 == c**2) and (a + b + c == 1000):
                val = a * b * c
print val