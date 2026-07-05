#llambda function to multiply two numbers 

Multiplication = lambda a, b: a * b

def main():
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter a number: "))

    print("Multiplication =",Multiplication(num1, num2))

if __name__ == "__main__":
    main()