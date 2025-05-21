def Area(L,B):
    A = L * B
    print("Are of rectangle is : ",A)

def Perimeter(L,B):
    P = 2*(L+B)
    print("Perimeter of rectangle is : ",P)

def main():
    lenght = int(input("Enter lenght : "))
    width = int(input("Enter width : "))

    Area(lenght,width)
    Perimeter(lenght,width)

if __name__ == "__main__":
    main()
