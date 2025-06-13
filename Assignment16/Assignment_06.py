import sys

def main():
    if len(sys.argv ) < 2 :
        print("Enter new file names that need to be compared")
        exit
    
    DestinationFileName = sys.argv[1]
    SourceFileName = sys.argv[2]
    
    fobj1 = open(SourceFileName,"r")
    data2 = fobj1.read()

    fobj2 = open(DestinationFileName,"w")
    data2 = fobj2.write(data2)

    fobj1.close()
    fobj2.close()



if __name__ == "__main__" :
    main()