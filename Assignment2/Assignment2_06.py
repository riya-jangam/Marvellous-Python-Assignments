def pattern(X):
    for i in range (X,0,-1):
        for j in range (i):
            print("*",end="  ")
        print()

def main():
    num= int(input("Enter number : "))

    pattern(num)
    
    

if __name__ == "__main__":
    main()