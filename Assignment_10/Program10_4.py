#print all even numbers till the given number 

def EvenNumbers(no):
    for i in range(2, no + 1, 2):
        print(i, end=" ")



def main():
    num = int(input("Enter a number: "))
    EvenNumbers(num)

if __name__ == "__main__":
    main()