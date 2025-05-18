from Arithmetic import *

def main ():

    print("For Addition -- ")
    X = int(input("Enter value 1 : "))
    Y = int(input("Enter value 2 : "))
    ans = Add(X , Y)
    print("Addition is : ",ans)

    print("For Subtraction -- ")
    X = int(input("Enter Big value  : "))
    Y = int(input("Enter Small value  : "))
    ans = Sub(X , Y)
    print("Subtraction is : ",ans)

    print("For Multiplication -- ")
    X = int(input("Enter value 1 : "))
    Y = int(input("Enter value 2 : "))
    ans = Mult(X , Y)
    print("Multiplication is : ",ans)

    print("For Division -- ")
    X = int(input("Enter value 1 : "))
    Y = int(input("Enter value 2 : "))
    ans = Div(X , Y)
    print("Division is : ",ans)

if __name__ == "__main__" :
    main()
