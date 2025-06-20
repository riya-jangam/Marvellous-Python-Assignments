import psutil
import time
import schedule

def ProcessScan():

    listprocess = []

    for proc in psutil.process_iter():
            info = proc.as_dict(attrs=['pid','name','username'])
            listprocess.append(info)
    
    print(listprocess)

def main():
    schedule.every(1).minute.do(ProcessScan)

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()