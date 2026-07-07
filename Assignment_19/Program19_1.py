# Write a program which contains one lambda function
# which accepts one parameter and returns the power of two.

power = lambda x: x**2

def main():
    num = int(input("Enter a number: "))

    print("Output:",power(num))

if __name__ == "__main__":
    main()