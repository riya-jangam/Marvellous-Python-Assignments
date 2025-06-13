import sys

def main():
    if len(sys.argv ) < 2 :
        print("Enter new file names that need to be compared")
        exit
    
    TargetFileName = sys.argv[1]
    SourceFileName = sys.argv[2]
    
    fobj1 = open(TargetFileName,"r")
    data1 = fobj1.read()

    fobj2 = open(SourceFileName,"r")
    data2 = fobj2.read()

    if data1 == data2 :
        print("Success \U0001F44D")
    
    else :
        print("Not same data \U0001F44E")

    fobj2.close()
    fobj1.close()



if __name__ == "__main__" :
    main()