#Write a program which accepts one number from the user and checks whether it is a prime number or not.

def CheckPrime(no):
    if no <= 1:
        return False

    for i in range(2, no):
        if no % i == 0:
            return False

    return True

def main():
    num = int(input("Enter number: "))

    if CheckPrime(num):
        print("It is Prime Number")
    else:
        print("It is Not Prime Number")

if __name__ == "__main__":
    main()