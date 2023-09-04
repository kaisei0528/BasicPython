number1 = 61
number2= 10

# TODO
def is_prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True
    
#素数判定
if is_prime(number1):
    print(number1,"は素数です")
else:
    print(number1,"は素数ではありません")    
if is_prime(number2):
    print(number2,"は素数です")
else:

    print(number2,"は素数ではありません")                 


result = is_prime(5)
print(type(number1))
print(type(number2))
    




    
print(number2,"は素数ではありません")                 

