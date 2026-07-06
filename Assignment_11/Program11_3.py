#Find the sum of digits of a number 

def SumDigits(no):
    sum = 0 
    
    while no > 0:
        digit = no % 10
        sum = sum + digit
        no = no // 10

    print("Sum of Digits: ",sum)



def main():
    num = int(input("Enter a number: "))
    SumDigits(num)

if __name__ == "__main__":
    main()