# Python learning script
# This file is for Git practice

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

if __name__ == "__main__":
    print("Fibonacci(10):", fibonacci(10))
    print("Factorial(5):", factorial(5))
