#Write a program which contains one lambda function which accepts two parameters and returns its multiplication.

multiplication = lambda x, y: x * y

def main():
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    print("Multiplication :", multiplication(num1, num2))

if __name__ == "__main__":
    main()