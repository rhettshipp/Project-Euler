
"""
palinrome test
"""

def is_palindrome(num):
    numstring = str(num)
    numlist = list(numstring)
    if numlist == numlist[::-1]:
        return True
    return False

"""
create a list consisting of all palindrome numbers
resulting in multiplying any two
triple digit numbers together
"""
L = []
value = 0
# Multiply all triple digit numbers together
for x in xrange(101,1000):
    for y in xrange(101,1000):
        # If it is a palindrone, append it to a list
        if  is_palindrome(x*y) == True:
            L.append(x*y)
print max(L)

