#TO do
def gcd(a,b):
    while b != 0:
        a, b = b, a % b
    return a
def judge_prime(a,b):
    if gcd(a,b) == 1:
        return True
    else:
        return False
judge_prime(5,3)        

     

          




