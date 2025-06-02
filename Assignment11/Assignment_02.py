def Factorial_iteration(no):
    fact = 1
    while (no>=1):
        fact*= no
        no = no - 1
    print("Iteration funtion : ",fact)


Fact = 1

def Factorial_recursion(no):
    global Fact

    if(no >= 1):
        Fact = Fact * no
        no  = no - 1
        Factorial_recursion(no)
        return Fact
    print ("Recursion function : ",Fact)

def main():
    num = int(input("Enter number : "))
    Factorial_iteration(num)
    Factorial_recursion(num)
    

if __name__ == "__main__":
    main()