#print the factorial of a number 

def Factorial(no):
    fact = 1 
    for i in range(1, no + 1):
        fact = fact * i
    print("Factorial is: ",fact)

def main():
    num = int(input("Enter a number: "))
    Factorial(num)

if __name__ == "__main__":
    main()