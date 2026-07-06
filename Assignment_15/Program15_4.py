#lambda function using reduce() to return the addition of all elements

from functools import reduce

def main():
    numbers = list(map(int, input("Enter numbers: ").split()))

    total = reduce(lambda x, y: x + y, numbers)

    print("Sum:", total)

if __name__ == "__main__":
    main()