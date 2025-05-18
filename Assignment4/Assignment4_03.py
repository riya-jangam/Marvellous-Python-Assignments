from functools import reduce

filt = lambda A : 70<= A <=90

increase = lambda A : A + 10

product = lambda A , B : A*B


def main():
    size = int(input("Enter size : "))
    data=[]
    print("Enter values : ")
    for i in range (size):
        no = int(input())
        data.append(no)
    print("List is : ",data)

    Fdata = list(filter (filt,data))
    print("Filter Output Data : ",Fdata) 

    Mdata = list(map(increase,Fdata))
    print("Map output data : ",Mdata)

    Rdata = (reduce(product,Mdata))
    print("Reduce output data is : ",Rdata)

if __name__ == "__main__":
    main()