import threading

def inc():
    print("Even Thread : ")
    for i in range(1,51):
        print(i,end=" ")

def dec():
    print("Odd Thread : ")
    for i in range(50,0,-1):
        print(i,end=" ")


def main():
    
    t1 = threading.Thread(target=inc)
    t2 = threading.Thread(target=dec)

    t1.start()
    t1.join()

    t2.start()
    t2.join()

if __name__ == "__main__":
    main()