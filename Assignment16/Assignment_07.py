def main():
    fobj=open("marks.txt","w")
    fobj.write("Akhilesh 69\n")
    fobj.write("Riya 99\n")
    fobj.write("Aniket 95\n")
    fobj.write("Sarvesh 93.6\n")

    fobj=open("marks.txt","r")
    lines=fobj.readlines()
    
    print("students with marks greater than 75: ")
    for i in lines:
        data=i.split()
        if float(data[1])>=75:
            print(data[0],"-",data[1])

    fobj.close()

if __name__ == "__main__":
    main()