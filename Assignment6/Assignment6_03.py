def multiplication_table (no):
    X = 1
    mult = 1
    while X <=10 :
        mult = no * X  
        print(no,"x",X,"=",mult)
        X += 1


def main():
    val = int(input("Enter a number : "))

    multiplication_table(val)

if __name__ == "__main__":
    main()