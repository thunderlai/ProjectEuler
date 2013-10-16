import math

def largestprimefactor(n):
    largest = 1
    y = 0
    # first take the square root of the number, use the ceiling
    # we will iterate up to this, checking the largest prime number?
    nsqrt = int(math.ceil(math.sqrt(n)))
    # as soon as we find the current lowest divisible facotr, we should check the opposite, y
    for x in range(2, nsqrt):
        if(n%x == 0):
            if largestprimefactor(x) == 1 and x > largest:
                largest = x
            y = n/x
            #check if x is prime
            if largestprimefactor(y) == 1:
                return y
    return largest

print largestprimefactor(600851475143)
