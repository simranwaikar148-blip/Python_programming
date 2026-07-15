#Write a Python program to implement a class named Circle with the following requirements

class Circle:
    PI = 3.14

    def __init__(self):
        self.radius = 0.0
        self.area = 0.0
        self.circumference = 0.0

    def Accept(self):
        self.radius = float(input("Enter radius: "))

    def CalculateArea(self):
        self.area = Circle.PI * self.radius * self.radius

    def CalculateCircumference(self):
        self.circumference = 2 * Circle.PI * self.radius

    def Display(self):
        print("Radius: ",self.radius)
        print("Area: ",self.area)
        print("Circumference: ",self.circumference)
        print()

def main():
    n = int(input("Enter number of circles: "))

    for i in range(n):
        print("\nCircle", i + 1)
        obj = Circle()
        obj.Accept()
        obj.CalculateArea()
        obj.CalculateCircumference()
        obj.Display()

if __name__ == "__main__":
    main()
        

