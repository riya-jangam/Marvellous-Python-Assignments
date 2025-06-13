def main ():
    FileName = "data.txt"

    fobj = open(FileName,"r") 

    display = fobj.read()

    print("Contents of file : ",display)
    
    fobj.close()

if __name__ == "__main__":
    main()