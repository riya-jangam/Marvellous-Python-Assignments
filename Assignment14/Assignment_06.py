class calculator():

    def __init__(self):
        self.value1 = int(input("enter value1: "))
        self.value2 = int(input("enter value2: "))
    
    def addition(self):
        print("addition: ", self.value1+self.value2)

    def subtraction(self):
        print("subtraction: ", self.value1-self.value2)

    def multiplication(self):
        print("multiplication: ", self.value1*self.value2)

    def division(self):
        print("division: ", self.value1/self.value2)
        
def main():
    obj1 = calculator()

    obj1.addition()
    obj1.subtraction()
    obj1.multiplication()
    obj1.division()
    
if __name__ == "__main__":
    main()