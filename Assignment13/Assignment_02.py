class BankAccount:

    ROI = 10.5

    def __init__ (self):
        self.Name = str(input("Enter Name : "))
        self.Amount = float(input("Enter initial amt : "))

    def Deposit(self):
        deposit_amount = float(input("Enter deposit amt : "))
        self.Amount += deposit_amount

    def Withdraw(self):
        withdraw_amount = float(input("Enter withdraw amt : "))
        if withdraw_amount <= self.Amount:
            self.Amount -= withdraw_amount
        else:
            print("Insufficient balance!")


    def CalculateInterest(self):
        interest = (self.Amount * BankAccount.ROI) / 100
        print("Interest : ",interest)

    def Display(self):
        print("Name : "+self.Name)
        print("Amount : ",self.Amount)
        

def main ():
    obj1= BankAccount()
    obj1.Deposit()
    obj1.Withdraw()
    obj1.CalculateInterest()
    obj1.Display()

if __name__ == "__main__":
    main()