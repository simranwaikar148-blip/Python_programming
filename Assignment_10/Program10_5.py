#print all odd numbers till the given number 

def OddNumbers(no):
    for i in range(1, no + 2, 2):
        print(i, end=" ")
    

def main():
    num = int(input("Enter the number: "))
    OddNumbers(num)


if __name__ == "__main__":
    main()