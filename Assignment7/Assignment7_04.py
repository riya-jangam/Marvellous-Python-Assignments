from functools import reduce

product = lambda A , B : A * B

def main():
    size = int(input("Enter size of data : "))

    data = []

    print("Enter Data : ")
    for i in range(size) :
        no = int(input())
        data.append(no)
    print ("List is : ",data)

    Rdata = reduce(product,data)
    print("Product is : ",Rdata)

if __name__ == "__main__":
    main()