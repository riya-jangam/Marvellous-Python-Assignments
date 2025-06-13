def main():
    fobj=open("names.txt","w")
    fobj.write("Akhilesh\n")
    fobj.write("Riya\n")
    fobj.write("\n")
    fobj.write("Sarvesh\n")

    nfobj=open("new.txt","w")

    fobj=open("names.txt","r")
    lines=fobj.readlines()
    
    for i in lines:
        lines=i.split()
        if lines!=[]:
            nfobj.write(i)

if __name__=="__main__":
    main()