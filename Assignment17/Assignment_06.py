import schedule
import time
import datetime

def LunchTime():
    print("Lunch Time !!!")

def WrapUpTime():
    print("Wrap Up Work")


def main():
    schedule.every().day.at("13:00").do(LunchTime)

    schedule.every().day.at("18:00").do(WrapUpTime)

    print("Application is in waiting state : ")

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()