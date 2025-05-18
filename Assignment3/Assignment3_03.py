min = lambda A,B : A < B

def Minimun (task , values) :
    result = values[0]
    for no in values :
        if  no < result :
            result = no 
    print ("Maximum value is : ",result)

        

def main ():
    size = int(input("Enter size : "))

    data = list()

    print("Enter data : ")
    for i in range(size):
        no = int(input())
        data.append(no)
    print("List : ",data)

    ans = Minimun(min ,data)
    


if __name__ == "__main__":
    main()