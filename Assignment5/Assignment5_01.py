def main ():
    A = int(input("Enter first number : "))
    B = int(input("Enter second number : "))
    
    Sum = lambda A,B : A + B 
    print("Sum of ",A,"and ",B,"is :",Sum(A,B) )

    Difference = lambda A, B : A - B
    print("Difference of ", A , "and ",B,"is : ",Difference(A,B))

    Product = lambda A,B : A * B
    print("Product of ",A, "and ",B,"is : ",Product(A,B))

    Division = lambda A,B : A/B
    print("Division of ",A,"and",B,"is : ",Division(A,B))



if __name__ == "__main__":
    main()