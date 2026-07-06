#lambda function to return the largest of three numbers

Largest = lambda a, b, c: a if a>=b and a>=c else (b if b>=c else c)

def main():
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    num3 = int(input("Enter third numbner: "))

    print("Largest number is=",Largest(num1, num2, num3))

if __name__ == "__main__":
    main()