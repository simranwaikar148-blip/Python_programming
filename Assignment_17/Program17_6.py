#Write a program which accepts one number from the user and displays the following pattern.

def Pattern(no):
    for i in range(1, no + 1):
        for j in range(i):
            print("*", end=" ")
        print()


def main():
    num = int(input("Enter a number: "))
    Pattern(num)


if __name__ == "__main__":
    main()