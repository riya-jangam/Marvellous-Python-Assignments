def main():
    print("enter name of file: ")
    filename=input()
    fobj=open(filename,"r")
    lines=fobj.readlines()
    for i in lines:
        count=len(i.split()) 
        if count>=5:
            print(i)

    fobj.close()
    
if __name__ =="__main__":
    main()