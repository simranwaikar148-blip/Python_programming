#print the multiplication table of a number 

def Table(no):
    for i in range(1, 11):
        print(no * i,end=" ")

def main():
    num = int(input("Enter a number: "))
    Table(num)

if __name__ == "__main__":
    main()

