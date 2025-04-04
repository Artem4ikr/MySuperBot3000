import os
import time

# Clear the terminal screen
def clear_screen():
    os.system('clear')  # Use 'cls' if you're on Windows

clear_screen()

def main():
    print("Simple Calculator")

    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    print("\nSelect Operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    choice = input("Enter choice (1/2/3/4): ")

    if choice == '1':
        print(f"Result: {a} + {b} = {a + b}")
    elif choice == '2':
        print(f"Result: {a} - {b} = {a - b}")
    elif choice == '3':
        print(f"Result: {a} * {b} = {a * b}")
    elif choice == '4':
        if b != 0:
            print(f"Result: {a} / {b} = {a / b}")
        else:
            print("Error: Division by zero is not allowed.")
    else:
        print("Invalid choice! Please select a valid option.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nExiting the program.")
        exit()
