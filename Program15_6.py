#lambda function using reduce() to return the minimum element 

from functools import reduce

def main():
    numbers = list(map(int, input("Enter numbers: ").split()))

    minimum = reduce(lambda x, y: x if x < y else y, numbers)

    print("Minimum: ",minimum)

if __name__ == "__main__":
    main()