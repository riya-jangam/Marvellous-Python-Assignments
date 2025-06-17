import os 

def main():
    FileName = input("Enter the file name to check : ")

    ret = os.path.exists(FileName)

    if ret == True :
        print ("File exists \u2713")
        fobj = open(FileName,"r")
        data = fobj.read()

        print("Data from file is : ",data)

        fobj.close()
            
    else :
        print("File does not exist \u274C") 

if __name__ == "__main__":
    main()