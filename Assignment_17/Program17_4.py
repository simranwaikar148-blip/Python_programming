#Write a program which accepts one number from the user and returns the addition of its factors.

def SumFactors(no):
    sum = 0
    for i in range(1, no):
        if no % i == 0:
            sum += i
    return sum

def main():
    num = int(input("Enter number: "))
    print("Addition of factors =", SumFactors(num))

if __name__ == "__main__":
    main()