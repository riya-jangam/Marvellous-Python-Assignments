from MarvellousNum import chkprime

def ListPrime ():
    size = int(input("Enter size : "))

    data =[]

    print("Enter the values : ")
    for n in range(size):
        no = int(input())
        data.append (no)
    print("list is : ",data) 
    


    add = 0
    for i in data :
        if chkprime(i) == 1 :
            add = add + i 
            print ("Prime numbers are :",i,)
        
    print ("Addition of prime no is : ",add)

ListPrime()



