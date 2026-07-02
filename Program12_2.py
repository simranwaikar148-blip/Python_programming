#program to print the factors of a number 

def PrintFactors(num):
    print("Factors are: ")
    for i in range(1, num + 1):
        if num % i == 0:
            print(i, end=" ")


def main():
    num = int(input("Enter a number: "))
    PrintFactors(num)

if __name__ == "__main__":
    main()