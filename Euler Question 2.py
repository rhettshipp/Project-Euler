sum = 0
fibonacci = [1,2]
while fibonacci[-1]<=4000000:
    fibonacci.append(fibonacci[-1]+fibonacci[-2])
for x in fibonacci:
    if x%2==0:
        sum +=x
print sum
    