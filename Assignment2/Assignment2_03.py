def factorial(no):
    for i in range(no-1,0,-1):
        no=no*i
    print("factorial is:",no)

def main():
    print("enter a number:")
    num=int(input())

    factorial(num)


if __name__=="__main__":
    main()