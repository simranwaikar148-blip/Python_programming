#program to print numbers from 1 to N

def PrintNumbers(num):
    for i in range(i, num + 1):
        print(i, end=" ")



def main():
    num = int(input("Enter a number: "))
    PrintNumbers(num)

if __name__ == "__main__":
    main()