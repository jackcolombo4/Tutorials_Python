def calculate_factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers!")
    if n == 0:
        return 1
    else:
        return n * calculate_factorial(n - 1)

if __name__ == "__main__":
    try:
        num = int(input("Enter a non-negative integer: "))
        result = calculate_factorial(num)
        print(f"The factorial of {num} is {result}")
    except ValueError as e:
        print(e)
