def Factorial(no):
    ans = 1
    for i in range(no,0,-1):
        ans *= i
    print("Factorial of",no,"is :",ans)
     
def main():
    val = int(input("Enter number : "))

    Factorial(val)


if __name__ == "__main__":
    main()