import multiprocessing

def factorial(no):
    for i in range(1,no):
        no=no*i
    return no

def main():
    print("enter number of elements: ")
    size=int(input())
    data=[]

    print("enter numeric values: ")
    for i in range(size):
        no=int(input())
        data.append(no)
    print("the list is: ",data)

    result = []

    p = multiprocessing.Pool()
    result = p.map(factorial,data)

    p.close()
    p.join()
    
    print("list of factorials is: ",result)

if __name__=="__main__":
    main()