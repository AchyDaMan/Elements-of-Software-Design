# FACTORIALS

# def factorial(n):
#     if n == 1:
#         return 1
#     else:
#         return n * factorial(n-1)
    
# print(factorial(4))
# print(factorial(6))

# Fibonacci - 0, 1, 1, 2, 3, 5, 8, etc.


def fib(n):
    if n == 0:
        return 0
    else:
        return fib(n) + fib(n - 1)
    
print(fib(9))