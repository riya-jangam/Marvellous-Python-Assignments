import schedule
import time
import datetime

def Display():
    print("JAY GANESH...")

def main():
    schedule.every(2).seconds.do(Display)

    print("Application is in waiting state : ")

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()