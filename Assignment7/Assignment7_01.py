square = lambda A : A**2
cube = lambda A : A ** 3

def main():

    X = int(input("Enter a number : "))

    print("Square of",X,"is :",square(X))
    print("Square of",X,"is :",cube(X))

if __name__ == "__main__":
    main()