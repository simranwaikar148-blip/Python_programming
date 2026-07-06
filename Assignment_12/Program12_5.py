#program to print numbers from N to 1 (reverse order)


def PrintNumbers_Reverse(num):
    for i in range(num, 0 , -1):
        print(i, end=" ")

def main():
    num = int(input("Enter a number: "))
    PrintNumbers_Reverse(num)

if __name__ == "__main__":
    main()
