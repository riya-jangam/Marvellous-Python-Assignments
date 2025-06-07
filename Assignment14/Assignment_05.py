class bankaccount:

    def __init__(self,a,b,c):
        self.name = a
        self.accountnumber = b
        self.balance = c

    def deposit(self):
        print("amount to deposit: ")
        dep_amount=int(input())
        self.balance=self.balance+dep_amount

    def withdraw(self):
        print("amount to withdraw: ")
        wid_amount=int(input())
        self.balance=self.balance-wid_amount

    def display(self):
        print("name: ",self.name)
        print("account number: ",self.accountnumber)
        print("balance: ",self.balance)
    
def main():
    obj1 = bankaccount("Riya",1111,2000)
    obj1.display()
    obj1.deposit()
    obj1.withdraw()
    obj1.display()

if __name__ == "__main__":
    main()
