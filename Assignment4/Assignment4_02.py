multiplication = lambda A ,B : A*B

def main():
    num1 = int(input("Enter Number 1 : "))
    num2 = int(input("Enter Number 2 : "))

    
    ret = multiplication(num1 , num2)

    print("Multiplication is : ",ret )

if __name__ == "__main__":
    main()