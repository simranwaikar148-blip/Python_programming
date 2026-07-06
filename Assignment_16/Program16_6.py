#Write a program which accepts a number from the user and checks whether that number is positive, negative, or zero.

def CheckNum(no):
    if no > 0:
        print("Positive")
    elif no < 0:
        print("Negative")
    else:
        print("Zero")


def main():
    num = int(input("Enter a number: "))
    CheckNum(num)

if __name__ == "__main__":
    main()