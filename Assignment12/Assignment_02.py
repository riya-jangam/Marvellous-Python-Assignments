class Circle():

    PI = 3.14

    def __init__ (self):
        self.radius = 0.0
        self.area = 0.0
        self.circumference = 0.0


    def Accept (self):
        self.radius = int(input("Enter Radius : "))
    
    def CalculateArea(self):
        self.area = Circle.PI * self.radius ** 2

    def CalculateCircumference(self):
        self.circumference = 2 * Circle.PI * self.radius

    def Display(self):
        print("Radius is : ",self.radius)
        print("Area is : ",self.area)
        print("Circumference is : ",self.circumference)

def main ():
    obj1=Circle()

    obj1.Accept()
    obj1.CalculateArea()
    obj1.CalculateCircumference()
    obj1.Display()

if __name__ == "__main__":
    main()

