#Write a program which accepts a number from the user and returns the number of digits in that number.

def CountDigits(no):
    count = 0

    while no > 0:
        count += 1
        no = no // 10

    return count


def main():
    num = int(input("Enter a number: "))
    print("Digit Count is: ",CountDigits(num))


if __name__ == "__main__":
    main()