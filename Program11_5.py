 #check whether a number is pallindrome or not 

def CheckPallindrome(no):
    temp = no
    rev = 0

    while no > 0:
        digit = no % 10
        rev = rev * 10 + digit
        no = no // 10

    if temp == rev:
        print("Pallindrome")
    else:
        print("Not Pallindrome")



def main():
    num = int(input("Enter a number: "))
    CheckPallindrome(num)

if __name__ == "__main__":
    main()