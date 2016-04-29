def factorial(number):
    if number <= 1:
        return 1
    else:
        fact = factorial(number - 1) * number
        return fact

print factorial(5)
