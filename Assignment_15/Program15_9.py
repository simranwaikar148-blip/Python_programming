#lambda function using reduce() to return product of all elements 
from functools import reduce

def main():
    numbers = list(map(int, input("Enter numbers: ").split))

    product = reduce(lambda x, y: x * y,numbers)

    print("Product is:",product)

if __name__ == "__main__":
    main()
    