class Rectangle :
    def __init__(self,A,B):
        self.Lenght = A
        self.Width = B

    def Area (self):
        Area = self.Lenght * self.Width
        print ("Area : ",Area)

    def Perimeter (self):
        Perimeter = 2*(self.Lenght + self.Width)
        print ("Perimeter : ",Perimeter)

def main():
    obj1 = Rectangle(10,5)
    obj1.Area()
    obj1.Perimeter()

if __name__ == "__main__":
    main()
