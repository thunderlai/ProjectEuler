# python fibonacci try project euler problem 2
x = 1
sum = 1
prevsum = 0

# fib
while( x <= 10) :
    sum = prevsum + sum
    prevsum = sum - prevsum
    print str(x) + "\t" + str(sum)
    x = x + 1
    

x = 1
sum = 1
prevsum = 0
evensum = 0

# evensumfib    
while( 1 ) :
    sum = prevsum + sum
    if(sum >= 4000000):
        break
    prevsum = sum - prevsum
    if(sum % 2 == 0):
        evensum = evensum + sum
    print str(x) + "\t" + str(sum)
    x = x + 1

print "sum of even values: " + str(evensum)