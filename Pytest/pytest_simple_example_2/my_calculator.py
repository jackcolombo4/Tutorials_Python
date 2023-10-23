class Calculator:
    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        if y == 0:
            raise ValueError("Cannot divide by zero")
        return x / y
    
    def square(self, x):
        return x ** 2

    def cube(self, x):
        return x ** 3

    def sqrt(self, x):
        if x < 0:
            raise ValueError("Cannot take square root of a negative number")
        return x ** 0.5