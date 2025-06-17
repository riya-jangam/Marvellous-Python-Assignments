import os
import sys
import shutil

def directorycopycontents(directoryName,directoryName2,Extension):

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
    
    os.mkdir(directoryName2)

    for FolderName , SubFolderNames, FileNames in os.walk(directoryName):
        for fname in FileNames:
            if fname.endswith(Extension):
                source = os.path.join(directoryName, fname)
                destination = os.path.join(directoryName2, fname)
                if os.path.isfile(source):
                    shutil.copy2(source, destination)
                    print(f"Copied: {source} -> {destination}")
                
def main():
    dirName1 = sys.argv[1]
    dirName2 = sys.argv[2]
    Extension = sys.argv[3]

    directorycopycontents(dirName1,dirName2,Extension)

if __name__ == "__main__":
    main()