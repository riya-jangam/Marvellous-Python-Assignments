import os
import sys

def DirectoryWatcher(DirectoryName,extension):

    FileName = "Assignment_01.log"

    fobj = open(FileName,"a")
    
    flag = os.path.isabs(DirectoryName)

    if(flag == False):
        DirectoryName = os.path.abspath(DirectoryName)

    flag = os.path.exists(DirectoryName)

    if(flag == False):
        print("The path is invalid")
        exit()

    flag = os.path.isdir(DirectoryName)

    if(flag == False):
        print("Path is valid but the target is not a directory")
        exit()
        
    fobj.write("Files with extension " +extension+ " are : \n")
    for FolderName , SubFolderNames, FileNames in os.walk(DirectoryName):
        for fname in FileNames:
           if fname.endswith(extension):
                fobj.write(fname+"\n")

def main():
    DirectoryName = sys.argv[1]
    extension = sys.argv[2]

    DirectoryWatcher(DirectoryName,extension)

if __name__ == "__main__":
    main()