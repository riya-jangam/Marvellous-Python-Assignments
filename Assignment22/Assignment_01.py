import os
import sys
import time
import hashlib
import schedule
import smtplib
from email.message import EmailMessage

def calculatechecksum(path,blocksize=1024):
    fobj=open(path,"rb")

    hobj=hashlib.md5()

    buffer= fobj.read(blocksize)
    while(len(buffer)>0):
        hobj.update(buffer)
        buffer= fobj.read(blocksize)

    fobj.close()

    return hobj.hexdigest()

def findduplicate(directoryname="marvellous"):

    flag=os.path.isabs(directoryname)

    if(flag==False):
        directoryname=os.path.abspath(directoryname)

    flag=os.path.exists(directoryname)

    if(flag==False):
        print("the path is invalid")
        exit()

    flag=os.path.isdir(directoryname)

    if(flag==False):
        print("the path is valid but target is not a directory")
        exit()

    duplicate={}

    for FolderName , SubFoldersNames , FileNames in os.walk(directoryname):
        for fname in FileNames:
            fname=os.path.join(FolderName,fname)
            checksum=calculatechecksum(fname)

            if(checksum in duplicate):
                duplicate[checksum].append(fname)
            else:
                duplicate[checksum]=[fname]

    return duplicate

def deleteduplicate(path="marvellous"):

    mydict=findduplicate(path)

    result=list(filter(lambda x : len(x)>1 , mydict.values()))

    count=0
    cnt=0

    for value in result:
        for subvalue in value:
            count=count+1
            if (count>1):
                print("file deleted: ",subvalue)
                os.remove(subvalue)   
                cnt=cnt+1         
        count=0

    print("total deleted files: ",cnt)

def sendmail(fpath):

    fobj=open(fpath,"rb")
    data=fobj.read()

    msg = EmailMessage()
    msg.add_attachment(data,maintype="file",subtype="log",filename=fpath)

    msg['Subject'] = "log file of current processes"
    msg['From'] = "ajj.442.11@gmail.com"
    msg['To'] = "jangam.riyaa@gmail.com"

    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login("ajj.442.11@gmail.com", "xyz123")
    s.send_message(msg)
    s.quit()

def main():
 
    border="-"*66
    print(border)
    print("-----------------------Marvellous Automation----------------------")
    print(border)

    if(len(sys.argv)==3):
        if((sys.argv[1]=="--h") or (sys.argv[1]=="--H")):
            print("this application is used to perform directory cleaning")
            print("this is the directory automation script")
        
        elif((sys.argv[1]=="--u") or (sys.argv[1]=="--U")):
            print("use the given script as")
            print("scriptname.py nameofdirectory")
            print("please provide valid absolute path")

    if(len(sys.argv)==3):
            schedule.every(int(sys.argv[2])).minutes.do(deleteduplicate)

            while True:
                schedule.run_pending()
                time.sleep(1)

    else:
        print("invalid number of commandline arguments")
        print("use the given flags as ")
        print("--h : used to display the help")
        print("--u : used to display the usage")

    print(border)
    print("-----------------Thank you for using our script ------------------")
    print("----------------------Marvellous Infosystems----------------------")
    print(border)
    
if __name__ == "__main__":
    main()