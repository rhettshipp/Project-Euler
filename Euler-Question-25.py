"""
The Fibonacci sequence is defined by the recurrence relation:

Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
Hence the first 12 terms will be:

F1 = 1
F2 = 1
F3 = 2
F4 = 3
F5 = 5
F6 = 8
F7 = 13
F8 = 21
F9 = 34
F10 = 55
F11 = 89
F12 = 144
The 12th term, F12, is the first term to contain three digits.

What is the first term in the Fibonacci sequence to contain 1000 digits?
"""

sum = 0
# create a fibonacci sequence up to 4000000
fib1 = 1
fib2 = 2
fibonacci = [1,2]
while fibonacci[-1]<=1000000000000:
    fibonacci.append(fibonacci[-1]+fibonacci[-2])
#sum all fibonacci numbers up to 400000 that are multiples of 2

"""
Note - rather than creating a list of fibonacci numbers, I need
to come up with a way to replace my fibonacci numbers with the next
in the sequence so I'm only storing 1 (or a few) fibonnaci numbers
at a time rather than the whole set
"""