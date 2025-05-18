freq = lambda A,B: A==B

def count (task ,values,num) :
    result = 0
    for no in values :
        if  no == num :
            result += 1
    print ("Output is : ",result)

        

def main ():
    size = int(input("Enter size : "))

    data = list()

    print("Enter Elements : ")
    for i in range(size):
        no = int(input())
        data.append(no)
    print("List : ",data)
    

    number = int(input("Element to search :"))
    ans = count(freq,data,number)
    

if __name__ == "__main__":
    main()