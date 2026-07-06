#lambda function to return the minimum of two numbers 

minimum = lambda a, b: a if a < b else b

def main():
    num1 = int(input("Enter a number: "))
    num2 = int(input ("Enter a number: "))

    print("minimum =",minimum(num1, num2))

if __name__ == "__main__":
    main()