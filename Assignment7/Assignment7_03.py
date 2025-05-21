even = lambda A : A%2 == 0 

def main ():
    size = int(input("Enter size of list : "))

    data =[]

    print("Enter data : ")
    for i in range(size) :
        no = int(input())
        data.append(no)
    print ("list is : ",data)

    Fdata = list(filter(even,data))
    print("Even list : ",Fdata)


if __name__ == "__main__":
    main()