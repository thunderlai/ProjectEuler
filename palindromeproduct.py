def numberOfDigits(n):
    if( n/10 == 0):
        return 1
    else:
        return 1 + numberOfDigits(n/10)
    
def getPlaceDigit(n, place):
    if(numberOfDigits(n)  < place):
        return 0
    else:
        x = (n / (10**(place-1))) % 10
        return x
    
def isPalindrome(n):
    place = 1
    numdigits = numberOfDigits(n)
    split = numdigits/2
    
    for x in range(1, split+1):
        if( not (getPlaceDigit(n,x) == getPlaceDigit(n, numdigits-x+1))):
            return False
    return True

def findLargestPalindrome():
    largest = 0
    for x in range(999, 100, -1):
        for y in range(999, 100, -1):
            product = x * y
            if( product > largest):
                if( isPalindrome(product) == True):
                    largest = product
    return largest

print findLargestPalindrome()