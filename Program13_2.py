#program to accept the radius of a circle and print its area

import math

def Calculate_Area(radius):
    area = math.pi * radius * radius
    print("Area of Circle is: ",area)

def main():
    radius = float(input("Enter radius: "))
    Calculate_Area(radius)

if __name__ == "__main__":
    main()