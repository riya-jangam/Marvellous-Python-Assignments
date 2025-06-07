class Employee :
    def __init__(self,A,B,C):
        self.Name = A
        self.Emp_ID = B
        self.Salary = C

    def display (self):
        print("Name : "+self.Name)
        print("ID : ",self.Emp_ID)
        print("Salary : ",self.Salary)

def main():
    obj1 = Employee("Rohit",50000,101)
    obj1.display() 

if __name__ == "__main__":
    main()