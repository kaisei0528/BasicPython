#TO do
def gcd(a,b):
    while b != 0:
        a, b = b, a % b
    return a
def judge_prime(a,b):
    gcd_result = gcd(a,b)
    if gcd(a,b) == 1:
        return True
    else:
        return False
a = 2
b = 3
result = judge_prime(a,b)
print(result)

     

          




