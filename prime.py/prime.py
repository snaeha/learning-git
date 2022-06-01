import math


# Prime Number function
# returns true if number is prime, false if it is not

def isPrime(n):
    if n < 2:
        return False
    if n % 2 == 0:
        return False
    for i in range(3, n, 2):
        if n % i == 0:
            return False
    return True

print(isPrime(163))