def printnum_iteration (no):
    i = 1
    print("Iteration function : ")
    while (i <= no):
        print(i,end=" ")
        i += 1
    print() 
    print("Recursion function : ")

i = 1

def printnum_recursion (no):
    global i
    if(i <= no):
        print(i,end=" ")
        i += 1    
        printnum_recursion(no)


def main():
    num = int(input("Enter Number : "))
    printnum_iteration(num)
    printnum_recursion(num)

if __name__ == "__main__":
    main()