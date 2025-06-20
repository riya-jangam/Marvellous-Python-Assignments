import psutil
import os
import time
import sys
import smtplib
from email.message import EmailMessage

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
    s.login("ajj.442.11@gmail.com", "vpng ktbp aahp oqnj")
    s.send_message(msg)
    s.quit()

def createlog(foldername):
    if not os.path.exists(foldername):
        os.mkdir(foldername)

    timestamp=time.ctime()
    timestamp=timestamp.replace(" ","")
    timestamp=timestamp.replace(":","_")
    timestamp=timestamp.replace("/","_")

    filename=os.path.join(foldername,"marvellous%s.log" %(timestamp))

    fobj=open(filename,"w")

    border="-"*80

    fobj.write(border)
    fobj.write("\n\t\tmarvellous infosystems process log\n")
    fobj.write("\n\t\tlog file is created at: "+time.ctime()+"\n")
    fobj.write(border)

    data=processscan()
    for value in data:
        fobj.write("%s \n" %value)

    fobj.write(border)

    fobj.close()

    return filename

def processscan():

    listprocess=[]

    for proc in psutil.process_iter():
        try:
            info=proc.as_dict(attrs=["name","pid","username"])
            listprocess.append(info)
        except (psutil.NoSuchProcess,psutil.AccessDenied,psutil.ZombieProcess):
            pass

    return listprocess

def main():
    dirname=sys.argv[1]
    path=createlog(dirname)
    sendmail(path)

if __name__ == "__main__":
    main()