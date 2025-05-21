double = lambda A : 2 * A 

def main ():
    size = int(input("Enter size of list : "))

    data =[]

    print("Enter data : ")
    for i in range(size) :
        no = int(input())
        data.append(no)
    print ("list is : ",data)

    Mdata = list(map(double,data))
    print("Doubled list : ",Mdata)


if __name__ == "__main__":
    main()