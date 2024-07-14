def add(a, b):
   return a + b

def subtract(a, b):
   return a - b

def multiply(a, b):
   return a * b

def divide(a, b):
   return a / b

def remainder(a, b):
    if b == 0:
        raise ValueError("Division by zero is not allowed.")
    return a % b