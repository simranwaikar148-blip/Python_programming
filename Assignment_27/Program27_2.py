#Write a Python program to implement a class named BankAccount with the following requirements

class BankAccount:
    ROI = 10.5

    def __init__(self, Name, Amount):
        self.Name = Name
        self.Amount = Amount

    def Display(self):
        print("Account Holder:", self.Name)
        print("Balance:", self.Amount)

    def Deposit(self):
        amt = float(input("Enter deposit amount: "))
        self.Amount += amt
        print("Amount Deposited Successfully")

    def Withdraw(self):
        amt = float(input("Enter withdrawal amount: "))
        if amt <= self.Amount:
            self.Amount -= amt
            print("Withdrawal Successful")
        else:
            print("Insufficient Balance")

    def CalculateInterest(self):
        interest = (self.Amount * BankAccount.ROI) / 100
        return interest


def main():
    n = int(input("Enter number of accounts: "))

    for i in range(n):
        print("\nAccount", i + 1)
        name = input("Enter Account Holder Name: ")
        amount = float(input("Enter Initial Balance: "))

        obj = BankAccount(name, amount)

        obj.Display()
        obj.Deposit()
        obj.Display()
        obj.Withdraw()
        obj.Display()

        print("Interest =", obj.CalculateInterest())


if __name__ == "__main__":
    main()