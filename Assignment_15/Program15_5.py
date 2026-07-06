#lambda function using reduce() to return the maximum element

from functools import reduce

def main():
    numbers = list(map(int, input("Enter numbers: ").split()))

    maximum = reduce(lambda x, y: x if x > y else y, numbers)

    print("Maximum:", maximum)

if __name__ == "__main__":
    main()