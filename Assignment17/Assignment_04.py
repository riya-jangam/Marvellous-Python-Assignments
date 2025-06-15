import schedule
import time
import datetime

def Display():
    print("Namskar \U0001F64F")

def main():
    schedule.every().day.at("09:00").do(Display)

    print("Application is in waiting state : ")

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()