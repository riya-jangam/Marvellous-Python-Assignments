import sys

def main():
    if len(sys.argv ) != 2 :
        print("Enter new file name as command argument")
        exit
    
    TargetFileName = sys.argv[1]
    SourceFileName = "Demo.txt"
    
    fobj1 = open(TargetFileName,"w")

    fobj2 = open(SourceFileName,"r")
    Data = fobj2.read()

    fobj1.write(Data)

    fobj2.close()
    fobj1.close()



if __name__ == "__main__" :
    main()