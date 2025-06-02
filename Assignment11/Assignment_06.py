def addnum_iteration(no):
    i=1
    sum=0
    while(i<=no):
        sum=sum+i
        i=i+1
    print("sum using iteration: ",sum)

i=1
sum=0
def addnum_recursion(no):
    global i
    global sum
    if(i<=no):
        sum=sum+i
        i=i+1
        addnum_recursion(no)
    return sum

def main():
    print("enter a number:")
    num=int(input())
    addnum_iteration(num)
    ret=addnum_recursion(num)
    print("sum using iteration: ",ret)

if __name__=="__main__":
    main()