def main ():
    FileName = "Student.txt"

    fobj = open(FileName,"w")
    
    data = ("Riya , Akhilesh , Gayatri , Aniket , Parth")
    
    fobj.write(data)

    fobj.close()


if __name__ == "__main__":
    main()