#WRITE YOUR CODE IN THIS FILE
def factorial(x):
    f = 1
    for i in range(1, x+1):
        f = i * f
    return f