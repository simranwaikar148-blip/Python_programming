#kambda function to return the cube of a number

def main():
    cube = lambda x:x * x * x

    num = int(input("Enter a number: "))
    print("Cube =",cube(num))

if __name__ == "__main__":
    main()