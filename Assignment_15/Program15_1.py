#lambda function using map() to return a list of squares 
def main():
    numbers = list(map(int, input("Enter numbers: ").split()))

    square = list(map(lambda x: x * x, numbers))

    print("Squares: ",square)

if __name__ == "__main__":
    main()


