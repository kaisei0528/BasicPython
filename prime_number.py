number1 = 61
number2= 10

# TODO

def is_prime(n):
    return n > 1 and all(n % i != 0 for i in range(2,int(n**0.5) + 1))
    
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

