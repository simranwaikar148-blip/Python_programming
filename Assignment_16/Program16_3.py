#Write a program which contains one function named Add() which accepts two numbers from the user and returns the addition of those two numbers.

def Add(no1, no2):
    return no1 + no2

def main():
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter a number: "))

    result = Add(num1, num2)
    print("Addition : ",result)

if __name__ == "__main__":
    main()
