import random

def primality(n):
    value = random.randint(2,n-2)
    new = value **(n-1) % n

    if new ==1:
        print('the number is prime')
        return True
    else:
        print('The number is composite')
        return False
        
primality(23)