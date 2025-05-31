import threading

def even():
    print("Even Thread : ")
    for i in range(2,21,2):
        print(i)

def odd():
    print("Odd Thread : ")
    for i in range(1,20,2):
        print(i)

def main():
    
    t1 = threading.Thread(target=even)
    t2 = threading.Thread(target=odd)

    t1.start()
    t1.join()

    t2.start()
    t2.join()

if __name__ == "__main__":
    main()