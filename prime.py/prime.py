import math


# Prime Number function
# returns true if number is prime, false if it is not

def isPrime(n):
    for i in range(2,n):
        if n % i == 0:
            return False
    return True

print(isPrime(163))