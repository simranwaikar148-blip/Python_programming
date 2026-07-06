#Write a program which accepts a number from the user and returns the addition of digits in that number.

def Add_Digits(no):
    sum = 0 

    while no > 0:
      digit = no % 10
      sum += digit
      no = no // 10
      
    return sum




def main():
    num = int(input("Enter a number: "))
    print("Sum of Digits is: ",Add_Digits(num))



if __name__ == "__main__":
    main()