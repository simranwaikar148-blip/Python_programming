#Write a program which contains one function that accepts one number from the user and returns True if the number is divisible by 5; otherwise returns False

def check_divisible_5(no):
    if no % 5 == 0:
       return True
    else:
       return False


def main():
    num = int(input("Enter a number: "))

    result = check_divisible_5(num)
    print(result)

if __name__ == "__main__":
    main()