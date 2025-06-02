def count_iteration(no):
    length=len(str(no))
    count=0
    i=1
    while(i<=length):
        digit=no%10
        if(digit==0):
            count=count+1
        no=no//10
        i=i+1
    print("number of zeros using iteration: ",count)   

count=0
i=1
def count_recursion(no,length):
    global i
    global count 
    if(i<=length):
        digit=no%10
        if(digit==0):
            count=count+1
        no=no//10
        i=i+1
        count_recursion(no,length)
    return count
    
def main():
    print("enter number:")
    num=int(input())
    leng=len(str(num))
    count_iteration(num)
    result=count_recursion(num,leng)
    print("number of zeros using recursion: ",result) 

if __name__=="__main__":
    main()