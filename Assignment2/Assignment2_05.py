def chkprime (num): 
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                print(num, "is not a prime number.")
                break
        else:
            print(num, "is a prime number.")
    else:
        print(num, "is not a prime number.")

def main():
    X = int(input("Enter a number: "))

    chkprime(X)

if __name__ == "__main__":
    main() 