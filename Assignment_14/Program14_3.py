#lambda function to return the maximum of two numbers 
maximum = lambda a, b: a if a > b else b

def main():
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    print("Maximum =", maximum(num1, num2))

if __name__ == "__main__":
    main()