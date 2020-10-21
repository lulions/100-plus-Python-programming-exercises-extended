def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)


n = input("Choose a number to calculate the factorial for: ")

while True:
    try:
        n = int(n)
    except ValueError:
        n = input("Please provide a valid integer: ")
        continue
    break

print(f"The factorial of {n} is {factorial(n)}")
