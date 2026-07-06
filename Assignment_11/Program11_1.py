#Check whether a number is prime or not 

def CheckPrimeNo(no):
    if no <= 1:
        print("Not Prime number")
        return
        

    for i in range(2, no):
        if i % 2 == 0:
            print("Not Prime Number ")
            return
            

def main():
    num = int(input("Enter a number: "))
    CheckPrimeNo(num)

if __name__ == "__main__":
    main()