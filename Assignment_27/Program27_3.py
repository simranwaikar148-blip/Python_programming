#Write a Python program to implement a class named Numbers with the following specifications

class Numbers:


    def __init__(self, Value):
        self.Value = Value

    def ChkPrime(self):
        if self.Value < 2:
            return False
        
        for i in range(2, int(self.Value ** 0.5) + 1):
            if self.Value % i == 0:
                return False
        return True
    
    def chkPerfect(self):
        total = 0
        for i in range(1, self.Value):
            if self.Value % i == 0:
                total += i
        return total == self.Value
    
    def Factors(self):
        print("Factors are: ")
        for i in range(1, self.Value + 1):
            if self.Value % i == 0:
                print(i, end=" ")
        print()

    def SumFactors(self):
        total = 0
        for i in range(1, self.Value + 1):
            if self.Value % i == 0:
                total += i
        return total
    

def main():
    n = int(input("Enter number of objects: "))

    for i in range(n):
            
       
        print("\nObject", i + 1)
        value = int(input("Enter number: "))

        obj = Numbers(value)

        print("Prime:", obj.ChkPrime())
        print("Perfect:",obj.chkPerfect())

        obj.Factors()

        print("Sum of Factors:",obj.SumFactors())

if __name__ == "__main__":
    main()