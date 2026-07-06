#Write a program which contains one function named ChkNum() which accepts one parameter as a number. If the number is even then display "Even Number", otherwise display "Odd Number".

def ChkNum(no):
    if no % 2 == 0:
        print("Even number")

    else:
        print("Odd number")

def main():
    num = int(input("Enter a number: "))

    ChkNum(num)

if __name__ == "__main__":
    main()
