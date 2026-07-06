#Write a program which accepts one number from the user and displays the following pattern.

def Display(no):
    for i in range(no):
        for j in range(no):
            print("*", end=" ")
        print()



def main():
    num = int(input("Enter a number: "))
    Display(num)


if __name__ == "__main__":
    main()