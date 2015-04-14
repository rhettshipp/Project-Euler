
filename = '/Users/rhettshipp1/Desktop/Project-Euler/Data-Files/Euler-Question-67.txt'
with open(filename) as f:
    pyramid = f.read()

def merge(p):
    lastrow = p.pop(0)
    for i in range(len(p[0])):
        p[0][i] += max(lastrow[i], lastrow[i+1])

p = []
for line in pyramid.split('\n'):	
    z = []
    for x in line.split():
        z.append(int(x))
    if len(z) > 0:
        p.append(z)
p.reverse()

while len(p) > 1:
    merge(p)
    print len(p)
print p