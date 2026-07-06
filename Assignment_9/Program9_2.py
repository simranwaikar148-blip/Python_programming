#program to accept two numbers and print greater number using ChkGreater()

def ChkGreater(No1, No2):
    if No1 > No2:
        print("No2 is greater ",No1)
    else:
        print("No2 is greater ",No2)

    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    ChkGreater(num1, num2)
