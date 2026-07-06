#program to accept length and width of a rectangle and print its area 

def Calculate_Area(length, width):
    area = length * width
    print("Area of Rectangle =",area)

def main():
    length = float(input("Enter length: "))
    width = float(input("Enter width: "))

    Calculate_Area(length, width)

if __name__ == "__main__":
    main()