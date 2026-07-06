#lambda function using filter() to return numbers divisible by 3 and 5

def main():
    numbers = list(map(int, input("Enter numbers: ").split()))

    divisible_3_5 = list(filter(lambda x: x % 3 == 0 and x % 5 == 0,numbers))

    print("Numbers Divisible by 3 and 5:",divisible_3_5)

if __name__ == "__main__":
    main()