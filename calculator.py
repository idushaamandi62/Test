def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        print("Error: Division by zero")
        return None
    return a / b

def main():
    print("Simple Python Calculator")
    print("Operations: +, -, *, /")

    while True:
        print("\nEnter 'q' to quit")
        num1 = input("Enter first number: ")
        if num1 == 'q':
            break

        operator = input("Enter operator (+, -, *, /): ")
        if operator == 'q':
            break

        num2 = input("Enter second number: ")
        if num2 == 'q':
            break

        try:
            num1 = float(num1)
            num2 = float(num2)
        except ValueError:
            print("Error: Invalid number")
            continue

        if operator == '+':
            result = add(num1, num2)
        elif operator == '-':
            result = subtract(num1, num2)
        elif operator == '*':
            result = multiply(num1, num2)
        elif operator == '/':
            result = divide(num1, num2)
        else:
            print("Error: Invalid operator")
            continue

        if result is not None:
            print(f"Result: {num1} {operator} {num2} = {result}")

if __name__ == "__main__":
    main()
