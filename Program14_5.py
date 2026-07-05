#lambda function to check whether a function is even

Is_even = lambda x: x % 2 == 0

def main():
    num = int(input("Enter a number: "))

    print(Is_even(num))

if __name__ == "__main__":
    main()