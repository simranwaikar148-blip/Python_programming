#program to check whether a number is a perfect number

def CheckPerfect(no):
    total = 0 

    for i in range(1, no):
        if no % i == 0:
            total += i

    if total == no:
        print("Perfect Number")
    else:
        print("Not a Perfect Number")

def main():
    num = int(input("Enter a number: "))
    CheckPerfect(num)

if __name__ == "__main__":
    main()