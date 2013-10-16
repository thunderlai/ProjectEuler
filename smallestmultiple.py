#smallest multiple
#find the smallest multiple of the numbers of 1 through 20.
# simple: just perform primefactorization on all numbers 1 through 20.
# check to see if they exist on the list already...

def factorize(n):
    # take a number n and return a list of its factors.
    # how to prime factorize?
    primefactors = []
    # don't include 1
    limit = n+1
    for x in range(2, limit):
        if n % x == 0:
            # add x to the primefactors
            primefactors.append(x)
            primefactors.extend(factorize(n/x))
            break  
    return primefactors

def smallestmultiple(n):
    allfactors = []
    for x in range(2, n+1):
        factors = factorize(x)
        factorscopy = factors
        print factors
        for y in range(2,n+1):
        # count how many there are in factors...
        # compare with how many there are in allfactors... add the difference of that item
            count1 = factors.count(y)
            count2 = allfactors.count(y)
            if count1 > count2:
                for z in range(count1 -count2):
                    allfactors.append(y)
    allfactors.sort()
    print allfactors
    result = reduce(lambda x, y: x*y, allfactors)
    return result
                
            
        
print smallestmultiple(20)
    
