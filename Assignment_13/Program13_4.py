#program to print the binary equivalent of a number 

def Binary_Equivalent(no):
    print("Binary Equivalent =",bin(no)[2:])

def main():
    num = int(input("Enter a number: "))
    Binary_Equivalent(num)

if __name__ == "__main__":
    main()