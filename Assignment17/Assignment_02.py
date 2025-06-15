import schedule
import time
import datetime

def ShowTime():
    print("Current time is : ",datetime.datetime.now())

def main():
    schedule.every(1).minute.do(ShowTime)

    print("Application is in waiting state : ")

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()