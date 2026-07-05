#lambda function to check whether a number is divisble by 5 

divisible_by_5 = lambda x: x % 5 == 0 

def main():
    num = int(input("Enter a number : "))

    print(divisible_by_5(num))

if __name__ == "__main__":
    main()