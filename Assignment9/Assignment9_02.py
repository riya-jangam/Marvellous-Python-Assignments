import multiprocessing

def square(values):
    print("Squared list is : ")
    for i in values:
        result=i**2
        print(result)

def main():
    print("enter number of elements: ")
    size=int(input())
    data=[]

    print("enter numeric values: ")
    for i in range(size):
        no=int(input())
        data.append(no)
    print("Original list is : ",data)

    P1 = multiprocessing.Process(target=square , args=(data,))

    P1.start()
    P1.join()

    print("exit from main")

if __name__=="__main__":
    main()