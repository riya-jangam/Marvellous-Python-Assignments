class person:

    def __init__(self, a, b ):
        self.name = a
        self.age = b

    def display(self):
        print("Name: "+self.name)
        print("age: ",self.age)

class teacher(person):
    def __init__(self,c,d,e,f):
        super().__init__(c,d)
        self.subject=e
        self.salary=f
    
    def display1(self):
        print("subject: "+self.subject)
        print("salary: ",self.salary)
        
def main():
    obj1=teacher("Riya",23,"Maths",35000)
    obj1.display()
    obj1.display1()

if __name__ == "__main__":
    main()