def pattern(no):
    for i in range(no+1):
        for j in range (i):
            print("*",end=" ")
        print()

def main():
    val = int(input("Enter number : "))
    pattern(val)

if __name__ == "__main__":
    main()