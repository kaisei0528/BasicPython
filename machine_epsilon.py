# TODO

epsilon = 1.0

while 1.0 + epsilon > 1.0:
    epsilon /= 2.0
epsilon *= 2.0    
print(epsilon)    

a = 1
count = 1 + a
while count > 1:
    a /= 2
    count += a
    if count > 1:
        count = 1
        count += a
    print(count)
    





