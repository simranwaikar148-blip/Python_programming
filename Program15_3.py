#lambda function using filter() to return odd numbers 

def main():
    numbers = list(map(int, input("Enter numbers: ").split()))

    odd = list(filter(lambda x: x % 2 != 0, numbers))

    print("Odd numbers:", odd)

if __name__ == "__main__":
    main()