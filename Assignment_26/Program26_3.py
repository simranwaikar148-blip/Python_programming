#Write a Python program to implement a class named Arithmetic with the following characteristics

class Arithematic:

    def __init__(self):
        self.Value1 = 0
        self.Value2 = 0

    def Accept(self):
        self.Value1 = int(input("Enter value1: "))
        self.Value2 = int(input("Enter value2: "))

    def Addition(self):
        return self.Value1 + self.Value2
    
    def Subtraction(self):
        return self.Value1 - self.Value2
    
    def Multiplication(self):
        return self.Value1 * self.Value2
    
    def Division(self):
        if self.Value2 == 0:
            return "Division is not possible"
        return self.Value1 / self.Value2
    
def main():
    n = int(input("Enter number of objects: "))

    for i in range(n):
        print("\nArithematic object", i + 1)
        obj = Arithematic()
        obj.Accept()

        print("Addition: ",obj.Addition())
        print("Subtraction: ",obj.Subtraction())
        print("Multiplication: ",obj.Multiplication())
        print("Division: ",obj.Division())
    
if __name__ == "__main__":
    main()
