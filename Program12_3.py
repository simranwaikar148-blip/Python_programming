#program to perform addition,subtraction,multiplication, and division

def arithmetic_Operations(a, b):
    print("Addition =", a + b)
    print("Subtraction =", a - b)
    print("Multiplication =", a * b)

    if b != 0:
        print("Division =", a / b)
    else:
        print("Division is not possible")


def main():
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    arithmetic_Operations(num1, num2)


if __name__ == "__main__":
    main()