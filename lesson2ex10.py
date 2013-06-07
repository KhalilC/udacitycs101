# Define a procedure, factorial, that
# takes one number as its input
# and returns the factorial of
# that number.

def factorial(n):
    multiplier = 1
    while n != 0:
        multiplier = n * multiplier
        n = n - 1
    return multiplier


        
    

#print factorial(4)
#>>> 24
#print factorial(5)
#>>> 120
#print factorial(6)
#>>> 720
