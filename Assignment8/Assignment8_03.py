import threading

def even_list(no):
    sum = 0
    for i in no:
        if i%2 == 0:
            sum += i
    print("Even thread",sum)

def odd_list(no):
    sum = 0
    for i in no:
        if i%2 != 0 :
            sum += i
    print("Odd thread",sum)

def main():
    size = int(input("Enter size of list : "))

    data =[]

    print("Enter data : ")
    for i in range(size) :
        no = int(input())
        data.append(no)
    print ("list is : ",data)
    
    t1 = threading.Thread(target=even_list,args=(data,))
    t2 = threading.Thread(target=odd_list,args=(data,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Exit from main")

if __name__ == "__main__":
    main()