def prime(no):
    factor = 1
    for i in range (1,no+1):
        if no%i == 0 :
            factor *= i
    if factor == no :
        print(no,"is a prime number")
    else :
        print(no,"is not a prime number")



def main():
    x = int(input("Enter a number : "))

    prime(x)

if __name__=="__main__":
    main()