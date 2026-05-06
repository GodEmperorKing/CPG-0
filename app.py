import greetings

def add(x, y): return x + y
def subtract(x, y): return x - y
def multiply(x, y): return x * y
def divide(x, y):
    if y == 0: return "Error! Division by zero."
    return x / y
def minus_one(x): return x - 1
def double(x): return x * 2

print("--- Python Calculator ---")
print(greetings.generate_greeting("Samael"))
print("Select operation:\n1. Add\n2. Subtract\n3. Multiply\n4. Divide\n5. Subtract 1\n6. Double a number")

while True:
    choice = input("Enter choice (1-6) or 'q' to quit: ")

    if choice.lower() == 'q':
        print("Exiting calculator. Goodbye!")
        break

    if choice in ('1', '2', '3', '4', '5', '6'):
        
        if choice in ('5', '6'):
            try:
                num1 = float(input("Enter a number: "))
            except ValueError:
                print("Invalid input. Please enter a numeric value.")
                continue
            
            if choice == '5':
                print(f"{num1} - 1 = {minus_one(num1)}")
            else:
                print(f"{num1} doubled = {double(num1)}")
        else:
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input. Please enter numeric values.")
                continue

            if choice == '1': print(f"{num1} + {num2} = {add(num1, num2)}")
            elif choice == '2': print(f"{num1} - {num2} = {subtract(num1, num2)}")
            elif choice == '3': print(f"{num1} * {num2} = {multiply(num1, num2)}")
            elif choice == '4': print(f"{num1} / {num2} = {divide(num1, num2)}")

        print("-" * 20)
    else:
        print("Invalid Input. Please pick a number between 1 and 6.")
        print("-" * 20)
