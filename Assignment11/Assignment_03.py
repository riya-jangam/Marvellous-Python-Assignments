def addition_iteration(no):
    length=len(str(no))
    sum=0
    i=1
    while(i<=length):
        digit=no%10
        sum=sum+digit
        no=no//10
        i=i+1
    print("sum of digits by iteration",sum)   

sum=0
i=1
def addition_recursion(no,length):
    global i
    global sum 
    if(i<=length):
        digit=no%10
        sum=sum+digit
        no=no//10
        i=i+1
        addition_recursion(no,length)
    return sum

def main():
    print("enter number:")
    num=int(input())
    leng=len(str(num))
    addition_iteration(num)
    result=addition_recursion(num,leng)
    print("sum of digits by recursion",result)

if __name__=="__main__":
    main()