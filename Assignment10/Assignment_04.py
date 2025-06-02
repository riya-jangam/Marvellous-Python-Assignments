from functools import reduce

even = lambda A : A % 2 == 0

square = lambda A : A *A

add = lambda A , B : A+B


def main():
    size = int(input("Enter size : "))
    data=[]
    print("Enter values : ")
    for i in range (size):
        no = int(input())
        data.append(no)
    print("List is : ",data)

    Fdata = list(filter (even,data))
    print("Filter Output Data : ",Fdata) 

    Mdata = list(map(square,Fdata))
    print("Map output data : ",Mdata)

    Rdata = (reduce(add,Mdata))
    print("Reduce output data is : ",Rdata)

if __name__ == "__main__":
    main()