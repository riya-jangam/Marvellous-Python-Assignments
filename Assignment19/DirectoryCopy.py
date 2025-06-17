import os
import sys

def directorrename(directoryName,ext1,ext2):

    flag = os.path.isabs(directoryName)

    if(flag == False):
        directoryName = os.path.abspath(directoryName)

    flag = os.path.exists(directoryName)

    if(flag == False):
        print("The path is invalid")
        exit()

    flag = os.path.isdir(directoryName)

    if(flag == False):
        print("Path is valid but the target is not a directory")
        exit()

    for FolderName , SubFolderNames, FileNames in os.walk(directoryName):
        for fname in FileNames:
            if fname.endswith(ext1):
                old_file = os.path.join(FolderName, fname)
                new_file = os.path.join(FolderName, fname.replace(ext1, ext2))
                os.rename(old_file, new_file)
                print(new_file)

def main():
    dirName = sys.argv[1]
    extension1= sys.argv[2]
    extension2= sys.argv[3]

    directorrename(dirName,extension1,extension2)

if __name__ == "__main__":
    main()
