#lambda function using filter() to return the count of even numbers 

def main():
    numbers = list(map(int, input("Enter numbers: ").split()))

    even = list(filter(lambda x: x % 2 == 0,numbers))

    print("Count of even numbers:",len(even))

if __name__ == "__main__":
    main()