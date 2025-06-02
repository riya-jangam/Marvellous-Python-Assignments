def pattern_iteration(no):
    print("pattern using iteration: ")
    i=1
    while(i<=no):
        for j in range(i):
            print("*",end=" ")
        i=i+1
        print()

i=1
def pattern_recursion(no):
    global i
    if(i<=no):
        for j in range(i):
            print("*",end=" ")
        i=i+1
        print()
        pattern_recursion(no)

def main():
    print("enter a number")
    num=int(input())
    pattern_iteration(num)
    print("pattern using recursion: ")
    pattern_recursion(num)

if __name__=="__main__":
    main()