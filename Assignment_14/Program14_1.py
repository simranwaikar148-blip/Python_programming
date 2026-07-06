#lambda function to return the square of a number 

def main():
    square = lambda x: x * x

    num = int(input("Enter a number: "))
    print("Square =", square(num))

if __name__ == "__main__":
    main()