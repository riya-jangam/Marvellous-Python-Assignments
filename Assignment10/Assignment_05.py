from functools import reduce

def chkprime (num): 
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                return 0
                break
        else:
            return  1
    else:
        return 0

multiple = lambda A : A *2

max = lambda A , B : A if A > B else B 


def main():
    size = int(input("Enter size : "))
    data=[]
    print("Enter values : ")
    for i in range (size):
        no = int(input())
        data.append(no)
    print("List is : ",data)

    Fdata = list(filter (chkprime,data))
    print("Filter Output Data : ",Fdata) 

    Mdata = list(map(multiple,Fdata))
    print("Map output data : ",Mdata)

    Rdata = (reduce(max,Mdata))
    print("Reduce output data is : ",Rdata)

if __name__ == "__main__":
    main()