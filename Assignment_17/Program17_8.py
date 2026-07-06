#Write a program which accepts one number from the user and displays the following pattern

def Display(no):
    for i in range(1, no + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()

def main():
    num = int(input("Enter number: "))
    Display(num)

if __name__ == "__main__":
    main()