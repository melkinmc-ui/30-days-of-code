import math

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    # Probamos divisores impares hasta la raiz cuadrada de n
    limit = int(math.isqrt(n))
    for i in range(3, limit + 1, 2):
        if n % i == 0:
            return False
            
    return True

t = int(input().strip())
for _ in range(t):
    n = int(input().strip())
    if is_prime(n):
        print("Prime")
    else:
        print("Not prime")