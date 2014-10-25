
totofsqr = 0
sqroftot = 0
tot = 0
for x in xrange(101):
    totofsqr += x**2
    tot += x
sqroftot = tot**2
difference = sqroftot - totofsqr
print difference