def power_iteration(b,e):
    result=1
    while(e>=1):
        result=result*b
        e=e-1
    print("power using iteration: ",result)

result=1
def power_recursion(b,e):
    global result
    if(e>=1):
        result=result*b
        e=e-1
        power_recursion(b,e)
    return result

def main():
    print("enter base: ")
    base=int(input())
    print("enter exponent: ")
    exponent=int(input())
    power_iteration(base,exponent)
    ret=power_recursion(base,exponent)
    print("power using recursion: ",ret)

if __name__=="__main__":
    main()