
value = 0
for x in xrange(10,100000000000,5):
    if x%2==0 and x%3==0 and x%4==0 and x%5==0 and x%7==0 \
       and x%9==0 and x%10==0 and x%11==0 and x%12==0 and x%13==0 \
       and x%14==0 and x%15==0 and x%16==0 and x%17==0 and x%18==0 \
       and x%19==0 and x%20==0:
           value = x
           break
print value