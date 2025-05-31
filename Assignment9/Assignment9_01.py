import threading
import time

def num():
    print("Numbers: ")
    for i in range(1,6):
        print(i)

def main():
 
    T1 = threading.Thread(target=num)
    T2 = threading.Thread(target=num)
    T3 = threading.Thread(target=num)

    T1.start()
    T1.join()

    time.sleep(1)

    T2.start()
    T2.join()

    time.sleep(1)

    T3.start()
    T3.join()

    print("exit from main")

if __name__=="__main__":
    main()