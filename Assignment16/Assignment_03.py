def main():
    FileName = "data.txt"

    fobj = open(FileName,"r")
    data = fobj.read() 

    line_count = len(data.splitlines())
    print("Number of lines are : ",line_count)

    word_count = len(data.split())
    print("Number of words are : ",word_count)  

    character_count = len(data)
    print("Number of characters are : ",character_count)

    fobj.close()
    
if __name__ == "__main__":
    main()

    