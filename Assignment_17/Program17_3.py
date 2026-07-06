#Write a program which accepts one number from the user and returns its factorial.

def Factorial(no):
    fact = 1
    for i in range(1, no + 1):
        fact *= i
    return fact


def main():
    num = int(input("Enter a number: "))

    print("Factorial: ",Factorial(num))


if __name__ == "__main__":
    main()