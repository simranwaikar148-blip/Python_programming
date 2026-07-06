#count the number of digits in a number

def CountDigits(no):
    count = 0

    while  no > 0:
        count = count + 1
        no = no // 10

        print("Count of digits: ",count)




def main():
    num = int(input("Enter a number : "))
    CountDigits(num)

if __name__ == "__main__":
    main()