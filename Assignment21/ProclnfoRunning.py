import psutil
import sys

def processdisplay(pname):
    border="*"*80
    print(border)
    print("information of currently running processes : ")
    print(border)

    for proc in psutil.process_iter(['name']):
        try:
            if proc.info['name'] == pname:
                info = proc.as_dict(attrs=['pid','name','username'])
                print(info)
        except Exception:
            print("Exception occured")

def main():
    name=sys.argv[1]
    processdisplay(name)

if __name__ == "__main__":
    main()