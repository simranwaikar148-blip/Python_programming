#print the sum of first N natural numbers 

def Sum(no):
    total = 0 
    for i in range(1, no + 1):
        total = total + i
    print("Sum is : ",total)

def main():
    num = int(input("Enter a number: "))
    Sum(num)

if __name__ == "__main__":
    main()