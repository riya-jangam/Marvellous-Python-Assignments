import sys

def main():
    if len(sys.argv ) < 2 :
        print("Enter the inputs in command line")
        exit
    
    FileName = sys.argv[1]
    Search_name = sys.argv[2]
    
    fobj1 = open(FileName,"r")
    data = fobj1.read()

    frequency = data.count(Search_name)

    print("The string ",Search_name,"appears",frequency,"times in ",FileName)

    fobj1.close()

if __name__ == "__main__" :
    main()
