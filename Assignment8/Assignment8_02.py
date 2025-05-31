import threading

def even_factors(no):
    sum = 0
    for i in range(2,no+1,2):
        if (no%i == 0):
            sum += i
    print("Even thread",sum)

def odd_factors(no):
    sum = 0
    for i in range(1,no+1,2):
        if(no%i == 0):
            sum += i
    print("Odd thread",sum)

def main():
    number = int(input("Enter number : "))
    t1 = threading.Thread(target=even_factors,args=(number,))
    t2 = threading.Thread(target=odd_factors,args=(number,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Exit from main")

if __name__ == "__main__":
    main()