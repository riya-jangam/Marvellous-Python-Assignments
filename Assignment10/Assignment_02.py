from functools import reduce

product = lambda A , B : A * B

def main():
    no1 = int(input("Enter first number : "))
    no2 = int(input("Enter second number : "))

    Rdata = reduce(product,(no1,no2))
    print("Product is : ",Rdata)

if __name__ == "__main__":
    main()