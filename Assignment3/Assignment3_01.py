add = lambda A ,B : A+B

def addition (task ,values):
        result = 0

        for no in values :
            result = result+ no
        print("Addition is : ",result)



def main():
    print("Enter Size : ")
    size = int(input())

    data = list()

    print("Enter the values: ")
    for i in range(size):
        no = int(input())
        data.append(no)

    print ("List is :",data)
    
    ans = addition(add,data)
    
    

 

if __name__ == "__main__":
    main()