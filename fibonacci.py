import random

n = random.random() * 1000    #Create random integer input 0-1000
o = [0, 1]

for n in range(0, int(n)):
    p2 = [o[len(o)-1], o[len(o)-2]]
    o.append(p2[0] + p2[1])  

print (n)
print (o)
