


# TODO

# TODO


def gcd(a,b):
    while b != 0:
        a, b = b, a % b
    return a



#(1)
a = 10
b = 20

result = gcd(a, b)
print("最大公約数:", result)
#(2)
c = 14
d = 91

result = gcd(c, d)
print("最大公約数:", result)

#(3)
e = 91
f = 14

result = gcd(e, f)
print("最大公約数:", result)
