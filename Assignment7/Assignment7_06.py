def prime(no):
    factor = 1
    for i in range (1,no+1):
        if no%i == 0 :
            factor *= i
    if factor == no :
        return 1
    else :
        return 0



def main():
    size = int(input("Enter size of list : "))

    data =[]

    print("Enter data : ")
    for i in range(size) :
        no = int(input())
        data.append(no)
    print ("list is : ",data)

    Fdata = list(filter(prime,data))
    print("Prime list : ",Fdata)


if __name__=="__main__":
    main()