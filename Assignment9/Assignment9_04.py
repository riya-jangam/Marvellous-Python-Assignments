import threading
import multiprocessing
import time

def Add ():
    sum = 0
    for i in range(10000000+1):
        sum += i
    print("Sum of numbers from 1 to 10M is : ",sum)

def main():
    normal_start = time.time()
    print("Execution by normal function")
    Add()
    normal_end = time.time()
    print("Execution time by normal function is : ",normal_end-normal_start)
    print()

    thread_start = time.time()
    print("Execution by Threading")
    T1= threading.Thread(target=Add)
    T1.start()
    T1.join()
    thread_end = time.time()
    print("Execution time by threading is : ",thread_end-thread_start)
    print()

    multiprocess_start = time.time()
    print("Execution by multiprocessing")
    P1=multiprocessing.Process(target=Add)
    P1.start()
    P1.join()
    multiprocess_end = time.time()
    print("Execution time by multiprocessing is : ",multiprocess_end-multiprocess_start)
    print()

    print("End from main")

if __name__ == "__main__":
    main()