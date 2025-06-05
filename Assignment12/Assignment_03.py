class Arithmetic:

    PI = 3.14

    def __init__ (self):
        self.Value1 = 0
        self.Value2 = 0

    def Accept (self):
        self.Value1 = int(input("Enter Value1 : "))
        self.Value2 = int(input("Enter Value2 : "))

    def Addition(self):
        print("Addition : ",self.Value1 + self.Value2)

    def Subtraction(self):
        print("Subtraction : ",self.Value1 - self.Value2)

    def Multiplication(self):
        print("Multiplication : ",self.Value1 * self.Value2)

    def Division(self):
        print("Division : ",self.Value1 / self.Value2)

def main ():
    obj1=Arithmetic()
    obj2=Arithmetic()
    obj3=Arithmetic()
    obj4=Arithmetic()

    obj1.Accept()
    obj1.Addition()

    obj2.Accept()
    obj2.Subtraction()

    obj3.Accept()
    obj3.Multiplication()

    obj4.Accept()
    obj4.Division()

if __name__ == "__main__":
    main()
