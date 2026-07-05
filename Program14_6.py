#lambda function to check whether a number is odd

Is_odd =lambda x: x % 2 != 0     # !=(no equal to zero)

def main():
    num = int(input("Enter a number: "))

    print(Is_odd(num))

if __name__ == "__main__":
    main()